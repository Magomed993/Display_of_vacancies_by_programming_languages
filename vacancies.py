import os
import requests
from dotenv import load_dotenv
from terminaltables import AsciiTable


def get_response_hhru(vacant_language, token, page=None):
    moscow_city_id = '1'
    url = 'https://api.hh.ru/vacancies'
    payload = {
        'text': vacant_language,
        'area': moscow_city_id,
        'page': page,
    }
    headers = {
        'Authorization': f'Bearer {token}'
    }
    response = requests.get(url, params=payload, headers=headers)
    response.raise_for_status()
    return response.json()


def get_statistics_hhru(vacant_languages, token):
    full_vacancies = {}
    for language in vacant_languages:
        expected_salaries = []
        page = 0
        last_page = False
        while not last_page:
            full_response = get_response_hhru(language, token, page)
            vacancies = full_response['items']
            for vacancy in vacancies:
                predicted_salary = predict_rub_salary_for_hhru(vacancy['salary'])
                expected_salaries.append(predicted_salary)
            page += 1
            last_page = page == full_response['pages']
        salaries = [i for i in expected_salaries if i]
        if salaries:
            meaning = sum(salaries) / len(salaries)
        else:
            meaning = 0
        full_vacancies[language] = {
            'Вакансий найдено': full_response['found'],
            'Средняя зарплата': int(meaning),
            'Вакансий обработано': len(salaries),
        }
    return full_vacancies


def predict_rub_salary_for_hhru(salary):
    if not salary:
        return None
    salary_from = salary['from']
    salary_to = salary['to']
    return calculates_average_salary(salary_from, salary_to)


def get_response_superjob(vacant_language, secret, access_token, page=None):
    city = 'Москва'
    headers = {
        'X-Api-App-Id': secret,
        'Authorization': f'Bearer {access_token}'
    }
    url_superjob = 'https://api.superjob.ru/2.0/vacancies/'
    params = {
        'page': page,
        'town': city,
        'keyword': vacant_language,
    }
    response = requests.get(url_superjob, headers=headers, params=params)
    response.raise_for_status()
    full_response = response.json()
    return full_response


def get_statistics_superjob(vacant_languages, secret, access_token):
    vacancies = {}
    for language in vacant_languages:
        expected_salaries = []
        page = 0
        more = True
        while more:
            full_response = get_response_superjob(language, secret, access_token, page)
            if not page:
                total_vacancies = full_response['total']
            for vacancy in full_response['objects']:
                expected_salaries.append(predict_rub_salary_for_superJob(vacancy))
            page += 1
            more = full_response['more']
        salaries = [i for i in expected_salaries if i]
        if salaries:
            meaning = sum(salaries) / len(salaries)
        else:
            meaning = 0
        vacancies[language] = {
            'Вакансий найдено': total_vacancies,
            'Средняя зарплата': int(meaning),
            'Вакансий обработано': len(salaries),
        }
    return vacancies


def predict_rub_salary_for_superJob(salary):
    if not salary:
        return None
    salary_from = salary['payment_from']
    salary_to = salary['payment_to']
    return calculates_average_salary(salary_from, salary_to)


def calculates_average_salary(salary_from, salary_to):
    if salary_from and salary_to:
        return int((salary_from + salary_to) / 2)
    elif salary_from:
        return int(salary_from * 1.2)
    elif salary_to:
        return int(salary_to * 0.8)
    return None


def get_table_with_vacancies(handle_vacancies, title=None):
    heading = title
    vacancy_stats = (['Язык программирования'] + list(next(iter(handle_vacancies.values())).keys()))
    table = [vacancy_stats]
    for record, fields in handle_vacancies.items():
        row = [record] + list(fields.values())
        table.append(row)
    table_instance = AsciiTable(table, heading)
    return table_instance.table


if __name__ == '__main__':
    load_dotenv()
    languages = ['Python', 'Java', 'Javascript', '1c', 'ruby', 'C', 'C#', 'C++', 'js', 'go']
    hhru_access_token = os.environ['HHRU_ACCESS_TOKEN']
    superjob_client_secret = os.environ['SUPERJOB_SECRET_KEY']
    superjob_access_token = os.environ['SUPERJOB_ACCESS_TOKEN']

    hhru_title = 'HeadHunter Moscow'
    superjob_title = 'SuperJob Moscow'

    print(get_table_with_vacancies(get_statistics_superjob(
        languages, superjob_client_secret, superjob_access_token), superjob_title))
    print()
    print(get_table_with_vacancies(get_statistics_hhru(languages, hhru_access_token), hhru_title))

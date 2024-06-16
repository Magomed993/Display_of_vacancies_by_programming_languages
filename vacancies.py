import os
import requests
from dotenv import load_dotenv
from terminaltables import AsciiTable


def get_access_token_hhru(client_id, client_secret):
    token_url = 'https://api.hh.ru/token'
    payload = {
        'client_id': client_id,
        'client_secret': client_secret,
        'grant_type': 'client_credentials',
    }
    headers = {
        'User-Agent': 'YourAppName/1.0',
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    response_token = requests.post(token_url, headers=headers, params=payload)
    response_token.raise_for_status()
    token_info = response_token.json()
    access_token = token_info['access_token']
    return access_token


def get_access_token_superjob(code, client_id, client_secret, redirect_uri):
    payload = {
        'code': code,
        'redirect_uri': redirect_uri,
        'client_id': client_id,
        'client_secret': client_secret,
    }
    url_superjob = 'https://api.superjob.ru/2.0/oauth2/access_token/'
    response = requests.post(url_superjob, params=payload)
    response.raise_for_status()
    token_access = response.json()
    return token_access


def get_response_hhru(vacant_languages, token, page=None):
    moscow_city_id = '1'
    url = 'https://api.hh.ru/vacancies'
    payload = {
        'text': vacant_languages,
        'area': moscow_city_id,
        'page': page,
    }
    headers = {
        'Authorization': f'Bearer {token}'
    }
    response = requests.get(url, params=payload, headers=headers)
    response.raise_for_status()
    return response.json()


def get_vacancies_hhru(vacant_languages, token):
    vacancies = {}
    for language in vacant_languages:
        expected_salaries = []
        total_vacancies_processed = 0
        for page in range(100):
            full_response = get_response_hhru(language, token, page)
            information_vacancies = full_response['items']
            for information_vacancy in information_vacancies:
                expected_salaries.append(predict_rub_salary_for_hhru(information_vacancy['salary']))
                if predict_rub_salary_for_hhru(information_vacancy['salary']):
                    total_vacancies_processed += 1
        meaning_salaries = [i for i in expected_salaries if i]
        if meaning_salaries:
            meaning = sum(meaning_salaries) / len(meaning_salaries)
        else:
            meaning = 0
        vacancies[language] = {
            'Вакансий найдено': full_response['found'],
            'Средняя зарплата': int(meaning),
            'Вакансий обработано': total_vacancies_processed,
        }
    return vacancies


def predict_rub_salary_for_hhru(salaries):
    if not salaries:
        return None
    salary_from = salaries['from']
    salary_to = salaries['to']
    return calculates_average_salary(salary_from, salary_to)


def get_response_superjob(vacant_languages, secret, access_token, page=None):
    city = 'Москва'
    headers = {
        'X-Api-App-Id': secret,
        'Authorization': f'Bearer {access_token}'
    }
    url_superjob = 'https://api.superjob.ru/2.0/vacancies/'
    params = {
        'page': page,
        'town': city,
        'keyword': f'{vacant_languages}',
    }
    response = requests.get(url_superjob, headers=headers, params=params)
    response.raise_for_status()
    full_response = response.json()
    return full_response


def get_vacancies_superjob(vacant_languages, secret, access_token):
    vacancies = {}
    for language in vacant_languages:
        expected_salaries = []
        page = 0
        more = True
        while more:
            full_response = get_response_superjob(language, secret, access_token, page)
            if page == 0:
                total_vacancies = full_response['total']
            for vacancy_information in full_response['objects']:
                expected_salaries.append(predict_rub_salary_for_superJob(vacancy_information))
            page += 1
            more = full_response['more']
        meaning_salaries = [i for i in expected_salaries if i]
        if meaning_salaries:
            meaning = sum(meaning_salaries) / len(meaning_salaries)
        else:
            meaning = 0
        vacancies[language] = {
            'Вакансий найдено': total_vacancies,
            'Средняя зарплата': int(meaning),
            'Вакансий обработано': len(meaning_salaries),
        }
    return vacancies


def predict_rub_salary_for_superJob(salaries):
    if not salaries:
        return None
    salary_from = salaries['payment_from']
    salary_to = salaries['payment_to']
    return calculates_average_salary(salary_from, salary_to)


def calculates_average_salary(salary_from, salary_to):
    if salary_from and salary_to:
        return int((salary_from + salary_to) / 2)
    elif salary_from:
        return int(salary_from * 1.2)
    elif salary_to:
        return int(salary_to * 0.8)
    return None


def get_table_with_vacancies(function_of_found_vacancies, title=None):
    heading = title
    extraction = (['Язык программирования'] +
                  list(next(iter(function_of_found_vacancies.values())).keys()))
    table = [extraction]
    for record, fields in function_of_found_vacancies.items():
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

    print(get_table_with_vacancies(get_vacancies_superjob(
        languages, superjob_client_secret, superjob_access_token), superjob_title))
    # print()
    # print(get_table_with_vacancies(get_vacancies_hhru(languages, hhru_access_token), hhru_title))

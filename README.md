# Вывод вакансий по языкам программирования
Программа позволяет выводить количество вакансий г.Москва в виде таблицы по определённым языкам программирования из сайтов SuperJob.ru и hh.ru.
## Как установить
Python3 должен быть уже установлен. Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```
## Окружения
Прежде чем начинать работу, необходимо ознакомиться с документацией для разработчиков [SuperJob](https://api.superjob.ru/) и [hh.ru](https://github.com/hhru/api?tab=readme-ov-file).
Для полноценной работы нужно получить `access_token`, а для его получения необходимо:
1. Зарегистрировать приложение [Регистрация SuperJob](https://api.superjob.ru/info/) и [Регистрация hh.ru](https://dev.hh.ru/admin):
   - Регистрацию приложения производят путем заполнения заявки на сайте [Регистрация SuperJob](https://api.superjob.ru/info/) и [Регистрация hh.ru](https://dev.hh.ru/admin) для разработчиков;
   - После успешной регистрации приложения вы получите `ID`, `Client ID` и `Secret_key`, `Client Secret` приложения для [SuperJob](https://api.superjob.ru/info/) и [hh.ru](https://dev.hh.ru/admin) в личном кабинете для разработчиков;
2. Авторизовать приложение [Авторизация SuperJob](https://api.superjob.ru/#auth) и [Авторизация hh.ru](https://api.hh.ru/openapi/redoc#tag/Avtorizaciya-prilozheniya):
    - Получаем access_token указанного с помощью функции `get_access_token_hhru` и `get_access_token_superjob`;
    - Приложение должно использовать полученный access_token для авторизации, передавая его в заголовке в формате:
      Authorization: Bearer {ACCESS_TOKEN};
3. Получение `access_token` с помощью скриптов:
   - `get_access_token_superjob` - аргументами которых служат данные полученные после регистрации приложения;
   - `get_access_token_hhru` - аргументами которых служат данные полученные после регистрации приложения.
## Переменные окружения
Сгенерированный access_token необходим для установления переменной окружения в секретный файл формата `.env`.
  - для работы функции `get_vacancy_count_superjob` необходимо добавить в переменную окружения `client_secret` и `access_token`, полученные при [регистрации](https://github.com/Magomed993/Display_of_vacancies_by_programming_languages/edit/main/README.md#%D0%BE%D0%BA%D1%80%D1%83%D0%B6%D0%B5%D0%BD%D0%B8%D1%8F) приложения;
  - для работы функции `get_vacancy_count_hh` хватает только `access_token`, полученный при [регистрации](https://github.com/Magomed993/Display_of_vacancies_by_programming_languages/edit/main/README.md#%D0%BE%D0%BA%D1%80%D1%83%D0%B6%D0%B5%D0%BD%D0%B8%D1%8F) приложения.
### Как получить
Для корректной работы `.env` задать в файле `.env` наименование переменной окружения схожей в имеющемся коде, например, `HHRU_ID=(ваш ID)`,
`HHRU_SECRET_KEY=(ваш ключ)` и `HHRU_ACCESS_TOKEN=(ваш access_ключ)`.
## Скрипты и их запуск
```
python vacancies.py
```
Программа получает данные вакансий в г.Москва по языкам программирования:
- Python 
- Java
- Javascript
- 1C
- ruby
- C
- C#
- C++
- js
- go
## Исключения
Из файла `.gitignore` исключить формат `.env` для корректной работы.
## Примечания
Пример работы данного проекта:

![Снимок экрана (9)](https://github.com/Magomed993/Display_of_vacancies_by_programming_languages/assets/160238040/43ce5bf7-2ce9-4c34-9043-e26f05eecfb5)

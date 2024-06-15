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
1. Зарегистрировать приложение [Регистрация SuperJob](https://api.superjob.ru/info/) и [Регистрация hh.ru](https://dev.hh.ru/admin);
   - Регистрацию приложения производят путем заполнения заявки на сайте [Регистрация SuperJob](https://api.superjob.ru/info/) и [Регистрация hh.ru](https://dev.hh.ru/admin) для разработчиков;
2. Авторизовать приложение [Авторизация SuperJob](https://api.superjob.ru/#auth) и [Авторизация hh.ru](https://api.hh.ru/openapi/redoc#tag/Avtorizaciya-prilozheniya);
    - Получаем access_token указанного с помощью функции `get_access_token_hhru` и `get_access_token_superjob`;
    - Приложение должно использовать полученный access_token для авторизации, передавая его в заголовке в формате:
      Authorization: Bearer {ACCESS_TOKEN}.

## Переменные окружения
Сгенерированный access_token необходим для установления переменной окружения в секретный файл формата `.env`.
  - для работы программы SuperJob необходимо добавить в переменную окружения `clietn_secret` и `access_token`;
  - для работы программы hh.ru хватает только `access_token`.
### Как получить
Для корректной работы `.env` задать в файле `.env` наименование переменной окружения схожей в имеющемся коде, например, `HHRU_ID=(ваш ключ)`,
`HHRU_SECRET_KEY=(ваш ключ)` и `HHRU_ACCESS_TOKEN=(адрес группы где будет установлен бот)`.
## Скрипты и их запуск

### python vacancies.py
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
Из файла `.gitignore` исключить формат `.env` для корректного запуска.
## Примечания
Пример работы данного проекта:

![Снимок экрана (9)](https://github.com/Magomed993/Display_of_vacancies_by_programming_languages/assets/160238040/43ce5bf7-2ce9-4c34-9043-e26f05eecfb5)

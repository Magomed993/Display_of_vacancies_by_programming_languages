# Вывод вакансий по языкам программирования
Программа позволяет выводить количество вакансий г.Москва в виде таблицы по определённым языкам программирования из сайтов [SuperJob.ru](https://superjob.ru/) и [hh.ru](https://hh.ru/).
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
   - После успешной регистрации приложения вы получите `ID`, `Client ID` приложения для [SuperJob](https://api.superjob.ru/info/) и `Secret_key`, `Client Secret` приложения для [hh.ru](https://dev.hh.ru/admin) в личном кабинете для разработчиков;
2. Авторизовать приложение [Авторизация SuperJob](https://api.superjob.ru/#auth) и [Авторизация hh.ru](https://api.hh.ru/openapi/redoc#tag/Avtorizaciya-prilozheniya):
3. Получение `access_token` производится согласно инструкции к руководству [hh.ru](https://github.com/hhru/api?tab=readme-ov-file) и [SuperJob](https://api.superjob.ru/).
## Переменные окружения
Сгенерированный access_token необходим для установления переменной окружения в секретный файл формата `.env`.
  - для работы функции `get_statistics_superjob` необходимо добавить в переменную окружения `client_secret` и `access_token`, полученные при [регистрации](#окружения) приложения;
  - для работы функции `get_statistics_hhru` хватает только `access_token`, полученный при [регистрации](#окружения) приложения.
### Как получить
![Снимок экрана (13)](https://github.com/Magomed993/Display_of_vacancies_by_programming_languages/assets/160238040/fe5bfb0a-9575-4195-84e6-a4a15401455d)
1. Создайте файл `.env` в корневом каталоге проекта, если он ещё не существует. Обычно это делается в корневой папке проекта, где находится основной исполняемый файл или файл конфигурации.
2. Откройте файл `.env` в текстовом редакторе и добавьте в него переменные окружения, как показано выше. Убедитесь, что переменные и их значения разделены знаком = без пробелов.
3. Убедитесь в установке с файла `requirements.txt` библиотеки `python-dotenv` для загрузки переменных окружения из файла `.env`.

Теперь у вас должен быть файл `.env`, содержащий все необходимые переменные окружения для корректной работы с API [HeadHunter](https://dev.hh.ru/admin) и [SuperJob](https://api.superjob.ru/info/).\
Получения данных ключей обозначено в заголовке [Окружения](#окружения).\
Данные переменные необходимы для корректной работы программы. От них зависит полномерность выведения данных вакансий на экран.
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
## Примечания
Пример работы данного проекта:

![Снимок экрана (11)](https://github.com/Magomed993/Display_of_vacancies_by_programming_languages/assets/160238040/13b88009-43ea-4170-b095-2a9a4c3652a9)

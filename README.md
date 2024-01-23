## Service for getting the current dollar exchange rate

### Описание проекта
Данное приложение было разработано в рамках тестового задания:
```
Предлагаем вам создать "голый" джанго проект, который  
по переходу на страницу /get-current-usd/ бужет отображать  
в json формате актуальный курс доллара к рублю (запрос по апи,  
найти самостоятельно) и показывать 10 последних запросов  
(паузу между запросами курсов должна быть не менее 10 секунд)  
```

### Технологии
- Python 3.11
- Django 4.2
- Djangorestframework 3.14.0
- Sqlite

### Запуск проекта

1. Склонировать репозиторий:
```
git clone  git@github.com:verafadeeva/test_photopoint.git
```

2. Перейти папку с проектом:
```
cd test_photopoint/
```

3. Создать и активировать виртуальное окружение:
- Windows:
```
C:\> python -m venv venv
C:\> venv\Scripts\activate.bat
```
- Linux / Mac:
```
$ python3 -m venv .venv
$ source .venv/bin/activate
```

4. Установить зависимости:
```
(.venv) pip install -r requirements.txt
```

5. В корневой папке проекта (test_photopoint/) необходимо создать .env файл
```
SECRET_KEY=<django-secret-key>
DEBUG="True"
ALLOWED_HOSTS="host1 host2 host3"

URL=<url-for-getting-data>
APP_ID=<your-api-key>
```

6. В корневой папке проекта (test_photopoint/) выполните миграции:

```
(.venv) ./manage.py migrate
```

7. Запустите сервер:

```
(.venv) ./manage.py runserver
```

### Пример использования
Локально сервер доступен по адресу http://127.0.0.1:8000.

Доступны следующие эндпоинты:

```
1. GET /get-current-usd/
```

Ответ (список из 10 последних запросов):
```
[
    {
        "id": 20,
        "date": "23.01.2024 11:59",
        "base": "USD",
        "rate": "RUB",
        "rate_value": "88.495575"
    },

    ...

    {
        "id": 10,
        "date": "23.01.2024 11:40",
        "base": "USD",
        "rate": "RUB",
        "rate_value": "88.495571"
    },
]
```

### Автор
- Вера Фадеева ([@fadeevavera](https://t.me/fadeevavera))

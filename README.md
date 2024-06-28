# django-faker-db
Скрипт создания тестовой базы данных - генерирует мета модель базы данных, и выполняет миграцию.

##

#### Склонировать репозиторий
```bash
git clone https://github.com/syuqa/django-faker-db.git
```
#### Собрать образ
```bash
docker compose build
```
#### Запустить контейнер (генерация модели и миграция )
после правки переменных В docker-compose.yml и правки конф. файлов (см. ниже).
```BASH
docker compose up
```

## Docker compose
```yml
services:
  faker:
    build: .
    volumes:
    # Шарим директорию с конфигурациямия
      - ./settings:/code/app/faker/conf
    command: /code/entrypoint.sh
    environment:
        # Имя файла с конфигурациями
        FAKER_SETTINGS: oracle
        # Базы данных
        FAKER_DATABASE: SCHEMA1,SCHEMA2,SCHEMA3,SCHEMA4,SCHEMA5,SCHEMA6,SCHEMA7,SCHEMA8,SCHEMA9,SCHEMA10
        # Кол-во баз данных
        CREATE_COUNT_METADATA_DATABASE: 50
        # Кол-во колонок в каждой базе - первичный ключ (он создатся по умолчанию), например что бы было 100 колонок надо указать 99.  
        CREATE_COUNT_METADATA_DATABASE_COLUMNS: 99
        # Типы колонок, через зяпятую (Char, Boolean, Integer, Slug, Auto, Text)
        CREATE_COUNT_METADATA_DATABASE_COLUMNS_TYPES: Char
        # Кол-во связей, всего.
        CREATE_COUNT_METADATA_DATABASE_COLUNNS_FK: 50
```



## Конфигурации баз данных

#### Oracle
File: settings/oracle.py
```python
DEBUG = True

INSTALLED_APPS = [
    'faker_meta_db',
]

DATABASES = {
    'SCHEMA1': {
        'ENGINE': 'django.db.backends.oracle',
        'NAME': '<database>',
        'USER': '<username>',
        'PASSWORD': '<password>',
        'HOST': '<hostname>',
        'PORT': '<port>',
    },
    'default': {}
  }

```

#### PostgreSQL
File: settings/postgres.py
```python
DEBUG = True
INSTALLED_APPS = [
    'django.contrib.contenttypes',
    'django_extensions',
    'faker_meta_db'
]
DATABASES = {
    'SCHEMA1': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '<database>',
        'USER': '<username>',
        'PASSWORD': '<password>',
        'HOST': '<hostname>',
        'PORT': '<port>',
        'OPTIONS': {
            'options': '-c search_path="<schema>"'
        }
    },
  'default': {}
```

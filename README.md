<h2 align="center">FastAPI Short URL service</h2>


### Описание проекта:
Веб-сервис написаный на FastAPI.
- CRUD по сокращениям URL

### Инструменты разработки

**Стек:**
- Python >= 3.8
- FastAPI == 0.61.1
- PostgreSQL

## Разработка

##### 1) Клонировать репозиторий

    git clone ссылка_сгенерированная_в_вашем_репозитории

##### 2) установить pipenv

    pip install pipenv
    
##### 3) Создать виртуальное окружение

    pipenv shell
    
##### 4) Установить зависимости

    pipenv install

##### 5.1) Запустить образ базы данных
    
    docker-compose run postgres
    
##### 5.2) Или запустить postgres самому и создать БД
    

##### 6) Создать в корне файл .env и прописать в нем переменные окружения для подключения к БД
    
    Пример:
    
    DB_USER=postgres
    DB_PASS=postgres
    DB_HOST=localhost
    DB_NAME=short_url

    

##### 7) Выполнить команду для создания миграций

    alembic upgrade head
    
##### 8.1) Запустить сервер

    uvicorn main:app --reload
    
##### 8.2) Или запустить сервер так

    python main.py   
    
##### 9) Перейти по адресу

    http://127.0.0.1:8000/docs
    
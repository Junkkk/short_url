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
    
##### 5.2) Или запустить postgres самому и создать БД short_url 
    

##### 6) Выполнить команду для создания миграций

    alembic upgrade head
    
##### 7.1) Запустить сервер

    uvicorn main:app --reload
    
##### 7.2) Или запустить сервер так

    python main.py   
    
##### 8) Перейти по адресу

    http://127.0.0.1:8000/docs
    
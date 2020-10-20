from starlette.requests import Request


# Получение сессии с БД
def get_db(request: Request):
    return request.state.db

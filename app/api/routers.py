from fastapi import APIRouter
from app.api.endpoints import urls


# Поделючение эндпоинтов к приложению
router = APIRouter()
router.include_router(urls.router)



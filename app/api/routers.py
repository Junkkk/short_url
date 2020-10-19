from fastapi import APIRouter
from app.api.endpoints import urls

router = APIRouter()
router.include_router(urls.router)



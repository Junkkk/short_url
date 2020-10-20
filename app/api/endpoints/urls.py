import validators
import short_url

from fastapi.responses import RedirectResponse
from fastapi import APIRouter, Depends, HTTPException
from app.models.url import schema, service
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from app.api.utils.db import get_db
from app.const import *

router = APIRouter()


# Эндпоинт редиректа по короткому URL
@router.get("/{url_str}")
async def read_url(
        url_str: str,
        db: Session = Depends(get_db)
):
    # Поиск по своему URL
    url_obj = service.get_url_special(db, url_str)
    if url_obj:
        if validators.domain(url_obj.url):
            url_obj.url = "http://" + url_obj.url
        return RedirectResponse(url_obj.url)

    # Поиск по сгенерированному URL
    try:
        url_id = short_url.decode_url(url_str)
        url_obj = service.get_url_id(db, url_id)
        if url_obj:
            return RedirectResponse(url_obj.url)
        raise ValueError
    except ValueError:
        raise HTTPException(status_code=400, detail='Не существующий URL')


# Эндпоинт крафта короткого URL
@router.post("/")
async def create_short_url(
        item: schema.Url,
        db: Session = Depends(get_db)
):
    # Проверка на правильность URL
    if validators.url(item.url) or validators.domain(item.url):
        # Проверка на уже имеющийся в БД свой URL
        try:
            url_obj = service.create_short_url(db, item)
        except IntegrityError:
            return {"url": ALIAS_ALREADY_EXIST}
    else:
        return {"url": INVALID_URL}

    # Конфигурирование URL в зависимости от заданных параметров
    if item.special_url:
        # Проверка на случайное попадание собственного URL в генерируемый
        try:
            short_url.decode_url(item.special_url)
            return {"url": INVALID_ALIAS}
        except ValueError:
            # Проверка правильности заданного собственного URL
            if validators.slug(item.special_url):
                out_url = DOMAIN + item.special_url
            else:
                out_url = INVALID_ALIAS
    else:
        # Крафт URL по его ID в БД
        out_url = "http://127.0.0.1:8000/" + short_url.encode_url(url_obj.id)

    return {"url": out_url}

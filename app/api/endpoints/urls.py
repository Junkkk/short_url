import validators
import short_url

from fastapi.responses import RedirectResponse
from fastapi import APIRouter
from app.models.url import schema


router = APIRouter()


@router.get("/")
async def read_url():
    response = RedirectResponse("https://typer.tiangolo.com")
    return response


@router.post("/")
async def create_short_url(item: schema.Url):
    if validators.url(item.url) or validators.domain(item.url):
        print(True)
    else:
        print(False)

    if item.special_url:
        if validators.slug(item.special_url):
            out_url = "http://127.0.0.1:8000/" + item.special_url
        else:
            out_url = "error"
    else:
        out_url = "http://127.0.0.1:8000/" + short_url.encode_url(1)
    return {
        "url": item.url,
        "date": item.creation_date,
        "days": item.existence_days,
        "short_url": out_url
    }

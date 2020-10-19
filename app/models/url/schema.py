from pydantic import BaseModel
from datetime import datetime


class Url(BaseModel):
    url: str
    creation_date: datetime = datetime.now()
    existence_days: int = 7
    special_url: str = None


class UrlDB(Url):
    id: int
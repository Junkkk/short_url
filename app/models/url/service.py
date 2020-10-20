from sqlalchemy.orm import Session
from app.models.url import schema, model
from fastapi.encoders import jsonable_encoder
from datetime import timedelta


def create_short_url(db: Session, item: schema.Url):
    db_item = model.Url(**item.dict())
    db_item.end_date = db_item.creation_date + timedelta(days=db_item.existence_days)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

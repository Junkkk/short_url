from sqlalchemy.orm import Session
from app.models.url import schema, model
from datetime import timedelta


#
def create_short_url(db: Session, item: schema.Url):
    db_item = model.Url(**item.dict())
    db_item.end_date = db_item.creation_date + timedelta(days=db_item.existence_days)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def get_url_id(db: Session, url_id: int):
    return db.query(model.Url).get(url_id)


def get_url_special(db: Session, special_url: str):
    out_data = db.query(model.Url).filter_by(special_url=special_url).first()
    return out_data

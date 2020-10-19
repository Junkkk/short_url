from sqlalchemy import Column, String, Integer, DateTime
from db.session import Base


class Url(Base):
    __tablename__ = 'urls'
    id = Column(Integer, primary_key=True)
    url = Column(String, nullable=False)
    creation_date = Column(DateTime)
    end_date = Column(DateTime)
    existence_days = Column(Integer)
    special_url = Column(String)

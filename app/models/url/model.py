from sqlalchemy import Column, String, Integer, DateTime
from db.base import Base


class Task(Base):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True)
    url = Column(String, nullable=False)
    creation_date = Column(DateTime)
    existence_days = Column(Integer)

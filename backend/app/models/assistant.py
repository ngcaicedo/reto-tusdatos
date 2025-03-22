from app.db.base import BaseModel
from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime


class Assistant(BaseModel):
    __tablename__ = "assistants"

    email = Column(String, index=True, nullable=False)
    phone = Column(String, index=True, nullable=False)

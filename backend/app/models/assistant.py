from app.db.base import Base
from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime


class Assistant(Base):
    __tablename__ = "assistants"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    email = Column(String, index=True, nullable=False)
    phone = Column(String, index=True, nullable=False)
    created_at = Column(DateTime, index=True,
                        default=datetime.now, nullable=False)
    updated_at = Column(DateTime, index=True, nullable=False)

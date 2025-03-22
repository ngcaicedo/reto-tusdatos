from app.db.base import Base
from sqlalchemy import Column, Integer, String, DateTime, Enum
import enum
from datetime import datetime

class StateEnum(enum.Enum):
    CREADO = "CREADO"
    PROGRAMADO = "PROGRAMADO"
    TERMINADO = "TERMINADO"
    CANCELADO = "CANCELADO"

class Event(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    description = Column(String, index=True)
    capacity = Column(Integer, index=True, nullable=False)
    state = Column(Enum(StateEnum, name="state"), index=True, nullable=False)
    created_at = Column(DateTime, index=True, default=datetime.now, nullable=False)
    updated_at = Column(DateTime, index=True, default=datetime.now, nullable=False)
    date_start = Column(DateTime, nullable=False)
    date_end = Column(DateTime, nullable=False)
    location = Column(String, index=True)

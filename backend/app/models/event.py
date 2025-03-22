from app.db.base import BaseModel
from sqlalchemy import Column, Integer, String, DateTime, Enum
import enum
from datetime import datetime


class StateEnum(enum.Enum):
    CREADO = "CREADO"
    PROGRAMADO = "PROGRAMADO"
    TERMINADO = "TERMINADO"
    CANCELADO = "CANCELADO"


class Event(BaseModel):
    __tablename__ = "events"

    description = Column(String, index=True)
    capacity = Column(Integer, index=True, nullable=False)
    state = Column(Enum(StateEnum, name="state"), index=True, nullable=False)
    date_start = Column(DateTime, nullable=False)
    date_end = Column(DateTime, nullable=False)
    location = Column(String, index=True)

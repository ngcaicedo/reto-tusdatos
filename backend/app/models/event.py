from app.db.base import BaseModel
from sqlalchemy import Column, Integer, String, DateTime, Enum, ForeignKey
import enum
from sqlalchemy.orm import relationship


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
    user_created_id = Column(Integer, ForeignKey("users.id"))
    
    users = relationship("User", back_populates="events")
    
    sessions = relationship("Session", back_populates="event")
    assistants = relationship("Assistant", secondary="event_assistant", back_populates="events")

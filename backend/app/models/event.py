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
    """
    Modelo que representa un evento.

    Relaciones:
    - Un evento puede tener múltiples sesiones (`sessions`), pero estas no se eliminan automáticamente
      si el evento es eliminado. Esto permite conservar las sesiones para fines de auditoría o histórico.
    - Un evento puede tener múltiples asistentes (`assistants`) mediante una relación muchos a muchos.
    - Un evento es creado por un usuario (`user_created_id`) a través de una relación con `User`.

    Notas:
    - No se aplica `cascade="all, delete-orphan"` en la relación con sesiones,
      ya que estas pueden seguir siendo útiles después de eliminar el evento.
    """
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

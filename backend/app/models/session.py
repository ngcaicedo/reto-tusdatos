from app.db.base import BaseModel
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class Speaker(BaseModel):
    """
    Modelo que representa un orador.
    
    Relaciones:
    - Un orador puede tener múltiples sesiones (`sessions`).
    """
    __tablename__ = "speakers"

    sessions = relationship("Session", back_populates="speaker")


class Session(BaseModel):
    """
    Modelo que representa una sesión de un evento.
    
    Relaciones:
    - Una sesión pertenece a un evento (`event`).
    - Una sesión tiene un orador (`speaker`).
    
    Notas:
    - No se aplica `cascade="all, delete-orphan"` en la relación con orador,
      ya que este puede seguir siendo útil después de eliminar la sesión.
    """
    __tablename__ = "sessions"

    description = Column(String, index=True, nullable=False)
    duration = Column(Integer, index=True, nullable=False)
    event_id = Column(Integer, ForeignKey("events.id"))
    speaker_id = Column(Integer, ForeignKey("speakers.id"), nullable=False)

    event = relationship("Event", back_populates="sessions")
    speaker = relationship("Speaker", back_populates="sessions")

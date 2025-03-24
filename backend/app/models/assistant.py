from app.db.base import BaseModel
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class Assistant(BaseModel):
    """
    Modelo que representa un asistente.
    
    Relaciones:
    - Un asistente pertenece a un usuario (`user`).
    - Un asistente puede asistir a múltiples eventos (`events`) mediante una relación muchos a muchos.
    
    Notas:
    - Se aplica `unique=True` en el campo `user_id` para evitar que un usuario tenga más de un registro en asistente.
    """
    __tablename__ = "assistants"

    email = Column(String, index=True, nullable=False)
    phone = Column(String, index=True, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False, unique=True)
    
    user = relationship("User", back_populates="assistant")
    events = relationship("Event", secondary="event_assistant", back_populates="assistants")

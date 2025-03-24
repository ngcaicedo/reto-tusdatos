from app.db.base import BaseModel
from sqlalchemy import Column, Integer, String, DateTime, Enum
import enum
from sqlalchemy.orm import relationship


class RoleEnum(enum.Enum):
    ADMIN = "ADMIN"
    ORGANIZADOR = "ORGANIZADOR"
    ASISTENTE = "ASISTENTE"


class User(BaseModel):
    """
    Modelo que representa un usuario.
    
    Relaciones:
    - Un usuario puede crear múltiples eventos (`events`).
    - Un usuario puede ser un asistente (`assistant`) en un evento.
    
    Notas:
    - Se aplica `cascade="all, delete-orphan"` en la relación con asistente, ya que no tiene sentido conservar el registro
      si el usuario es eliminado.
    """
    __tablename__ = "users"

    phone = Column(String, index=True, nullable=False)
    email = Column(String, index=True, nullable=False, unique=True)
    password = Column(String, nullable=False)
    role = Column(Enum(RoleEnum, name="role"), index=True, nullable=False)
    
    events = relationship("Event", back_populates="users")
    assistant = relationship("Assistant", back_populates="user", uselist=False, cascade="all, delete-orphan")

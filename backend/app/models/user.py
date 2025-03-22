from app.db.base import BaseModel
from sqlalchemy import Column, Integer, String, DateTime, Enum
import enum
from datetime import datetime


class RoleEnum(enum.Enum):
    ADMIN = "ADMIN"
    ORGANIZADOR = "ORGANIZADOR"
    ASISTENTE = "ASISTENTE"


class User(BaseModel):
    __tablename__ = "users"

    phone = Column(String, index=True, nullable=False)
    email = Column(String, index=True)
    password = Column(String, nullable=False)
    role = Column(Enum(RoleEnum, name="role"), index=True, nullable=False)

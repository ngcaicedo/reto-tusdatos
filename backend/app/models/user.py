from app.db.base import Base
from sqlalchemy import Column, Integer, String, DateTime, Enum
import enum
from datetime import datetime

class RoleEnum(enum.Enum):
    ADMIN = "ADMIN"
    ORGANIZADOR = "ORGANIZADOR"
    ASISTENTE = "ASISTENTE"

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    phone = Column(String, index=True, nullable=False)
    email = Column(String, index=True)
    password = Column(String, nullable=False)
    role = Column(Enum(RoleEnum, name="role"), index=True, nullable=False)
    created_at = Column(DateTime, index=True, default=datetime.now, nullable=False)
    updated_at = Column(DateTime, index=True, default=datetime.now, nullable=False)
    
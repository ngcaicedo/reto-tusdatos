from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime

# Base común para todos los modelos
Base = declarative_base()


class BaseModel(Base):
    """ Modelo base para todos los modelos de la aplicación """
    __abstract__ = True
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    created_at = Column(DateTime, index=True,
                        default=datetime.now, nullable=False)
    updated_at = Column(DateTime, index=True,
                        default=datetime.now, nullable=False)

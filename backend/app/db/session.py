from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.config import settings

DATABASE_URL = settings.DATABASE_URL

# Crear el motor de la base de datos
engine = create_engine(DATABASE_URL, echo=True)

# Crear la sesión de SQLAlchemy
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    """ Dependencia para obtener la sesión de la base de datos """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
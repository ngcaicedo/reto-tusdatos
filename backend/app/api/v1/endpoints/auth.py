from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.core.managment import Managment
from app.schemas.user import Token

managment = Managment()

auth_router = APIRouter()


@auth_router.post("/login", response_model=Token)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    """ 
    Endpoint para autenticar un usuario 

    Args:
        form_data (OAuth2PasswordRequestForm): Datos del formulario de autenticación
        db (Session): Sesión de la base de datos

    Returns:
        Token: Token de autenticación
    """
    return managment.login(form_data, db)

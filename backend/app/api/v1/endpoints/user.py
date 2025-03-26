from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.core.managment import Managment
from app.schemas.user import UserResponse, UserCreate
from app.schemas.assistant import AssistantResponse, AssistantCreate
from app.models.user import User
from app.core.authenticator.auth import get_current_user

managment = Managment()

user_router = APIRouter()


@user_router.post("/register", response_model=UserResponse, status_code=201)
def register_user(user_data: UserCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    """ 
    Endpoint para registrar un usuario
    
    Args:
        user_data (UserCreate): Datos del usuario a registrar
        db (Session): Sesión de la base de datos
    
    Returns:
        UserResponse: Usuario registrado
    """
    return managment.create_user(db, user_data)


@user_router.post("/register/assistant", response_model=AssistantResponse, status_code=201)
def register_user_assistant(assistant_data: AssistantCreate, db: Session = Depends(get_db)):
    """ 
    Endpoint para registrar un asistente
    
    Args:
        assistant_data (AssistantCreate): Datos del asistente a registrar
        db (Session): Sesión de la base de datos
    
    Returns:
        AssistantResponse: Asistente registrado
    """
    return managment.register_user_assistant(db, assistant_data)
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.core.managment import Managment
from app.schemas.user import UserResponse, UserCreate

managment = Managment()

user_router = APIRouter()


@user_router.post("/register", response_model=UserResponse, status_code=201)
def register_user(user_data: UserCreate, db: Session = Depends(get_db)):
    """ 
    Endpoint para registrar un usuario
    
    Args:
        user_data (UserCreate): Datos del usuario a registrar
        db (Session): Sesión de la base de datos
    
    Returns:
        UserResponse: Usuario registrado
    """
    return managment.create_user(db, user_data)

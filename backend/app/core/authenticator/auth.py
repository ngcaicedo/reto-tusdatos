from fastapi.security import OAuth2PasswordRequestForm
from fastapi import HTTPException, status
from .security import verify_password
from .jwt_utils import create_access_token
from app.models import User
from sqlalchemy.orm import Session
from app.schemas.user import UserLogin


def authenticate_user(db: Session, login_data: UserLogin) -> User | None:
    """ 
    Función para autenticar un usuario 

    Args:
        db (Session): Sesión de la base de datos
        email (str): Correo electrónico del usuario
        password (str): Contraseña del usuario

    Returns:
        User | None: Usuario autenticado
    """

    user = db.query(User).filter(User.email == login_data.username).first()
    if user and verify_password(user.password, login_data.password):
        return user
    return None


def generate_token(data):
    """ Función para crear un token de acceso """
    return create_access_token(data=data)


def login_user(form_data: OAuth2PasswordRequestForm, db: Session) -> dict:
    """ 
    Función para autenticar un usuario

    Args:
        form_data (OAuth2PasswordRequestForm): Datos del formulario de autenticación
        db (Session): Sesión de la base de datos

    Returns:
        dict: Token de autenticación
    """

    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Credenciales incorrectas",
        headers={"WWW-Authenticate": "Bearer"},
    )

    user = authenticate_user(db, form_data)
    if not user:
        raise credentials_exception
    token = generate_token({"sub": user.email})
    return {
        "token": token,
        "token_type": "bearer",
        "user": user.email,
        "role": user.role
    }

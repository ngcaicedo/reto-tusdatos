from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi import Depends, HTTPException, status
import jwt
from jwt.exceptions import InvalidTokenError

from .security import verify_password
from .jwt_utils import create_access_token, SECRET_KEY, ALGORITHM
from app.models import User
from sqlalchemy.orm import Session
from app.schemas.user import UserLogin
from app.db.session import get_db


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

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
        "user": user.name,
        "role": user.role,
        "user_id": user.id
    }


def get_current_user(db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)) -> User:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="No autorizado",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
    except InvalidTokenError:
        raise credentials_exception

    user = db.query(User).filter(User.email == email).first()
    if user is None:
        raise credentials_exception

    return user

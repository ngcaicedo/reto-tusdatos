from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.core.authenticator.auth import authenticate_user, generate_token
from app.schemas.user import Token

auth_router = APIRouter(prefix="/auth", tags=["auth"])


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

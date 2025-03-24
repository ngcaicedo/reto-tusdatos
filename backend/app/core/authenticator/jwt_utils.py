import jwt
from datetime import timedelta, datetime, timezone
from jwt.exceptions import InvalidTokenError
from dotenv import load_dotenv
import os

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY", "test_secret_key")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60


def create_access_token(data: dict, expires_delta: timedelta | None = None) -> str:
    """ Función para crear un token de acceso 
    
    Args:
        data (dict): Datos a codificar en el token
        expires_delta (timedelta | None): Duración del token
    
    Returns:
        str: Token de acceso
    """
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + \
            timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    
    encode_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encode_jwt


def decode_access_token(token: str) -> dict:
    """ Función para decodificar un token
    
    Args:
        token (str): Token a decodificar
    
    Returns:
        dict: Datos decodificados
    """
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except InvalidTokenError:
        return {}
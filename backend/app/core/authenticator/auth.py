from .security import hash_password, verify_password
from .jwt_utils import create_access_token, decode_access_token
from app.models import User
from sqlalchemy.orm import Session


def authenticate_user(db: Session, email: str, password: str) -> User | None:
    """ 
    Función para autenticar un usuario 
    
    Args:
        db (Session): Sesión de la base de datos
        email (str): Correo electrónico del usuario
        password (str): Contraseña del usuario
        
    Returns:
        User | None: Usuario autenticado
    """
    
    user = db.query(User).filter(User.email == email).first()
    print(user.password, password)
    if user and verify_password(user.password, password):
        return user
    return None
from .security import verify_password
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
    
    user = db.query(User).filter(User.email == login_data.email).first()
    if user and verify_password(user.password, login_data.password):
        return user
    return None
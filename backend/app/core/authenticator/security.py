from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str) -> str:
    """ Encripta una contraseña 
    
    Args:
        password (str): Contraseña en texto plano
        
    Returns:
        str: Contraseña encriptada
    """
    return pwd_context.hash(password)


def verify_password(hashed_password: str, plain_password: str) -> bool:
    """ Verifica que la contraseña en texto plano coincida con la contraseña encriptada 
    
    Args:
        hashed_password (str): Contraseña encriptada
        plain_password (str): Contraseña en texto plano
        
    Returns:
        bool: True si la contraseña en texto plano coincide con la contraseña encriptada, False en caso contrario
    """
    return pwd_context.verify(plain_password, hashed_password)

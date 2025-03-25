from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserCreate, RoleEnum
from app.schemas.assistant import AssistantCreate
from app.models.assistant import Assistant
from app.core.authenticator.security import hash_password
from fastapi import HTTPException, status

def create_user(db: Session, user_data: UserCreate):
    """ Crea un usuario en la base de datos.
    Args:
        db (Session): Sesión de la base de datos
        user_data (UserCreate): Datos del usuario a crear
    Returns:
        User: Usuario creado
    """
    user_exception = HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail="El usuario ya se encuentra registrado",
        headers={"WWW-Authenticate": "Bearer"},
    )
    existing_user = db.query(User).filter(User.email == user_data.email).first()
    if existing_user:
        raise user_exception
    
    db_user = User(
        name=user_data.name,
        phone=user_data.phone,
        email=user_data.email,
        password=hash_password(user_data.password),
        role=user_data.role
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def register_user_assistant(db: Session, assistant_data: AssistantCreate) -> Assistant:
    """Registra un usuario con rol ASISTENTE y crea su perfil de asistente.
    
    Args:
        db (Session): Sesión de la base de datos
        assistant_data (AssistantCreate): Datos del asistente a registrar
    Returns:
        Assistant: Asistente registrado
    """

    if assistant_data.role != RoleEnum.ASISTENTE:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Solo los usuarios con rol ASISTENTE pueden registrarse como asistentes.",
        )

    existing_user = db.query(User).filter(User.email == assistant_data.email).first()
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El usuario ya se encuentra registrado",
        )

    user = User(
        name=assistant_data.name,
        email=assistant_data.email,
        phone=assistant_data.phone,
        password=hash_password(assistant_data.password),
        role=RoleEnum.ASISTENTE,
    )
    db.add(user)
    db.commit()
    db.refresh(user)

    assistant = Assistant(
        name=assistant_data.name,
        email=assistant_data.email,
        phone=assistant_data.phone,
        user_id=user.id,
    )
    db.add(assistant)
    db.commit()
    db.refresh(assistant)

    return assistant

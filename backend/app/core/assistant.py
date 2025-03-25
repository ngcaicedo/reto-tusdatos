from sqlalchemy.orm import Session
from app.schemas.assistant import AssistantCreate, AssistantUpdate, AssistantResponse
from app.models.assistant import Assistant
from app.models.user import User
from fastapi import HTTPException, status


def create_assistant(db: Session, assistant_data: AssistantCreate):
    """ Función para registrar un asistente 

    Args:
        db (Session): Sesión de la base de datos
        assistant_data (AssistantCreate): Datos del asistente a registrar
    Returns:
        Assistant: Asistente registrado
    """

    assistant_exception = HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail="El asistente ya se encuentra registrado",
        headers={"WWW-Authenticate": "Bearer"},
    )

    existing_assistant = db.query(Assistant).filter(
        Assistant.email == assistant_data.email).first()
    if existing_assistant:
        raise assistant_exception

    user = User(
        name=assistant_data.name,
        email=assistant_data.email,
        password=assistant_data.password,
        phone=assistant_data.phone,
        role=assistant_data.role
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    assistant = Assistant(
        name=assistant_data.name,
        email=assistant_data.email,
        phone=assistant_data.phone,
        user_id=user.id
    )
    db.add(assistant)
    db.commit()
    db.refresh(assistant)
    return assistant


def update_assistant(db: Session, assistant_id: int, assistant_data: AssistantUpdate):
    """ Función para actualizar un asistente

    Args:
        db (Session): Sesión de la base de datos
        assistant_id (int): Identificador del asistente a actualizar
        assistant_data (AssistantUpdate): Datos del asistente a actualizar
    Returns:
        Assistant: Asistente actualizado
    """

    assistant = db.query(Assistant).filter(
        Assistant.id == assistant_id).first()
    if not assistant:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="El asistente no se encuentra registrado",
            headers={"WWW-Authenticate": "Bearer"},
        )

    assistants = db.query(Assistant).filter(
        Assistant.name == assistant_data.name, Assistant.id != assistant_id).all()
    if len(assistants) >= 1:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El asistente ya se encuentra registrado",
            headers={"WWW-Authenticate": "Bearer"},)

    assistant.name = assistant_data.name
    assistant.phone = assistant_data.phone
    db.commit()
    db.refresh(assistant)
    return assistant


def get_assistants(db: Session):
    """ Función para obtener todos los asistentes

    Args:
        db (Session): Sesión de la base de datos
    Returns:
        List[Assistant]: Lista de asistentes
    """

    assistants = db.query(Assistant).all()
    return assistants


def get_assistant(db: Session, assistant_id: int):
    """ Función para obtener un asistente

    Args:
        db (Session): Sesión de la base de datos
        assistant_id (int): Identificador del asistente a obtener
    Returns:
        Assistant: Asistente obtenido
    """

    assistant = db.query(Assistant).filter(
        Assistant.id == assistant_id).first()
    if not assistant:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="El asistente no se encuentra registrado",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return assistant

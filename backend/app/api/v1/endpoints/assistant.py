from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.core.managment import Managment
from app.schemas.assistant import AssistantCreate, AssistantUpdate, AssistantResponse
from app.core.authenticator.auth import get_current_user

managment = Managment()

assistant_router = APIRouter()

@assistant_router.post("/create", response_model=AssistantResponse, status_code=201)
def create_assistant(assistant_data: AssistantCreate, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    """ 
    Endpoint para registrar un asistente
    Args:
        assistant_data (AssistantCreate): Datos del asistente a registrar
        db (Session): Sesión de la base de datos
        current_user (User): Usuario autenticado
    Returns:
        AssistantCreate: Asistente registrado
    """
    return managment.create_assistant(db, assistant_data)

@assistant_router.put("/update/{assistant_id}", response_model=AssistantResponse)
def update_assistant(assistant_id: int, assistant_data: AssistantUpdate, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    """ 
    Endpoint para actualizar un asistente
    Args:
        assistant_id (int): Identificador del asistente a actualizar
        assistant_data (AssistantUpdate): Datos del asistente a actualizar
        db (Session): Sesión de la base de datos
        current_user (User): Usuario autenticado
    Returns:
        AssistantResponse: Asistente actualizado
    """
    return managment.update_assistant(db, assistant_id, assistant_data)

@assistant_router.get("/assistants", response_model=list[AssistantResponse])
def get_assistants(db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    """ 
    Endpoint para obtener la lista de asistentes
    Args:
        db (Session): Sesión de la base de datos
        current_user (User): Usuario autenticado
    Returns:
        list[AssistantResponse]: Lista de asistentes
    """
    return managment.get_assistants(db)

@assistant_router.get("/{assistant_id}", response_model=AssistantResponse)
def get_assistant(assistant_id: int, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    """ 
    Endpoint para obtener un asistente
    Args:
        assistant_id (int): Identificador del asistente a obtener
        db (Session): Sesión de la base de datos
        current_user (User): Usuario autenticado
    Returns:
        AssistantResponse: Asistente
    """
    return managment.get_assistant(db, assistant_id)
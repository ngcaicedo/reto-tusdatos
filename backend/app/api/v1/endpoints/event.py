from typing import Optional
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.core.managment import Managment
from app.schemas.event import EventCreate, EventResponse, EventUpdate
from app.models.user import User
from app.core.authenticator.auth import get_current_user, get_current_user_optional
from app.models.assistant import Assistant

managment = Managment()

event_router = APIRouter()


@event_router.post("/create", response_model=EventResponse, status_code=201)
def create_event(event_data: EventCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    """ 
    Endpoint para registrar un evento
    Args:
        event_data (EventCreate): Datos del evento a registrar
        db (Session): Sesión de la base de datos
        current_user (User): Usuario autenticado
    Returns:
        EventResponse: Evento registrado
    """
    return managment.create_event(db, event_data, current_user)


@event_router.put("/update/{event_id}", response_model=EventResponse)
def update_event(event_id: int, event_data: EventUpdate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    """ 
    Endpoint para actualizar un evento
    Args:
        event_id (int): Identificador del evento a actualizar
        event_data (EventUpdate): Datos del evento a actualizar
        db (Session): Sesión de la base de datos
        current_user (User): Usuario autenticado
    Returns:
        EventResponse: Evento actualizado
    """
    return managment.update_event(db, event_id, event_data)

@event_router.get("/assistant/register", response_model=list[EventResponse])
def get_events_register_by_assistant(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    """ 
    Endpoint para obtener la lista de eventos registrados por un asistente
    Args:
        db (Session): Sesión de la base de datos
        current_user (User): Usuario autenticado
    Returns:
        list[EventResponse]: Lista de eventos registrados por el asistente
    """
    return managment.get_events_register_by_assistant(db, current_user)


@event_router.get("/events", response_model=list[EventResponse])
def get_events(db: Session = Depends(get_db)):
    """ 
    Endpoint para obtener la lista de eventos
    Args:
        db (Session): Sesión de la base de datos
        current_user (User): Usuario autenticado
    Returns:
        list[EventResponse]: Lista de eventos
    """
    return managment.get_events(db)


@event_router.get("/{event_id}", response_model=EventResponse)
def get_event(event_id: int, db: Session = Depends(get_db), current_user: Optional[Assistant] = Depends(get_current_user_optional)):
    """ 
    Endpoint para obtener un evento
    Args:
        event_id (int): Identificador del evento a obtener
        db (Session): Sesión de la base de datos
        current_user (User): Usuario autenticado
    Returns:
        EventResponse: Evento obtenido
    """
    event = managment.get_event(db, event_id)
    is_registered = (
        any(assistant.id == current_user.id for assistant in event.assistants)
        if current_user
        else False
    )
    
    evnt_mod = EventResponse.model_validate(event).model_dump()
    evnt_mod["is_registered"] = is_registered
    return evnt_mod


@event_router.post("/register/{event_id}", status_code=201)
def register_to_event(event_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    """ 
    Endpoint para registrar un usuario a un evento
    Args:
        event_id (int): Identificador del evento a registrar
        db (Session): Sesión de la base de datos
        current_user (User): Usuario autenticado
    """
    managment.register_to_event(db, event_id, current_user)
    return {"message": "Registro exitoso", "event_id": event_id}
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.core.managment import Managment
from app.schemas.event import EventCreate, EventResponse, EventUpdate
from app.models.user import User
from app.core.authenticator.auth import get_current_user

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
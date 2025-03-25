from sqlalchemy.orm import Session
from app.models.user import User
from app.models.event import Event
from app.schemas.event import EventCreate, EventUpdate
from app.core.authenticator.security import hash_password
from fastapi import HTTPException, status


def create_event(db: Session, event_data: EventCreate, current_user: User):
    """
    Crea un evento en la base de datos.

    Args:
        db (Session): Sesión de la base de datos
        event_data (EventCreate): Datos del evento a crear
        current_user (User): Usuario autenticado
    """

    event_exception = HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail="El evento ya se encuentra registrado",
        headers={"WWW-Authenticate": "Bearer"},
    )
    existing_event = db.query(Event).filter(
        Event.name == event_data.name).first()
    if existing_event:
        raise event_exception

    db_event = Event(
        name=event_data.name,
        description=event_data.description,
        capacity=event_data.capacity,
        state=event_data.state,
        date_start=event_data.date_start,
        date_end=event_data.date_end,
        location=event_data.location,
        user_created_id=current_user.id
    )
    db.add(db_event)
    db.commit()
    db.refresh(db_event)
    return db_event


def update_event(db: Session, event_id: id, event_data: EventUpdate):
    """
    Actualiza un evento en la base de datos.

    Args:
        db (Session): Sesión de la base de datos
        event (Event): Evento a actualizar
        event_data (EventCreate): Datos del evento a actualizar
    """

    event = db.query(Event).filter(Event.id == event_id).first()
    if not event:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="El evento no se encuentra registrado",
            headers={"WWW-Authenticate": "Bearer"},
        )
        
    events = db.query(Event).filter(Event.name == event_data.name).all()
    if len(events) > 1:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El evento ya se encuentra registrado",
            headers={"WWW-Authenticate": "Bearer"},
        )

    event.name = event_data.name
    event.description = event_data.description
    event.capacity = event_data.capacity
    event.state = event_data.state
    event.date_start = event_data.date_start
    event.date_end = event_data.date_end
    event.location = event_data.location
    db.commit()
    db.refresh(event)
    return event


def get_events(db: Session):
    """
    Obtiene todos los eventos registrados en la base de datos.

    Args:
        db (Session): Sesión de la base de datos
    
    Returns:
        list[Event]: Lista de eventos registrados
    """
    return db.query(Event).all()

def get_event(db: Session, event_id: int):
    """
    Obtiene un evento registrado en la base de datos.

    Args:
        db (Session): Sesión de la base de datos
        event_id (int): Identificador del evento a obtener
    
    Returns:
        Event: Evento registrado
    """
    return db.query(Event).filter(Event.id == event_id).first()
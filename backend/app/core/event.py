from sqlalchemy.orm import Session
from app.models.user import User
from app.models.event import Event
from app.schemas.event import EventCreate
from app.core.authenticator.security import hash_password
from fastapi import HTTPException, status

def create_event(db: Session, user_data: EventCreate, current_user: User):
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
    existing_event = db.query(Event).filter(Event.name == user_data.name).first()
    if existing_event:
        raise event_exception
    
    db_event = Event(
        name=user_data.name,
        description=user_data.description,
        capacity=user_data.capacity,
        state=user_data.state,
        date_start=user_data.date_start,
        date_end=user_data.date_end,
        location=user_data.location,
        user_created_id=current_user.id
    )
    db.add(db_event)
    db.commit()
    db.refresh(db_event)
    return db_event
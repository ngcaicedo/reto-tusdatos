from sqlalchemy.orm import Session
from app.models.user import User, RoleEnum
from app.models.event_assistant import EventAssistant
from app.models.event import Event
from app.schemas.event import EventCreate, EventUpdate
from app.core.authenticator.security import hash_password
from fastapi import HTTPException, status
from app.models.session import Session as SessionModel
from sqlalchemy.orm import joinedload


def create_event(db: Session, event_data: EventCreate, current_user: User):
    """
    Crea un evento en la base de datos, lo asocia a un usuario y a las sesiones.

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
    
    sessions = db.query(SessionModel).filter(SessionModel.id.in_(event_data.session_ids)).all()
    
    if len(sessions) != len(event_data.session_ids):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="No se encontraron todas las sesiones",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    for session in sessions:
        session.event_id = db_event.id
    
    db.commit()
    return db_event


def update_event(db: Session, event_id: int, event_data: EventUpdate):
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
        
    events = db.query(Event).filter(Event.name == event_data.name, Event.id != event_id).all()
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
    
    
    sessions = db.query(SessionModel).filter(SessionModel.id.in_(event_data.session_ids)).all()
    
    if len(sessions) != len(event_data.session_ids):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="No se encontraron todas las sesiones",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    for session in db.query(SessionModel).filter(SessionModel.event_id == event_id).all():
        session.event_id = None
    
    for session in sessions:
        session.event_id = event_id
        
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
    return db.query(Event).order_by(Event.date_start).all()

def get_event(db: Session, event_id: int):
    """
    Obtiene un evento registrado en la base de datos.

    Args:
        db (Session): Sesión de la base de datos
        event_id (int): Identificador del evento a obtener
    
    Returns:
        Event: Evento registrado
    """
    return db.query(Event).options(joinedload(Event.sessions).joinedload(SessionModel.speaker)).filter(Event.id == event_id).first()


def register_to_event(db: Session, event_id: int, current_user: User):
    """ Se registra un assistente a un evento.
    
    Args:
        db (Session): Sesión de la base de datos
        event_id (int): Identificador del evento
        current_user (User): Usuario autenticado
    
    Returns:
        event_assistant: Asistente registrado
    """
    if current_user.role != RoleEnum.ASISTENTE:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Solo los asistentes pueden registrarse a eventos."
        )

    event = db.query(Event).filter(Event.id == event_id).first()
    if not event:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Evento no encontrado"
        )

    # Validar estado del evento (si aplica)
    if event.state == "CANCELLED":  # o enum
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Este evento ha sido cancelado."
        )

    # Verificar capacidad
    current_attendees = db.query(EventAssistant).filter(EventAssistant.event_id == event_id).count()
    if current_attendees >= event.capacity:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="La capacidad del evento está llena"
        )

    # Verificar si ya está registrado
    already_registered = db.query(EventAssistant).filter(
        EventAssistant.assistant_id == current_user.assistant.id,
        EventAssistant.event_id == event_id
    ).first()
    if already_registered:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El asistente ya se encuentra registrado en el evento"
        )

    # Registrar
    attendee = EventAssistant(assistant_id=current_user.assistant.id, event_id=event_id)
    db.add(attendee)
    db.commit()
    db.refresh(attendee)
    return attendee

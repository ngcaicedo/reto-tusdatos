from app.schemas.session import SpeakerCreate, SpeakerUpdate, SpeakerResponse, SessionCreate, SessionUpdate, SessionResponse
from app.models.session import Session
from app.models.session import Speaker
from fastapi import HTTPException, status

def create_speaker(db, speaker: SpeakerCreate) -> SpeakerResponse:
    """ Función para crear un speaker 
    
    Args:
        db (Session): Sesión de la base de datos
        speaker (SpeakerCreate): Datos del speaker a crear
        
    Returns:
        SpeakerResponse: Datos del speaker creado
    """
    
    speaker_exception = HTTPException(
        status_code=status.HTTP_409_CONFLICT,
        detail="El speaker ya se encuentra registrado",
        headers={"WWW-Authenticate": "Bearer"},
    )
    
    speaker_db = db.query(Speaker).filter(
        Speaker.name == speaker.name).first()
    if speaker_db:
        raise speaker_exception
    speaker_db = Speaker(name=speaker.name)
    db.add(speaker_db)
    db.commit()
    db.refresh(speaker_db)
    return speaker_db


def update_speaker(db, speaker_id: int, speaker: SpeakerUpdate) -> SpeakerResponse:
    """ Función para actualizar un speaker
    
    Args:
        db (Session): Sesión de la base de datos
        speaker_id (int): ID del speaker a actualizar
        speaker (SpeakerUpdate): Datos del speaker a actualizar
    
    Returns:
        SpeakerResponse: Datos del speaker actualizado
    """
    
    speaker_db = db.query(Speaker).filter(Speaker.id == speaker_id).first()
    if not speaker_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="El speaker no se encuentra registrado",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    speaker_duplicate = db.query(Speaker).filter(
        Speaker.name == speaker.name, Speaker.id != speaker_id).first()
    
    if speaker_duplicate:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="El speaker ya se encuentra registrado",
            headers={"WWW-Authenticate": "Bearer"},
        )    
    
    speaker_db.name = speaker.name
    db.add(speaker_db)
    db.commit()
    db.refresh(speaker_db)
    return speaker_db

def get_speakers(db):
    """ Función para obtener todos los speakers
    
    Args:
        db (Session): Sesión de la base de datos
        
    Returns:
        List[Speaker]: Lista de speakers
    """
    
    speakers = db.query(Speaker).all()
    return speakers

def get_speaker(db, speaker_id: int) -> SpeakerResponse:
    """ Función para obtener un speaker por ID 
    
    Args:
        db (Session): Sesión de la base de datos
        speaker_id (int): ID del speaker a obtener
    
    Returns:
        SpeakerResponse: Datos del speaker
    """
    
    speaker = db.query(Speaker).filter(Speaker.id == speaker_id).first()
    if not speaker:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="El speaker no se encuentra registrado",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return speaker


def create_session(db, session: SessionCreate) -> SessionResponse:
    """ Función para crear una sesión
    
    Args:
        db (Session): Sesión de la base de datos
        session (SessionCreate): Datos de la sesión a crear
    
    Returns:
        SessionResponse: Datos de la sesión creada
    """
    
    session_db = db.query(Session).filter(
        Session.name == session.name).first()
    if session_db:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="La sesión ya se encuentra registrada",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    session_db = Session(
        name=session.name,
        description=session.description,
        duration=session.duration,
        speaker_id=session.speaker_id,
    )
    db.add(session_db)
    db.commit()
    db.refresh(session_db)
    return session_db

def update_session(db, session_id: int, session: SessionUpdate) -> SessionResponse:
    """ Función para actualizar una sesión
    
    Args:
        db (Session): Sesión de la base de datos
        session_id (int): ID de la sesión a actualizar
        session (SessionUpdate): Datos de la sesión a actualizar
    
    Returns:
        SessionResponse: Datos de la sesión actualizada
    """
    
    session_db = db.query(Session).filter(Session.id == session_id).first()
    if not session_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="La sesión no se encuentra registrada",
            headers={"WWW-Authenticate": "Bearer"},
        )
        
    session_duplicate = db.query(Session).filter(
        Session.name == session.name, Session.id != session_id).first()
    
    if session_duplicate:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="La sesión ya se encuentra registrada",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    session_db.name = session.name
    session_db.description = session.description
    session_db.duration = session.duration
    session_db.speaker_id = session.speaker_id
    db.add(session_db)
    db.commit()
    db.refresh(session_db)
    return session_db

def get_sessions(db):
    """ Función para obtener todas las sesiones
    
    Args:
        db (Session): Sesión de la base de datos
        
    Returns:
        List[Session]: Lista de sesiones
    """
    
    sessions = db.query(Session).filter(Session.event_id.is_(None)).all()
    return sessions

def get_session(db, session_id: int) -> SessionResponse:
    """ Función para obtener una sesión por ID"""
    
    session = db.query(Session).filter(Session.id == session_id).first()
    if not session:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="La sesión no se encuentra registrada",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return session
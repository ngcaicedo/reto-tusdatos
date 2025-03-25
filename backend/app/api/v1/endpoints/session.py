from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.core.managment import Managment
from app.schemas.session import SpeakerCreate, SpeakerUpdate, SpeakerResponse, SessionCreate, SessionUpdate, SessionResponse
from app.models.user import User
from app.core.authenticator.auth import get_current_user

managment = Managment()

session_router = APIRouter()

@session_router.post("/create/speaker", response_model=SpeakerResponse, status_code=201)
def create_speaker(speaker_data: SpeakerCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    """ 
    Endpoint para registrar un speaker
    Args:
        speaker_data (SpeakerCreate): Datos del speaker a registrar
        db (Session): Sesión de la base de datos
        current_user (User): Usuario autenticado
    Returns:
        SpeakerResponse: Speaker registrado
    """
    return managment.create_speaker(db, speaker_data)

@session_router.put("/update/speaker/{speaker_id}", response_model=SpeakerResponse)
def update_speaker(speaker_id: int, speaker_data: SpeakerUpdate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    """ 
    Endpoint para actualizar un speaker
    Args:
        speaker_id (int): Identificador del speaker a actualizar
        speaker_data (SpeakerUpdate): Datos del speaker a actualizar
        db (Session): Sesión de la base de datos
        current_user (User): Usuario autenticado
    Returns:
        SpeakerResponse: Speaker actualizado
    """
    return managment.update_speaker(db, speaker_id, speaker_data)

@session_router.get("/speakers", response_model=list[SpeakerResponse])
def get_speakers(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    """ 
    Endpoint para obtener la lista de speakers
    Args:
        db (Session): Sesión de la base de datos
        current_user (User): Usuario autenticado
    Returns:
        list[SpeakerResponse]: Lista de speakers
    """
    return managment.get_speakers(db)

@session_router.get("/speaker/{speaker_id}", response_model=SpeakerResponse)
def get_speaker(speaker_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    """ 
    Endpoint para obtener un speaker
    Args:
        speaker_id (int): Identificador del speaker a obtener
        db (Session): Sesión de la base de datos
        current_user (User): Usuario autenticado
    Returns:
        SpeakerResponse: Speaker obtenido
    """
    return managment.get_speaker(db, speaker_id)


@session_router.post("/create", response_model=SessionResponse, status_code=201)
def create_session(session_data: SessionCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    """ 
    Endpoint para registrar una sesión
    Args:
        session_data (SessionCreate): Datos de la sesión a registrar
        db (Session): Sesión de la base de datos
        current_user (User): Usuario autenticado
    Returns:
        SessionResponse: Sesión registrada
    """
    return managment.create_session(db, session_data)

@session_router.put("/update/{session_id}", response_model=SessionResponse)
def update_session(session_id: int, session_data: SessionUpdate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    """ 
    Endpoint para actualizar una sesión
    Args:
        session_id (int): Identificador de la sesión a actualizar
        session_data (SessionUpdate): Datos de la sesión a actualizar
        db (Session): Sesión de la base de datos
        current_user (User): Usuario autenticado
    Returns:
        SessionResponse: Sesión actualizada
    """
    return managment.update_session(db, session_id, session_data)

@session_router.get("/", response_model=list[SessionResponse])
def get_sessions(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    """ 
    Endpoint para obtener la lista de sesiones
    Args:
        db (Session): Sesión de la base de datos
        current_user (User): Usuario autenticado
    Returns:
        list[SessionResponse]: Lista de sesiones
    """
    return managment.get_sessions(db)

@session_router.get("/{session_id}", response_model=SessionResponse)
def get_session(session_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    """ 
    Endpoint para obtener una sesión
    Args:
        session_id (int): Identificador de la sesión a obtener
        db (Session): Sesión de la base de datos
        current_user (User): Usuario autenticado
    Returns:
        SessionResponse: Sesión obtenida
    """
    return managment.get_session(db, session_id)
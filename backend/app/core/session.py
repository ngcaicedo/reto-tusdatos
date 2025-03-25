from app.schemas.session import SpeakerCreate, SpeakerUpdate, SpeakerResponse
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
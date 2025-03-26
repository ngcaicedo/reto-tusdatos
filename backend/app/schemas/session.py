from pydantic import BaseModel, ConfigDict
from datetime import datetime

class SessionBase(BaseModel):
    name: str
    
class SpeakerCreate(SessionBase):
    pass

class SpeakerUpdate(SessionBase):
    pass

class SpeakerResponse(SessionBase):
    id: int
    
class SessionCreate(SessionBase):
    description: str
    duration: int
    date_start: datetime
    speaker_id: int
    
class SessionUpdate(SessionBase):
    description: str
    duration: int
    date_start: datetime
    speaker_id: int
    
class SessionResponse(SessionBase):
    id: int
    description: str
    duration: int
    date_start: datetime
    speaker_id: int
    speaker: SpeakerResponse
    
    model_config = ConfigDict(from_attributes=True)
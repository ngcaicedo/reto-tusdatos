from pydantic import BaseModel

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
    speaker_id: int
    
class SessionUpdate(SessionBase):
    description: str
    duration: int
    speaker_id: int
    
class SessionResponse(SessionBase):
    id: int
    description: str
    duration: int
    speaker_id: int
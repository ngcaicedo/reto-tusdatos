from pydantic import BaseModel

class SpeakerBase(BaseModel):
    name: str
    
class SpeakerCreate(SpeakerBase):
    pass

class SpeakerUpdate(SpeakerBase):
    pass

class SpeakerResponse(SpeakerBase):
    id: int
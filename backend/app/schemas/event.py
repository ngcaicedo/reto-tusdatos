from pydantic import BaseModel, EmailStr, ConfigDict, Field
from app.models.event import StateEnum
from datetime import datetime
from app.schemas.session import SessionResponse


class EventCreate(BaseModel):
    name: str
    description: str
    capacity: int
    state: StateEnum
    date_start: datetime
    date_end: datetime
    location: str
    user_created_id: int
    session_ids: list[int] = Field(min_length=1)


class EventUpdate(BaseModel):
    name: str
    description: str
    capacity: int
    state: StateEnum
    date_start: datetime
    date_end: datetime
    location: str
    session_ids: list[int] = Field(min_length=1)


class EventResponse(BaseModel):
    id: int
    name: str
    description: str
    capacity: int
    state: StateEnum
    date_start: datetime
    date_end: datetime
    location: str
    user_created_id: int
    sessions: list[SessionResponse] = []  # <-- Aquí incluyes las sesiones asociadas
    is_registered: bool = False

    model_config = ConfigDict(from_attributes=True)

from pydantic import BaseModel, EmailStr, ConfigDict
from app.models.event import StateEnum
from datetime import datetime


class EventCreate(BaseModel):
    name: str
    description: str
    capacity: int
    state: StateEnum
    date_start: datetime
    date_end: datetime
    location: str
    user_created_id: int


class EventUpdate(BaseModel):
    name: str
    description: str
    capacity: int
    state: StateEnum
    date_start: datetime
    date_end: datetime
    location: str


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

    model_config = ConfigDict(from_attributes=True)

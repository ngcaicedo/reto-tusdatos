from pydantic import BaseModel, ConfigDict, EmailStr
from app.models.user import RoleEnum


class AssistantCreate(BaseModel):
    name: str
    email: EmailStr
    password: str
    phone: str
    role: RoleEnum = RoleEnum.ASISTENTE


class AssistantUpdate(BaseModel):
    name: str
    phone: str


class AssistantResponse(BaseModel):
    id: int
    name: str
    email: str
    phone: str
    user_id: int

    model_config = ConfigDict(from_attributes=True)

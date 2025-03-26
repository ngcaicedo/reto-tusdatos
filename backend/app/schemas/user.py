from pydantic import BaseModel, EmailStr, ConfigDict
from app.models.user import RoleEnum


class UserLogin(BaseModel):
    username: EmailStr
    password: str


class Token(BaseModel):
    user_id: int
    access_token: str
    token_type: str = "bearer"
    user: str
    role: RoleEnum


class UserCreate(BaseModel):
    name: str
    phone: str
    email: EmailStr
    password: str
    role: RoleEnum


class UserResponse(BaseModel):
    id: int
    name: str
    phone: str
    email: EmailStr
    role: RoleEnum

    model_config = ConfigDict(from_attributes=True)

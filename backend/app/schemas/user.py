from pydantic import BaseModel, EmailStr

class UserLogin(BaseModel):
    username: EmailStr
    password: str
    
class Token(BaseModel):
    token: str
    token_type: str = "bearer"
    user: str
    role: str
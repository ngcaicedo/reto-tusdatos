from app.db.base import BaseModel
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class Assistant(BaseModel):
    __tablename__ = "assistants"

    email = Column(String, index=True, nullable=False)
    phone = Column(String, index=True, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False, unique=True)
    
    user = relationship("User", back_populates="assistant")
    events = relationship("Event", secondary="event_assistant", back_populates="assistants")

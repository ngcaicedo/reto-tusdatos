from app.db.base import BaseModel
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class Speaker(BaseModel):
    __tablename__ = "speakers"

    sessions = relationship("Session", back_populates="speaker")


class Session(BaseModel):
    __tablename__ = "sessions"

    description = Column(String, index=True, nullable=False)
    duration = Column(Integer, index=True, nullable=False)
    event_id = Column(Integer, ForeignKey("events.id"), nullable=False)
    speaker_id = Column(Integer, ForeignKey("speakers.id"), nullable=False)

    event = relationship("Event", back_populates="sessions")
    speaker = relationship("Speaker", back_populates="sessions")

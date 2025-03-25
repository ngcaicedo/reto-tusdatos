from sqlalchemy import Table, Column, Integer, ForeignKey
from app.db.base import Base
from sqlalchemy.orm import relationship

class EventAssistant(Base):
    __tablename__ = 'event_assistant'

    event_id = Column(Integer, ForeignKey('events.id'), primary_key=True)
    assistant_id = Column(Integer, ForeignKey('assistants.id'), primary_key=True)

    event = relationship("Event", backref="event_assistants")
    assistant = relationship("Assistant", backref="event_assistants")
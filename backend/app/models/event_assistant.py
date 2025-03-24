from sqlalchemy import Table, Column, Integer, ForeignKey
from app.db.base import BaseModel

event_assistant = Table(
    'event_assistant',
    BaseModel.metadata,
    Column('event_id', Integer, ForeignKey('events.id'), primary_key=True),
    Column('assistant_id', Integer, ForeignKey('assistants.id'), primary_key=True)
)
from sqlalchemy import inspect
from app.models.event import Event, StateEnum
from app.models.assistant import Assistant
from app.models.user import User, RoleEnum
import faker


def test_table_event_assistant(db):
    """ Test para verificar que el modelo Event se haya creado correctamente """
    inspector = inspect(db.bind)
    table_names = inspector.get_table_names()
    assert "event_assistant" in table_names


def test_event_has_assistant(db, user_factory, event_factory, assistant_factory):
    """ Test para verificar que el modelo Event tiene una relación con el modelo Assistant """
    user = user_factory()
    event = event_factory(user=user)
    assistant = assistant_factory(user=user)

    event.assistants.append(assistant)
    db.commit()
    db.refresh(event)

    assert assistant in event.assistants
    assert event in assistant.events

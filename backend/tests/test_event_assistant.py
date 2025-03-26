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


def test_event_has_assistant(db, client, user_factory, event_factory, assistant_factory):
    """ Test para verificar que el modelo Event tiene una relación con el modelo Assistant """
    user = user_factory.create_user()
    event = event_factory.create_event(user_id=user.id, state=StateEnum.CREADO)
    assistant = assistant_factory(client)
    assistant = db.query(Assistant).filter_by(user_id=assistant['user_id']).first()

    event.assistants.append(assistant)
    db.commit()
    db.refresh(event)

    assert assistant in event.assistants
    assert event in assistant.events

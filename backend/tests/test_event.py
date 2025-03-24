from sqlalchemy import inspect
from app.models.event import Event, StateEnum
from app.models.session import Session, Speaker
from app.models.user import User, RoleEnum
import faker


def test_model_event(db):
    """ Test para verificar que el modelo Event se haya creado correctamente """
    inspector = inspect(db.bind)
    table_names = inspector.get_table_names()
    assert "events" in table_names


def test_event_has_session(db, user_factory, event_factory, speaker_factory, session_factory):
    """ Test para verificar que el modelo Event tiene una relación con el modelo Session """
    user = user_factory()
    event = event_factory(user=user)
    speaker = speaker_factory()
    session = session_factory(event=event, speaker=speaker)
    
    assert event.sessions[0].id == session.id
    assert session.event.id == event.id


def test_event_created_by_user(db, user_factory, event_factory):
    """ Test para verificar que el evento fue creado por un usuario """
    user = user_factory()
    event = event_factory(user=user)

    assert event.user_created_id == user.id
    assert user.events[0].id == event.id
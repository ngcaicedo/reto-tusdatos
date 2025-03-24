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


def test_event_has_session(db):
    """ Test para verificar que el modelo Event tiene una relación con el modelo Session """
    fake = faker.Faker()
    event = Event(
        name=fake.name(),
        description=fake.text(),
        capacity=100,
        state=StateEnum.CREADO,
        date_start=fake.date_time_this_year(),
        date_end=fake.date_time_this_year(),
        location=fake.address(),
    )
    db.add(event)
    db.commit()
    db.refresh(event)

    speaker = Speaker(
        name=fake.name(),
    )
    db.add(speaker)
    db.commit()
    db.refresh(speaker)

    session = Session(
        name=fake.name(),
        description=fake.text(),
        duration=1,
        speaker_id=speaker.id,
        event_id=event.id,
    )
    db.add(session)
    db.commit()
    db.refresh(session)

    assert event.sessions[0].id == session.id
    assert session.event.id == event.id


def test_event_created_by_user(db):
    """ Test para verificar que el evento fue creado por un usuario """
    fake = faker.Faker()
    user = User(
        name=fake.name(),
        phone=fake.phone_number(),
        email=fake.email(),
        role=RoleEnum.ORGANIZADOR,
        password="123456",
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    event = Event(
        name=fake.name(),
        description=fake.text(),
        capacity=100,
        state=StateEnum.CREADO,
        date_start=fake.date_time_this_year(),
        date_end=fake.date_time_this_year(),
        location=fake.address(),
        user_created_id=user.id,
    )

    db.add(event)
    db.commit()
    db.refresh(event)

    assert event.user_created_id == user.id
    assert user.events[0].id == event.id
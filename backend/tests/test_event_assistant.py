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


def test_event_has_assistant(db):
    """ Test para verificar que el modelo Event tiene una relación con el modelo Assistant """
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

    user = User(
        name=fake.name(),
        phone=fake.phone_number(),
        email=fake.email(),
        role=RoleEnum.ASISTENTE,
        password="123456",
    )
    db.add(user)
    db.commit()
    db.refresh(user)

    assistant = Assistant(
        name=fake.name(),
        email=fake.email(),
        phone=fake.phone_number(),
        user_id=user.id,
    )
    db.add(assistant)
    db.commit()
    db.refresh(assistant)

    event.assistants.append(assistant)
    db.commit()
    db.refresh(event)

    assert assistant in event.assistants
    assert event in assistant.events

from sqlalchemy import inspect
from app.models.user import User, RoleEnum
from app.models.assistant import Assistant
import faker
import pytest


def test_model_user(db):
    """ Test para verificar que el modelo User se haya creado correctamente """
    inspector = inspect(db.bind)
    table_names = inspector.get_table_names()
    assert "users" in table_names


def test_user_has_not_assistant(db):
    fake = faker.Faker()
    user = User(
        name=fake.name(),
        phone=fake.phone_number(),
        email=fake.email(),
        role=RoleEnum.ADMIN,
        password="123456",
    )
    db.add(user)
    db.commit()
    db.refresh(user)

    assert user.assistant is None
    
def test_assistant_has_user(db):
    fake = faker.Faker()
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
    
    assert assistant.user_id is not None
    assert user.assistant.id == assistant.id
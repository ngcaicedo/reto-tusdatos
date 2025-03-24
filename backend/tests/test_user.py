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


def test_user_has_not_assistant(db, user_factory):
    """ Test para verificar que el modelo User no tiene un asistente """
    user = user_factory(role=RoleEnum.ADMIN)
    assert user.assistant is None
    
def test_assistant_has_user(db, user_factory, assistant_factory):
    """ Test para verificar que el modelo Assistant tiene un usuario """
    user = user_factory(role=RoleEnum.ASISTENTE)
    assistant = assistant_factory(user=user)
    
    assert assistant.user_id is not None
    assert user.assistant.id == assistant.id
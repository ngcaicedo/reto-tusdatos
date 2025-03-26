import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool
from app.db.base import Base
import app.models as models
import faker
from fastapi.testclient import TestClient
from .factories.user_factory import UserFactory
from .factories.event_factory import EventFactory
from .factories.session_factory import SessionFactory

RoleEnum = models.user.RoleEnum
StateEnum = models.event.StateEnum
User = models.user.User
Event = models.event.Event
Session = models.session.Session
Speaker = models.session.Speaker
Assistant = models.assistant.Assistant
fake = faker.Faker()


@pytest.fixture
def auth_header():
    """ Fixture para obtener el encabezado de autenticación """
    def _auth_header(user: dict) -> dict:
        """ Función para obtener el encabezado de autenticación """
        return {'Authorization': f'Bearer {user["access_token"]}'}
    return _auth_header


@pytest.fixture
def assistant_payload():
    def _payload(**overrides):
        return {
            'name': overrides.get('name', fake.name()),
            'email': overrides.get('email', fake.email()),
            'password': overrides.get('password', fake.password()),
            'phone': overrides.get('phone', fake.phone_number()),
            'role': RoleEnum.ASISTENTE.value,
        }
    return _payload


@pytest.fixture
def user_factory(db):
    """ Fixture para crear un usuario en la base de datos """
    return UserFactory(db)


@pytest.fixture
def event_factory(db):
    """ Fixture para crear un evento en la base de datos """
    return EventFactory(db)


@pytest.fixture
def session_factory(db):
    """ Fixture para crear una sesión en la base de datos """
    return SessionFactory(db)


@pytest.fixture
def assistant_factory(db):
    """ Fixture para crear un asistente en la base de datos"""
    def create_assistant() -> Assistant:
        """ Función para crear un asistente en la base de datos """
        name = fake.name()
        email = fake.email()
        password = fake.password()
        phone = fake.phone_number()
        role = RoleEnum.ASISTENTE
        user = User(
            name=name,
            email=email,
            password=password,
            phone=phone,
            role=role,
        )

        db.add(user)
        db.commit()
        db.refresh(user)

        assistant = Assistant(
            name=name,
            email=email,
            phone=phone,
            user_id=user.id,
        )
        db.add(assistant)
        db.commit()
        db.refresh(assistant)
        return assistant
    return create_assistant


@pytest.fixture
def speaker_factory(db):
    """ Fixture para crear un speaker en la base de datos """
    def create_speaker() -> Speaker:
        """ Función para crear un speaker en la base de datos """
        speaker = Speaker(
            name=fake.name()
        )
        db.add(speaker)
        db.commit()
        db.refresh(speaker)
        return speaker
    return create_speaker


@pytest.fixture(scope="function")
def db():
    """ Fixture para crear una base de datos en memoria para pruebas """
    engine = create_engine(
        "sqlite:///:memory:",
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )
    TestingSessionLocal = sessionmaker(
        autocommit=False, autoflush=False, bind=engine)

    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


@pytest.fixture
def client(db):
    """ Fixture para crear un cliente de pruebas """
    from app.main import app
    from app.db.session import get_db

    def override_get_db():
        yield db

    app.dependency_overrides[get_db] = override_get_db
    return TestClient(app)

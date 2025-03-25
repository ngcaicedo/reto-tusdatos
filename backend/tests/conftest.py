import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool
from app.db.base import Base
import app.models as models
import faker
from fastapi.testclient import TestClient
from .factories.user_factory import UserFactory

RoleEnum = models.user.RoleEnum
StateEnum = models.event.StateEnum
User = models.user.User
Event = models.event.Event
Session = models.session.Session
Speaker = models.session.Speaker
Assistant = models.assistant.Assistant
fake = faker.Faker()


@pytest.fixture
def user_factory(db):
    """ Fixture para crear un usuario en la base de datos """
    return UserFactory(db)


@pytest.fixture
def event_factory(db):
    """ Fixture para crear un evento en la base de datos """
    def create_event(user: User, state: StateEnum = StateEnum.CREADO) -> Event:
        """ Función para crear un evento en la base de datos """
        event = Event(
            name=fake.name(),
            description=fake.text(),
            capacity=100,
            state=state,
            date_start=fake.date_time_this_year(),
            date_end=fake.date_time_this_year(),
            location=fake.address(),
            user_created_id=user.id,
        )
        db.add(event)
        db.commit()
        db.refresh(event)
        return event
    return create_event


@pytest.fixture
def session_factory(db):
    """ Fixture para crear una sesión en la base de datos """
    def create_session(event: Event, speaker: Speaker) -> Session:
        """ Función para crear una sesión en la base de datos """
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
        return session
    return create_session


@pytest.fixture
def assistant_factory(db):
    """ Fixture para crear un asistente en la base de datos"""
    def create_assistant(user: User) -> Assistant:
        """ Función para crear un asistente en la base de datos """
        assistant = Assistant(
            name=fake.name(),
            email=fake.email(),
            phone=fake.phone_number(),
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

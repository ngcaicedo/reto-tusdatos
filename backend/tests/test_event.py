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
    user = user_factory.create_user()
    event = event_factory(user=user)
    speaker = speaker_factory()
    session = session_factory(event=event, speaker=speaker)

    assert event.sessions[0].id == session.id
    assert session.event.id == event.id


def test_event_created_by_user(db, user_factory, event_factory):
    """ Test para verificar que el evento fue creado por un usuario """
    user = user_factory.create_user()
    event = event_factory(user=user)

    assert event.user_created_id == user.id
    assert user.events[0].id == event.id


def test_create_event_without_auth(client, user_factory):
    user = user_factory.create_user()
    """ Test para verificar la creación de un evento sin autenticación """
    data = {
        'name': faker.Faker().name(),
        'description': faker.Faker().sentence(),
        'state': StateEnum.CREADO.value,
        'user_created_id': user.id
    }

    headers = {
        'Authorization': f'Bearer '}

    response = client.post('/events/create', json=data, headers=headers)
    assert response.status_code == 401
    response_data = response.json()
    assert response_data['detail'] == 'Not authenticated'


def test_create_event(client, user_factory):
    """ Test para verificar la creación de un evento """
    role = [RoleEnum.ADMIN, RoleEnum.ORGANIZADOR]
    user_logged = user_factory.login_user(role=faker.Faker().random_element(elements=role))
    data = {
        'name': faker.Faker().name(),
        'description': faker.Faker().sentence(),
        'state': StateEnum.CREADO.value,
        'user_created_id': user_logged['id']
    }

    headers = {
        'Authorization': f'Bearer {user_logged['token']}'
    }

    response = client.post('/events/create', json=data, headers=headers)
    assert response.status_code == 201
    response_data = response.json()
    assert response_data['name'] == data['name']
    assert response_data['description'] == data['description']
    assert response_data['state'] == data['state']
    assert response_data['user_created_id'] == data['user_created_id']


def test_create_event_without_data(client, user_factory):
    """ Test para verificar la creación de un evento sin"""
    role = [RoleEnum.ADMIN, RoleEnum.ORGANIZADOR]
    user_logged = user_factory.login_user(role=faker.Faker().random_element(elements=role))
    data = {
        'name': '',
        'description': '',
        'state': '',
        'user_created_id': ''
    }

    headers = {
        'Authorization': f'Bearer {user_logged['token']}'
    }

    response = client.post('/events/create', json=data, headers=headers)
    assert response.status_code == 422
    response_data = response.json()
    fields_required = ['name', 'description', 'state', 'user_created_id']
    for error in response_data['detail']:
        assert error['loc'][-1] in fields_required
        assert error['msg'] == 'Field required'

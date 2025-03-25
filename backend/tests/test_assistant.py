from sqlalchemy import inspect
from faker import Faker
from app.models.user import User

faker = Faker()


def test_model_assistant(db):
    """ Test para verificar que el modelo Assistant se haya creado correctamente """
    inspector = inspect(db.bind)
    table_names = inspector.get_table_names()
    assert "assistants" in table_names


def test_model_speaker(db):
    """ Test para verificar que el modelo Speaker se haya creado correctamente """
    inspector = inspect(db.bind)
    table_names = inspector.get_table_names()
    assert "speakers" in table_names


def test_create_assistant(db, client, user_factory):
    """ Test para verificar la creación de un asistente y su relación con un usuario """
    user = user_factory.create_user()
    data = {
        'name': faker.name(),
        'email': faker.email(),
        'password': faker.password(),
        'phone': faker.phone_number(),
        'user_id': user.id
    }

    headers = {
        'Authorization': f'Bearer {user.token}'
    }

    response = client.post('/assistants/create', json=data, headers=headers)
    assert response.status_code == 201
    response_data = response.json()
    user = db.get(User, response_data['user_id'])
    assert user is not None
    assert user.assistant.id == response_data['id']
    assert response_data['name'] == data['name']
    assert response_data['email'] == data['email']
    assert response_data['phone'] == data['phone']
    assert response_data['user_id'] == data['user_id']


def test_create_assistant_without_auth(client, user_factory):
    """ Test para verificar la creación de un asistente sin autenticación """
    user = user_factory.create_user()
    data = {
        'name': faker.name(),
        'email': faker.email(),
        'password': faker.password(),
        'phone': faker.phone_number(),
        'user_id': user.id
    }

    headers = {
        'Authorization': f'Bearer '
    }

    response = client.post('/assistants/create', json=data, headers=headers)
    assert response.status_code == 401
    response_data = response.json()
    assert response_data['detail'] == 'No autorizado'
    
    
def test_create_assistant_duplicate(client, user_factory, assistant_factory):
    """ Test para verificar la creación de un asistente duplicado """
    user = user_factory.create_user()
    assistant = assistant_factory()
    data = {
        'name': assistant.name,
        'email': assistant.email,
        'phone': assistant.phone
    }

    headers = {
        'Authorization': f'Bearer {user.token}'
    }

    response = client.post('/assistants/create', json=data, headers=headers)
    assert response.status_code == 400
    response_data = response.json()
    assert response_data['detail'] == 'El asistente ya existe'
    
def test_update_assistant(client, user_factory, assistant_factory):
    """ Test para verificar la actualización de un asistente """
    user = user_factory.create_user()
    assistant = assistant_factory()
    data = {
        'name': faker.name(),
        'email': faker.email(),
        'phone': faker.phone_number()
    }

    headers = {
        'Authorization': f'Bearer {user.token}'
    }

    response = client.put(f'/assistants/update/{assistant.id}', json=data, headers=headers)
    assert response.status_code == 200
    response_data = response.json()
    assert response_data['name'] == data['name']
    assert response_data['email'] == data['email']
    assert response_data['phone'] == data['phone']
    assert response_data['user_id'] == user.id
    
def test_update_assistant_duplicate(client, user_factory, assistant_factory):
    """ Test para verificar la actualización de un asistente duplicado """
    user = user_factory.create_user()
    assistant = assistant_factory()
    data = {
        'name': assistant.name,
        'email': assistant.email,
        'phone': assistant.phone
    }

    headers = {
        'Authorization': f'Bearer {user.token}'
    }

    response = client.put(f'/assistants/update/{assistant.id}', json=data, headers=headers)
    assert response.status_code == 400
    response_data = response.json()
    assert response_data['detail'] == 'El asistente ya existe'
    
def test_get_assistants(client, user_factory, assistant_factory):
    """ Test para verificar la obtención de asistentes """
    user = user_factory.create_user()
    assistant = assistant_factory()
    headers = {
        'Authorization': f'Bearer {user.token}'
    }

    response = client.get('/assistants/assistants', headers=headers)
    assert response.status_code == 200
    response_data = response.json()
    assert len(response_data) > 0
    assert response_data[0]['name'] == assistant.name
    assert response_data[0]['email'] == assistant.email
    assert response_data[0]['phone'] == assistant.phone
    assert response_data[0]['user_id'] == user.id
    
def test_get_assistant(client, db, assistant_factory):
    """ Test para verificar la obtención de un asistente """
    assistant = assistant_factory()
    user = db.get(User, assistant.user_id)
    headers = {
        'Authorization': f'Bearer {user.token}'
    }

    response = client.get(f'/assistants/{assistant.id}', headers=headers)
    assert response.status_code == 200
    response_data = response.json()
    assert response_data['name'] == assistant.name
    assert response_data['email'] == assistant.email
    assert response_data['phone'] == assistant.phone
    assert response_data['user_id'] == user.id
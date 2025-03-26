from sqlalchemy import inspect
from faker import Faker
from app.models.user import User, RoleEnum
from app.models.assistant import Assistant

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


def test_create_assistant(db, client, user_factory, auth_header, assistant_payload):
    """ Test para verificar la creación de un asistente y su relación con un usuario """
    user = user_factory.login_user(RoleEnum.ORGANIZADOR)
    headers = auth_header(user)
    data = assistant_payload()

    response = client.post('/assistants/create', json=data, headers=headers)
    assert response.status_code == 201

    response_data = response.json()
    user = db.get(User, response_data['user_id'])
    assert user is not None
    assert user.assistant.id == response_data['id']
    assert response_data['name'] == data['name']
    assert response_data['email'] == data['email']
    assert response_data['phone'] == data['phone']


def test_create_assistant_without_auth(client, user_factory, assistant_payload):
    """ Test para verificar la creación de un asistente sin autenticación """
    user = user_factory.login_user(RoleEnum.ORGANIZADOR)
    data = assistant_payload()

    response = client.post('/assistants/create', json=data)
    assert response.status_code == 401
    response_data = response.json()
    assert response_data['detail'] == 'Not authenticated'


def test_create_assistant_duplicate(client, user_factory, assistant_factory, auth_header, assistant_payload):
    """ Test para verificar la creación de un asistente duplicado """
    user = user_factory.login_user(RoleEnum.ORGANIZADOR)
    headers = auth_header(user)
    data = assistant_payload()

    response = client.post('/assistants/create', json=data, headers=headers)
    response = client.post('/assistants/create', json=data, headers=headers)

    assert response.status_code == 400
    response_data = response.json()
    assert response_data['detail'] == 'El asistente ya se encuentra registrado'


def test_update_assistant(db, client, user_factory, assistant_factory, auth_header, assistant_payload):
    """ Test para verificar la actualización de un asistente """
    user = user_factory.login_user(RoleEnum.ORGANIZADOR)
    headers = auth_header(user)
    data = assistant_payload()
    assistant = assistant_factory(client)
    assistant_id = db.query(Assistant).filter_by(user_id=assistant['user_id']).first().id

    response = client.put(
        f'/assistants/update/{assistant_id}', json=data, headers=headers)
    assert response.status_code == 200
    response_data = response.json()
    assert response_data['name'] == data['name']
    assert response_data['email'] != data['email']
    assert response_data['phone'] == data['phone']


def test_update_assistant_duplicate(db, client, user_factory, assistant_factory, auth_header):
    """Test para verificar que no se puede actualizar un asistente con datos duplicados de otro existente"""

    # Crea un usuario organizador autenticado
    user = user_factory.login_user(RoleEnum.ORGANIZADOR)
    headers = auth_header(user)
    assistant1 = assistant_factory(client)
    assistant1 = db.query(Assistant).filter_by(user_id=assistant1['user_id']).first()
    assistant2 = assistant_factory(client)
    assistant2 = db.query(Assistant).filter_by(user_id=assistant2['user_id']).first()

    data_duplicate = {
        'name': assistant1.name,
        'email': assistant1.email,
        'password': faker.password(),
        'phone': assistant1.phone,
    }

    response = client.put(
        f'/assistants/update/{assistant2.id}',
        json=data_duplicate,
        headers=headers
    )

    assert response.status_code == 400
    assert response.json()[
        'detail'] == 'El asistente ya se encuentra registrado'


def test_get_assistants(db, client, user_factory, assistant_factory, auth_header):
    """ Test para verificar la obtención de asistentes """
    user = user_factory.login_user(RoleEnum.ORGANIZADOR)
    headers = auth_header(user)
    assistant = assistant_factory(client)
    assistant = db.query(Assistant).filter_by(user_id=assistant['user_id']).first()

    response = client.get('/assistants/assistants', headers=headers)
    assert response.status_code == 200
    
    response_data = response.json()
    assert len(response_data) > 0
    assert any(a['id'] == assistant.id for a in response_data)


def test_get_assistant(client, db, assistant_factory, user_factory, auth_header):
    """ Test para verificar la obtención de un asistente """
    assistant = assistant_factory(client)
    assistant = db.query(Assistant).filter_by(user_id=assistant['user_id']).first()
    user = user_factory.login_user(RoleEnum.ORGANIZADOR)
    headers = auth_header(user)

    response = client.get(f'/assistants/{assistant.id}', headers=headers)
    assert response.status_code == 200
    
    response_data = response.json()
    assert response_data['id'] == assistant.id

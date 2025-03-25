from sqlalchemy import inspect
from app.models.user import RoleEnum
from faker import Faker

faker = Faker()


def test_model_session(db):
    """ Test para verificar que el modelo Session se haya creado correctamente """
    inspector = inspect(db.bind)
    table_names = inspector.get_table_names()
    assert "sessions" in table_names

def test_model_speaker(db):
    """ Test para verificar que el modelo Speaker se haya creado correctamente """
    inspector = inspect(db.bind)
    table_names = inspector.get_table_names()
    assert "speakers" in table_names
    
def test_create_speaker(client, auth_header, user_factory):
    """ Función para crear un speaker """
    user_login = user_factory.login_user(role=RoleEnum.ORGANIZADOR)
    data = {
        "name": faker.name(),
    }
    headers = auth_header(user_login)
    response = client.post("sessions/create/speaker/", json=data, headers=headers)
    assert response.status_code == 201
    data_response = response.json()
    assert data_response.get("id") is not None
    assert data_response.get("name") == data["name"]

def test_create_duplicated_speaker(client, auth_header, user_factory):
    """ Función para crear un speaker duplicado """
    user_login = user_factory.login_user(role=RoleEnum.ORGANIZADOR)
    data = {
        "name": faker.name(),
    }
    headers = auth_header(user_login)
    response = client.post("sessions/create/speaker/", json=data, headers=headers)
    response = client.post("sessions/create/speaker/", json=data, headers=headers)
    assert response.status_code == 409
    data_response = response.json()
    assert data_response.get("detail") == "El speaker ya se encuentra registrado"
    
def test_update_speaker(client, auth_header, user_factory):
    """ Función para actualizar un speaker """
    user_login = user_factory.login_user(role=RoleEnum.ORGANIZADOR)
    data = {
        "name": faker.name(),
    }
    headers = auth_header(user_login)
    response = client.post("sessions/create/speaker/", json=data, headers=headers)
    speaker = response.json()
    data2 = {
        "name": faker.name(),
    }
    response = client.put(f"sessions/update/speaker/{speaker.get('id')}", json=data2, headers=headers)
    assert response.status_code == 200
    data_response = response.json()
    assert data_response.get("id") == speaker.get("id")
    assert data_response.get("name") == data2["name"]
    
def test_update_speaker_not_found(client, auth_header, user_factory):
    """ Función para actualizar un speaker no encontrado """
    user_login = user_factory.login_user(role=RoleEnum.ORGANIZADOR)
    data = {
        "name": faker.name(),
    }
    headers = auth_header(user_login)
    response = client.put(f"sessions/update/speaker/1000", json=data, headers=headers)
    assert response.status_code == 404
    data_response = response.json()
    assert data_response.get("detail") == "El speaker no se encuentra registrado"
    
def test_get_speakers(client, auth_header, user_factory):
    """ Función para obtener todos los speakers """
    user_login = user_factory.login_user(role=RoleEnum.ORGANIZADOR)
    data = {
        "name": faker.name(),
    }
    headers = auth_header(user_login)
    
    response = client.post("sessions/create/speaker/", json=data, headers=headers)
    assert response.status_code == 201
    
    response = client.get("sessions/speakers/", headers=headers)
    assert response.status_code == 200
    data_response = response.json()
    assert isinstance(data_response, list)
    assert len(data_response) > 0
    assert data_response[0].get("id") is not None
    
def test_get_speaker(client, auth_header, user_factory):
    """ Función para obtener un speaker """
    user_login = user_factory.login_user(role=RoleEnum.ORGANIZADOR)
    headers = auth_header(user_login)
    data = {
        "name": faker.name(),
    }
    headers = auth_header(user_login)
    response = client.post("sessions/create/speaker/", json=data, headers=headers)
    speaker = response.json()
    response = client.get(f"sessions/speaker/{speaker.get('id')}", headers=headers)
    assert response.status_code == 200
    data_response = response.json()
    assert data_response.get("id") == speaker.get("id")
    assert data_response.get("name") == speaker.get("name")
    
def test_create_session(client, auth_header, user_factory):
    """ Función para crear una sesión """
    user_login = user_factory.login_user(role=RoleEnum.ORGANIZADOR)
    data_speaker = {
        "name": faker.name(),
    }
    headers = auth_header(user_login)
    response = client.post("sessions/create/speaker/", json=data_speaker, headers=headers)
    speaker = response.json()
    data = {
        "name": faker.name(),
        "description": faker.text(),
        "duration": faker.random_int(min=1, max=60),
        "speaker_id": speaker.get("id"),
    }
    response = client.post("sessions/create/", json=data, headers=headers)
    assert response.status_code == 201
    data_response = response.json()
    assert data_response.get("id") is not None
    assert data_response.get("name") == data["name"]
    assert data_response.get("description") == data["description"]
    assert data_response.get("duration") == data["duration"]
    assert data_response.get("speaker_id") == speaker.get("id")
    
    
def test_create_session_duplicate(client, auth_header, user_factory):
    """ Función para crear una sesión duplicada """
    user_login = user_factory.login_user(role=RoleEnum.ORGANIZADOR)
    data_speaker = {
        "name": faker.name(),
    }
    headers = auth_header(user_login)
    response = client.post("sessions/create/speaker/", json=data_speaker, headers=headers)
    speaker = response.json()
    data = {
        "name": faker.name(),
        "description": faker.text(),
        "duration": faker.random_int(min=1, max=60),
        "speaker_id": speaker.get("id"),
    }
    response = client.post("sessions/create/", json=data, headers=headers)
    response = client.post("sessions/create/", json=data, headers=headers)
    assert response.status_code == 409
    data_response = response.json()
    assert data_response.get("detail") == "La sesión ya se encuentra registrada"
    
def test_update_session(client, auth_header, user_factory):
    """ Función para actualizar una sesión """
    user_login = user_factory.login_user(role=RoleEnum.ORGANIZADOR)
    data_speaker = {
        "name": faker.name(),
    }
    headers = auth_header(user_login)
    response = client.post("sessions/create/speaker/", json=data_speaker, headers=headers)
    speaker = response.json()
    data = {
        "name": faker.name(),
        "description": faker.text(),
        "duration": faker.random_int(min=1, max=60),
        "speaker_id": speaker.get("id"),
    }
    response = client.post("sessions/create/", json=data, headers=headers)
    session = response.json()
    data2 = {
        "name": faker.name(),
        "description": faker.text(),
        "duration": faker.random_int(min=1, max=60),
        "speaker_id": speaker.get("id"),
    }
    response = client.put(f"sessions/update/{session.get('id')}", json=data2, headers=headers)
    assert response.status_code == 200
    data_response = response.json()
    assert data_response.get("id") == session.get("id")
    assert data_response.get("name") == data2["name"]
    assert data_response.get("description") == data2["description"]
    assert data_response.get("duration") == data2["duration"]
    assert data_response.get("speaker_id") == speaker.get("id")
    
def test_update_session_not_found(client, auth_header, user_factory):
    """ Función para actualizar una sesión no encontrada """
    user_login = user_factory.login_user(role=RoleEnum.ORGANIZADOR)
    data_speaker = {
        "name": faker.name(),
    }
    headers = auth_header(user_login)
    response = client.post("sessions/create/speaker/", json=data_speaker, headers=headers)
    speaker = response.json()
    data = {
        "name": faker.name(),
        "description": faker.text(),
        "duration": faker.random_int(min=1, max=60),
        "speaker_id": speaker.get("id"),
    }
    response = client.put(f"sessions/update/1000", json=data, headers=headers)
    assert response.status_code == 404
    data_response = response.json()
    assert data_response.get("detail") == "La sesión no se encuentra registrada"
    
    
def test_get_sessions(client, auth_header, user_factory):
    """ Función para obtener todas las sesiones """
    user_login = user_factory.login_user(role=RoleEnum.ORGANIZADOR)
    data_speaker = {
        "name": faker.name(),
    }
    headers = auth_header(user_login)
    response = client.post("sessions/create/speaker/", json=data_speaker, headers=headers)
    speaker = response.json()
    data = {
        "name": faker.name(),
        "description": faker.text(),
        "duration": faker.random_int(min=1, max=60),
        "speaker_id": speaker.get("id"),
    }
    response = client.post("sessions/create/", json=data, headers=headers)
    assert response.status_code == 201
    
    response = client.get("sessions/", headers=headers)
    assert response.status_code == 200
    data_response = response.json()
    assert isinstance(data_response, list)
    assert len(data_response) > 0
    assert data_response[0].get("id") is not None
    
def test_get_session(client, auth_header, user_factory):
    """ Función para obtener una sesión """
    user_login = user_factory.login_user(role=RoleEnum.ORGANIZADOR)
    data_speaker = {
        "name": faker.name(),
    }
    headers = auth_header(user_login)
    response = client.post("sessions/create/speaker/", json=data_speaker, headers=headers)
    speaker = response.json()
    data = {
        "name": faker.name(),
        "description": faker.text(),
        "duration": faker.random_int(min=1, max=60),
        "speaker_id": speaker.get("id"),
    }
    response = client.post("sessions/create/", json=data, headers=headers)
    session = response.json()
    response = client.get(f"sessions/{session.get('id')}", headers=headers)
    assert response.status_code == 200
    data_response = response.json()
    assert data_response.get("id") == session.get("id")
    assert data_response.get("name") == session.get("name")
    assert data_response.get("description") == session.get("description")
    assert data_response.get("duration") == session.get("duration")
    assert data_response.get("speaker_id") == speaker.get("id")
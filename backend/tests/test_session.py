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
    response = client.post("create/speaker/", json=data, headers=headers)
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
    response = client.post("create/speaker/", json=data, headers=headers)
    response = client.post("create/speaker/", json=data, headers=headers)
    assert response.status_code == 409
    data_response = response.json()
    assert data_response.get("detail") == "El speaker ya se encuentra registrado"
    
def test_update_speaker(client, auth_header, user_factory):
    """ Función para actualizar un speaker """
    user_login = user_factory.login_user(role=RoleEnum.ORGANIZADOR)
    speaker = user_factory.create_speaker()
    data = {
        "name": faker.name(),
    }
    headers = auth_header(user_login)
    response = client.put(f"update/speaker/{speaker.id}", json=data, headers=headers)
    assert response.status_code == 200
    data_response = response.json()
    assert data_response.get("id") == speaker.id
    assert data_response.get("name") == data["name"]
    
def test_update_speaker_not_found(client, auth_header, user_factory):
    """ Función para actualizar un speaker no encontrado """
    user_login = user_factory.login_user(role=RoleEnum.ORGANIZADOR)
    data = {
        "name": faker.name(),
    }
    headers = auth_header(user_login)
    response = client.put(f"update/speaker/1000", json=data, headers=headers)
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
    
    response = client.post("create/speaker/", json=data, headers=headers)
    assert response.status_code == 201
    
    response = client.get("speakers/", headers=headers)
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
    response = client.post("create/speaker/", json=data, headers=headers)
    speaker = response.json()
    response = client.get(f"speaker/{speaker.get('id')}", headers=headers)
    assert response.status_code == 200
    data_response = response.json()
    assert data_response.get("id") == speaker.get("id")
    assert data_response.get("name") == speaker.get("name")
from app.core.authenticator.security import hash_password, verify_password
from app.core.authenticator.jwt_utils import create_access_token, decode_access_token
from app.core.authenticator.auth import authenticate_user
from datetime import timedelta
from app.schemas.user import UserLogin
from faker import Faker
from app.models.user import User, RoleEnum
from app.models.event import StateEnum

faker = Faker()


def test_hash_password():
    """ Test para verificar que la contraseña se encripta correctamente """
    password = "password"
    hashed_password = hash_password(password)
    assert verify_password(hashed_password, password)


def test_create_access_token(user_factory):
    """ Test para verificar que se crea un token de acceso """
    user = user_factory.create_user()
    data = {
        "sub": user.email
    }

    token = create_access_token(data=data)
    assert token is not None
    assert isinstance(token, str)


def test_decode_access_token(user_factory):
    """ Test para verificar que se decodifica un token de acceso """
    user = user_factory.create_user()
    data = {
        "sub": user.email
    }
    token = create_access_token(data=data)

    decoded_token = decode_access_token(token)
    assert isinstance(decoded_token, dict)
    assert decoded_token.get("sub") == user.email


def test_decode_access_token_expired(user_factory):
    """ Test para verificar que se decodifica un token de acceso expirado """
    user = user_factory.create_user()
    data = {
        "sub": user.email
    }
    token = create_access_token(data=data, expires_delta=timedelta(seconds=-1))

    decoded_token = decode_access_token(token)
    assert decoded_token == {}


def test_authenticate_user(db, user_factory):
    """ Test para verificar que se autentica un usuario """
    user = user_factory.create_user(password="password")
    user_login = UserLogin(username=user.email, password="password")
    user_auth = authenticate_user(db, user_login)

    assert user_auth is not None
    assert user_auth.email == user.email
    assert user_auth.role == user.role


def test_login_success(client, user_factory):
    """ Test para verificar que un usuario inicia sesión correctamente """
    user = user_factory.create_user(password="password")
    data = {
        "username": user.email,
        "password": "password"
    }
    response = client.post("/auth/login", data=data)

    assert response.status_code == 200
    data_response = response.json()
    assert data_response.get("token") is not None
    assert data_response.get("user") == user.name
    assert data_response.get("role") == user.role.value
    assert data_response.get("token_type") == "bearer"
    assert data_response.get("user_id") == user.id


def test_login_fail(client, user_factory):
    """ Test para verificar que un usuario no inicia sesión con credenciales incorrectas """
    user = user_factory.create_user(password="password")
    data = {
        "username": user.email,
        "password": "password123"
    }
    response = client.post("/auth/login", data=data)

    assert response.status_code == 401
    data_response = response.json()
    assert data_response.get("detail") == "Credenciales incorrectas"


def test_register_user_with_assistant_role(client, db):
    """ Test para verificar que un usuario se registra con el rol de asistente """
    data = {
        "name": faker.name(),
        "email": faker.email(),
        "password": faker.password(),
        "phone": faker.phone_number(),
        "role": "ASISTENTE"
    }

    response = client.post("/users/register/assistant", json=data)
    assert response.status_code == 201
    user_data = response.json()

    user = db.get(User, user_data["id"])
    assert user.role == RoleEnum.ASISTENTE
    assert user.assistant is not None
    assert user.assistant.email == user.email


def test_register_duplicate_user_assistant(client, user_factory, assistant_payload):
    """ Test para verificar el registro de un usuario duplicado con el rol de asistente """
    data = assistant_payload()

    response = client.post("/users/register/assistant", json=data)
    response = client.post("/users/register/assistant", json=data)
    assert response.status_code == 400
    data_response = response.json()
    assert data_response.get(
        "detail") == "El usuario ya se encuentra registrado"


def test_register_user_with_invalid_role(client):
    """ Test para verificar el registro de un usuario con un rol inválido """
    data = {
        "name": faker.name(),
        "email": faker.email(),
        "password": faker.password(),
        "phone": faker.phone_number(),
        "role": "ORGANIZADOR"
    }

    response = client.post("/users/register/assistant", json=data)
    assert response.status_code == 400
    data_response = response.json()
    assert data_response.get(
        "detail") == "Solo los usuarios con rol ASISTENTE pueden registrarse como asistentes."
    
    
def test_register_assistant_to_event(client, db, user_factory, event_factory, assistant_payload):
    """ Test para verificar el registro de un asistente a un evento """
    data = assistant_payload()
    response = client.post("/users/register/assistant", json=data)
    assert response.status_code == 201

    response_login = client.post("/auth/login", data={
        "username": data["email"],
        "password": data["password"]
    })
    token = response_login.json()["token"]
    headers = {"Authorization": f"Bearer {token}"}

    organizador = user_factory.create_user(role=RoleEnum.ORGANIZADOR)
    event = event_factory.create_event(user_id=organizador.id, state=StateEnum.CREADO)

    response = client.post(f"/events/register/{event.id}", headers=headers)
    assert response.status_code == 201

    response_data = response.json()
    assert response_data["event_id"] == event.id
    assert response_data["message"] == "Registro exitoso"


def test_register_assistant_again_to_event(client, db, user_factory, event_factory, assistant_payload):
    """ Test para verificar el registro de un asistente a un evento ya registrado """
    data = assistant_payload()
    response = client.post("/users/register/assistant", json=data)
    assert response.status_code == 201

    response_login = client.post("/auth/login", data={
        "username": data["email"],
        "password": data["password"]
    })
    token = response_login.json()["token"]
    headers = {"Authorization": f"Bearer {token}"}

    organizador = user_factory.create_user(role=RoleEnum.ORGANIZADOR)
    event = event_factory.create_event(user_id=organizador.id, state=StateEnum.CREADO)

    response = client.post(f"/events/register/{event.id}", headers=headers)
    assert response.status_code == 201

    response = client.post(f"/events/register/{event.id}", headers=headers)
    assert response.status_code == 400
    response_data = response.json()
    assert response_data["detail"] == "El asistente ya se encuentra registrado en el evento"
    
def test_register_with_full_capacity(client, db, user_factory, event_factory, assistant_payload):
    """ Test para verificar el registro de un asistente a un evento con capacidad llena """
    data = assistant_payload()
    response = client.post("/users/register/assistant", json=data)
    assert response.status_code == 201

    response_login = client.post("/auth/login", data={
        "username": data["email"],
        "password": data["password"]
    })
    token = response_login.json()["token"]
    headers = {"Authorization": f"Bearer {token}"}

    organizador = user_factory.create_user(role=RoleEnum.ORGANIZADOR)
    event = event_factory.create_event(user_id=organizador.id, state=StateEnum.CREADO, capacity=1)

    response = client.post(f"/events/register/{event.id}", headers=headers)
    assert response.status_code == 201

    response = client.post(f"/events/register/{event.id}", headers=headers)
    assert response.status_code == 400
    response_data = response.json()
    assert response_data["detail"] == "La capacidad del evento está llena"
    

def test_event_not_found(client, db, assistant_payload ):
    """ Test para verificar el registro de un asistente a un evento no encontrado """
    data = assistant_payload()
    response = client.post("/users/register/assistant", json=data)
    assert response.status_code == 201

    response_login = client.post("/auth/login", data={
        "username": data["email"],
        "password": data["password"]
    })
    token = response_login.json()["token"]
    headers = {"Authorization": f"Bearer {token}"}

    response = client.post("/events/register/100", headers=headers)
    assert response.status_code == 404
    response_data = response.json()
    assert response_data["detail"] == "Evento no encontrado"
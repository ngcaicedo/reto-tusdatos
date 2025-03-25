from app.core.authenticator.security import hash_password, verify_password
from app.core.authenticator.jwt_utils import create_access_token, decode_access_token
from app.core.authenticator.auth import authenticate_user
from datetime import timedelta
from app.schemas.user import UserLogin


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
    assert data_response.get("user") == user.email
    assert data_response.get("role") == user.role.value
    assert data_response.get("token_type") == "bearer"
    
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
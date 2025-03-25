from sqlalchemy import inspect
from app.models.user import RoleEnum
import faker


fake = faker.Faker()


def test_model_user(db):
    """ Test para verificar que el modelo User se haya creado correctamente """
    inspector = inspect(db.bind)
    table_names = inspector.get_table_names()
    assert "users" in table_names


def test_user_has_not_assistant(user_factory):
    """ Test para verificar que el modelo User no tiene un asistente """
    user = user_factory.create_user(role=RoleEnum.ADMIN)
    assert user.assistant is None


def test_assistant_has_user(user_factory, assistant_factory):
    """ Test para verificar que el modelo Assistant tiene un usuario """
    user = user_factory.create_user(role=RoleEnum.ASISTENTE)
    assistant = assistant_factory(user=user)

    assert assistant.user_id is not None
    assert user.assistant.id == assistant.id


def test_register_organization_user(client):
    """ Test para verificar el registro de un usuario de organización """
    data = {
        'name': fake.name(),
        'phone': fake.phone_number(),
        'email': fake.email(),
        'password': fake.password(),
        'role': 'ORGANIZADOR'
    }

    response = client.post('/users/register', json=data)
    assert response.status_code == 201
    response_data = response.json()
    assert response_data['name'] == data['name']
    assert response_data['phone'] == data['phone']
    assert response_data['email'] == data['email']
    assert response_data['role'] == data['role']


def test_register_duplicate_user(client, user_factory):
    """ Test para verificar el registro de un usuario duplicado """
    fake_password = fake.password()
    user = user_factory.create_user(password=fake_password)
    data = {
        'name': user.name,
        'phone': user.phone,
        'email': user.email,
        'password': fake_password,
        'role': user.role.value
    }

    response = client.post('/users/register', json=data)
    assert response.status_code == 400
    response_data = response.json()
    assert response_data['detail'] == 'El usuario ya se encuentra registrado'


def test_register_user_invalid_data(client):
    """ Test para verificar el registro de un usuario con datos inválidos """
    data = {
        'name': fake.name(),
        'phone': fake.phone_number(),
    }

    response = client.post('/users/register', json=data)
    assert response.status_code == 422
    response_data = response.json()
    missing_fields = {error["loc"][-1] for error in response_data["detail"] if error["msg"] == "Field required"}
    expected_missing = {"email", "password", "role"}
    assert missing_fields == expected_missing

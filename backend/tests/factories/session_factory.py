from faker import Faker
from app.models.session import Session, Speaker
from .user_factory import UserFactory
from app.models.user import RoleEnum

class SessionFactory:
    """ Clase para crear sesiones en la base de datos """
    def __init__(self, db):
        self.db = db
        self.fake = Faker()
        self.user_factory = UserFactory(db)
    
    def create_session(self, client, auth_header) -> Session:
        """ Función para crear una sesión en la base de datos """
        user_login = self.user_factory.login_user(role = RoleEnum.ORGANIZADOR)
        data_speaker = {
            'name': self.fake.name(),
        }
        
        headers = auth_header(user_login)
        response = client.post("sessions/create/speaker/", json=data_speaker, headers=headers)
        speaker = response.json()
    
        data_session = {
            'name': self.fake.name(),
            'description': self.fake.text(),
            'duration': self.fake.random_int(min=2, max=60),
            'speaker_id': speaker.get('id'),
        }
        
        response = client.post("sessions/create/", json=data_session, headers=headers)
        session = response.json()
        return session
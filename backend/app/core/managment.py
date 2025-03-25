from app.core.authenticator.auth import login_user
from app.core.user import create_user
from app.core.event import create_event

class Managment:
    """ Clase para gestionar las operaciones de la API """
    def __init__(self):
        pass

    def login(self, form_data, db):
        return login_user(form_data, db)
    
    def create_user(self, db, user_data):
        return create_user(db, user_data)
    
    def create_event(self, db, event_data, current_user):
        return create_event(db, event_data, current_user)
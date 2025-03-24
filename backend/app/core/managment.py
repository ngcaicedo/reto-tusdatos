from app.core.authenticator.auth import login_user
from app.core.event import create_user

class Managment:
    """ Clase para gestionar las operaciones de la API """
    def __init__(self):
        pass

    def login(self, form_data, db):
        return login_user(form_data, db)
    
    def create_user(self, db, user_data):
        return create_user(db, user_data)
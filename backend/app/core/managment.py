from app.core.authenticator.auth import login_user

class Managment:
    """ Clase para gestionar las operaciones de la API """
    def __init__(self):
        pass

    def login(self, form_data, db):
        return login_user(form_data, db)
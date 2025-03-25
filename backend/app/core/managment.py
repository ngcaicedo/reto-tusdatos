from app.core.authenticator.auth import login_user
from app.core.user import create_user
from app.core.event import create_event, update_event, get_events, get_event
from app.core.assistant import create_assistant, get_assistants, get_assistant, update_assistant

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
    
    def update_event(self, db, event_id, event_data):
        return update_event(db, event_id, event_data)
    
    def get_events(self, db):
        return get_events(db)
    
    def get_event(self, db, event_id):
        return get_event(db, event_id)
    
    def create_assistant(self, db, assistant_data):
        return create_assistant(db, assistant_data)
    
    def update_assistant(self, db, assistant_id, assistant_data):
        return update_assistant(db, assistant_id, assistant_data)
    
    def get_assistants(self, db):
        return get_assistants(db)
    
    def get_assistant(self, db, assistant_id):
        return get_assistant(db, assistant_id)
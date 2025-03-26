from app.core.authenticator.auth import login_user
from app.core.user import create_user, register_user_assistant
from app.core.event import create_event, update_event, get_events, get_event, register_to_event, get_events_register_by_assistant
from app.core.assistant import create_assistant, get_assistants, get_assistant, update_assistant
from app.core.session import create_speaker, update_speaker, get_speakers, get_speaker, create_session, update_session, get_sessions, get_session

class Managment:
    """ Clase para gestionar las operaciones de la API """
    def __init__(self):
        pass

    def login(self, form_data, db):
        return login_user(form_data, db)
    
    def create_user(self, db, user_data):
        return create_user(db, user_data)
    
    def register_user_assistant(self, db, assistant_data):
        return register_user_assistant(db, assistant_data)
    
    def create_event(self, db, event_data, current_user):
        return create_event(db, event_data, current_user)
    
    def update_event(self, db, event_id, event_data):
        return update_event(db, event_id, event_data)
    
    def get_events(self, db):
        return get_events(db)
    
    def get_event(self, db, event_id):
        return get_event(db, event_id)
    
    def get_events_register_by_assistant(self, db, current_user):
        return get_events_register_by_assistant(db, current_user)
    
    def register_to_event(self, db, event_id, current_user):
        return register_to_event(db, event_id, current_user)
    
    def create_assistant(self, db, assistant_data):
        return create_assistant(db, assistant_data)
    
    def update_assistant(self, db, assistant_id, assistant_data):
        return update_assistant(db, assistant_id, assistant_data)
    
    def get_assistants(self, db):
        return get_assistants(db)
    
    def get_assistant(self, db, assistant_id):
        return get_assistant(db, assistant_id)
    
    def create_speaker(self, db, speaker_data):
        return create_speaker(db, speaker_data)
    
    def update_speaker(self, db, speaker_id, speaker_data):
        return update_speaker(db, speaker_id, speaker_data)
    
    def get_speakers(self, db):
        return get_speakers(db)
    
    def get_speaker(self, db, speaker_id):
        return get_speaker(db, speaker_id)
    
    def create_session(self, db, session_data):
        return create_session(db, session_data)
    
    def update_session(self, db, session_id, session_data):
        return update_session(db, session_id, session_data)
    
    def get_sessions(self, db):
        return get_sessions(db)
    
    def get_session(self, db, session_id):
        return get_session(db, session_id)
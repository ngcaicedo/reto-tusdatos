from app.models.event import Event, StateEnum
from faker import Faker
from datetime import datetime

class EventFactory:
    def __init__(self, db):
        self.event = Event()
        self.fake = Faker()
        self.db = db
        
    def generate_data(self, user_id: int, state: StateEnum, update: bool = False) -> dict:
        """ Función para generar los datos de un evento """
        data = {
            'name': self.fake.name(),
            'description': self.fake.sentence(),
            'capacity': 100,
            'state': state.value,
            'date_start': self.fake.date_time_this_year().isoformat(),
            'date_end': self.fake.date_time_this_year().isoformat(),
            'location': self.fake.address(),
            'user_created_id': user_id,
        }
        if update:
            data.pop('user_created_id')
        return data
    
    def create_event(self, user_id: int, state: str) -> Event:
        """ Función para crear un evento en la base de datos """
        data = self.generate_data(user_id, state)
        data['date_start'] = datetime.fromisoformat(data['date_start'])
        data['date_end'] = datetime.fromisoformat(data['date_end'])
        event = Event(**data)
        self.db.add(event)
        self.db.commit()
        self.db.refresh(event)
        return event
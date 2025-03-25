from app.core.managment import Managment
from app.core.authenticator.security import hash_password
from app.models.user import User, RoleEnum
from faker import Faker

class UserFactory:
    def __init__(self, db):
        self.db = db
        self.managment = Managment()
        self.fake = Faker()
        
    def create_user(self, role: RoleEnum = RoleEnum.ORGANIZADOR, email: str = None, password: str = '123456') -> User:
        if email is None:
            email = self.fake.email()
        """ Función para crear un usuario en la base de datos """
        user = User(
            name=self.fake.name(),
            phone=self.fake.phone_number(),
            email=email,
            role=role,
            password=hash_password(password),
        )
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user
    
    def login_user(self, role: RoleEnum) -> dict:
        """ Función para crear un usuario y autenticarlo """
        class MockForm:
            def __init__(self, username, password):
                self.username = username
                self.password = password
                self.scopes = []
        fake_password = self.fake.password()
        new_user = self.create_user(role=role, password=fake_password)
        form_data = MockForm(username=new_user.email, password=fake_password)
        user = self.managment.login(form_data, self.db)

        return user
        
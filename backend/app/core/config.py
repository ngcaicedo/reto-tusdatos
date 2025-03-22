import os
from dotenv import load_dotenv


class Settings:
    def __init__(self):
        self.env_file = ".env"
        load_dotenv(self.env_file)
        self.DATABASE_USER = os.getenv("DATABASE_USER")
        self.DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD")
        self.DATABASE_HOST = os.getenv("DATABASE_HOST")
        self.DATABASE_NAME = os.getenv("DATABASE_NAME")
        self.DATABASE_PORT = os.getenv("DATABASE_PORT")
        self.DATABASE_URL = f"postgresql://{self.DATABASE_USER}:{self.DATABASE_PASSWORD}@{self.DATABASE_HOST}:{self.DATABASE_PORT}/{self.DATABASE_NAME}"


settings = Settings()

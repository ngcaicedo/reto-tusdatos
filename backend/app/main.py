from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.models.user import User, RoleEnum
from app.api.v1.api_v1 import api_router
from fastapi.middleware.cors import CORSMiddleware
from app.db.session import SessionLocal
from app.core.authenticator.security import hash_password


@asynccontextmanager
async def lifespan(app: FastAPI):
    db = SessionLocal()
    default_name = 'admin'
    default_email = 'admin@gmail.com'
    default_password = 'admin'
    default_role = RoleEnum.ADMIN
    default_phone = '1234567890'
    user = db.query(User).filter(User.email == default_email).first()
    if not user:
        user = User(name=default_name, email=default_email, role=default_role,
                    password=hash_password(default_password), phone=default_phone)
        db.add(user)
        db.commit()
        db.refresh(user)
    yield
    db.close()

app = FastAPI(lifespan=lifespan)

origins = [
    "http://localhost",
    "http://localhost:3000",
    "http://localhost:8000",
    "http://localhost:4200",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router)


@app.get("/")
def root():
    return {"message": "Bienvenido a Mis Eventos API"}

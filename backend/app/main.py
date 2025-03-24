from fastapi import FastAPI
from app.api.v1.api_v1 import api_router

app = FastAPI()

app.include_router(api_router)

@app.get("/")
def root():
    return {"message": "Bienvenido a Mis Eventos API"}

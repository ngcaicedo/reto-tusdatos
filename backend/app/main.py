from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Bienvenido a Mis Eventos API"}

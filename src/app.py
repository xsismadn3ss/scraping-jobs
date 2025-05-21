from fastapi import FastAPI
from .routes import ofertas

app = FastAPI()

@app.get("/")
def read_root():
    return {
        "message": "Bienvenido a Sivar Chamba API"
    }

app.include_router(ofertas.router)
from fastapi import FastAPI
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from .routes import ofertas
import os

app = FastAPI()

app.add_middleware(
    TrustedHostMiddleware,
    allowed_hosts=[
        os.environ["ALLOWED_HOST"],
        "localhost",
        "127.0.0..1",
        "::1",
    ],
)


@app.get("/")
def read_root():
    return {"message": "Bienvenido a Sivar Chamba API"}


app.include_router(ofertas.router)

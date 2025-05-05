from pydantic import BaseModel
from typing import Any

class PaginaCreate(BaseModel):
    nombre: str
    dominio: str

class PaginaUpdate(BaseModel):
    pass

class Pagina(PaginaCreate):
    id: Any
    nombre: str
    dominio: str

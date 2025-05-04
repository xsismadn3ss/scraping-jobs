from pydantic import BaseModel

class Pagina(BaseModel):
    id: int
    nombre: str
    dominio: str

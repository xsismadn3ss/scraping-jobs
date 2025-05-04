from pydantic import BaseModel

class Empresa(BaseModel):
    id: int
    nombre: str

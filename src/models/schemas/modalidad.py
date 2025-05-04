from pydantic import BaseModel

class Modalidad(BaseModel):
    id: int
    nombre: str

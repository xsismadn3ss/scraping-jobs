from pydantic import BaseModel

class Busqueda(BaseModel):
    id: int
    parametros: str

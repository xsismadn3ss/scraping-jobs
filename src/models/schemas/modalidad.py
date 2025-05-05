from pydantic import BaseModel


class ModalidadCreate(BaseModel):
    nombre: str


class Modalidad(ModalidadCreate):
    id: str

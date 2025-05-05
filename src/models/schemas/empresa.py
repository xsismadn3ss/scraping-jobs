from pydantic import BaseModel


class EmpresaCreate(BaseModel):
    nombre: str


class Empresa(EmpresaCreate):
    id: str

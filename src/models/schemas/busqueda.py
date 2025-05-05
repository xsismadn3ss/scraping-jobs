from pydantic import BaseModel


class BusquedaCreate(BaseModel):
    parametros: str


class BusquedaUpdate(BusquedaCreate):
    pass


class Busqueda(BusquedaCreate):
    id: str
    parametros: str

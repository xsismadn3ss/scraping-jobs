from pydantic import BaseModel, Field
from datetime import date
from typing import Optional
from .empresa import Empresa
from .modalidad import Modalidad
from .busqueda import Busqueda
from .pagina import Pagina

class OfertaCreate(BaseModel):
    titulo:str
    descrcipcion:str
    salario: float
    publidado: date
    url: str
    # TODO: agregar parametros extra al implementar el controlador


class OfertaLinked(BaseModel):
    id: str
    titulo: str = Field(min_length=1)
    descripcion: str
    empresa: Optional[Empresa] = None
    modalidad: Optional[Modalidad] = None
    salario: float
    publicado: date
    pagina: Optional[Pagina] = None
    busqueda: Optional[Busqueda] = None
    url: str
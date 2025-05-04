from pydantic import BaseModel, Field
from datetime import date
from typing import Optional
from .empresa import Empresa
from .modalidad import Modalidad
from .busqueda import Busqueda
from .pagina import Pagina

class Oferta(BaseModel):
    # id: Any = Field(default=None)
    titulo: str = Field(min_length=1)
    descripcion: str
    empresa: Optional[Empresa] = None
    modalidad: Optional[Modalidad] = None
    salario: float
    publicado: date
    pagiana: Optional[Pagina] = None
    busqueda: Optional[Busqueda] = None
    url: str

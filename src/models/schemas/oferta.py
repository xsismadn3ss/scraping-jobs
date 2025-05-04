from pydantic import BaseModel, Field
from datetime import date
from typing import Any

class Oferta(BaseModel):
    id: Any = Field(default=None)
    titulo: str = Field(min_length=1)
    descripcion: str
    id_empresa: int
    id_modalidad: int
    salario: float
    publicado: date
    id_pagina: int
    id_busqueda: int
    url: str

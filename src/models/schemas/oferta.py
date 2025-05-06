from pydantic import BaseModel, Field, field_validator
from typing import Any, Optional
from src.models.schemas import Empresa, Modalidad, Busqueda, Pagina
from google.cloud.firestore import DocumentReference

class OfertaCreate(BaseModel):
    titulo: Optional[str] = None
    descripcion: Optional[str] = None
    salario: Optional[float] = None 
    publicado: Optional[str] = None
    url: Optional[str] = None
    empresa: Optional[str] = Field(description="referencia de la empresa", default=None)
    modalidad: Optional[str] = Field(description="referencia de la modalidad", default=None)
    pagina: Optional[str] = Field(description="referencia de la pagina", default=None)
    busqueda: Optional[str] = Field(description="referencia de la busqueda", default=None)


class OfertaLinked(BaseModel):
    id: str
    titulo: str = Field(min_length=1)
    descripcion: str
    salario: float
    publicado: str
    url: str
    empresa: Any = None
    modalidad: Any = None
    pagina: Any = None
    busqueda: Any = None

    @field_validator("empresa")
    def validate_empresa(cls, value):
        if isinstance(value, DocumentReference):
            doc = value.get()
            if not doc.exists:
                return None
            return Empresa(**doc.to_dict(), id=doc.id)  # type: ignore

    @field_validator("modalidad")
    def validate_modalidad(cls, value):
        if isinstance(value, DocumentReference):
            doc = value.get()
            if not doc.exists:
                return None
            return Modalidad(id=doc.id, **doc.to_dict())  # type: ignore
        return value

    @field_validator("pagina")
    def validate_pagina(cls, value):
        if isinstance(value, DocumentReference):
            doc = value.get()
            if not doc.exists:
                return None
            return Pagina(id=doc.id, **doc.to_dict())  # type: ignore
        return value

    @field_validator("busqueda")
    def validate_busqueda(cls, value):
        if isinstance(value, DocumentReference):
            doc = value.get()
            if not doc.exists:
                return None
            return Busqueda(id=doc.id, **doc.to_dict())  # type: ignore
        return value

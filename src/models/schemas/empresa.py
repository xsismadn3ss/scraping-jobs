from pydantic import BaseModel
from typing import Any

class Empresa(BaseModel):
    id: Any
    nombre: str

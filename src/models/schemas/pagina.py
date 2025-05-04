from pydantic import BaseModel
from typing import Any

class Pagina(BaseModel):
    # id: Any
    nombre: str
    dominio: str

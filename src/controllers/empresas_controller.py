from google.cloud.firestore import Client
from src.models.schemas.empresa import Empresa, EmpresaCreate
from src.controllers.base_controller import BaseController
from typing import override, List, Any

class EmpresasController(BaseController):
    """Controlador para la colección `empresas`"""

    def __init_subclass__(cls) -> None:
        return super().__init_subclass__()

    @override
    @classmethod
    def get_all(cls, db: Client, collection_name: str, count: int = 10, start_after=None) -> List[Empresa] | None:
        documents = super().get_all(db, collection_name, count, start_after)
        if not documents:
            return []
        return [Empresa(id=doc_id, **doc_data) for doc_data, doc_id in documents]

    @override
    @classmethod
    def get_by_id(cls, db, collection_name, id: str) -> Empresa:
        doc, doc_id = super().get_by_id(db, collection_name, id)
        return Empresa(**doc, id=doc_id)

    @override
    @classmethod
    def add(cls, db, collection_name, payload: EmpresaCreate) -> Empresa:
        doc_data, id = super().add(db, collection_name, payload)
        return Empresa(**doc_data, id=id)

    @override
    @classmethod
    def update(cls, db, collection_name, payload: EmpresaCreate, id: str) -> Empresa:
        doc_data, doc_id = super().update(db, collection_name, payload, id)
        return Empresa(**doc_data, id=doc_id)

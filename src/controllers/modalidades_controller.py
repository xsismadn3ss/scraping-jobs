from google.cloud.firestore import Client
from src.models.schemas.modalidad import Modalidad, ModalidadCreate
from src.controllers.base_controller import BaseController
from typing import override, List, Any

class ModalidadesController(BaseController):
    """Controlador para la colección `modalidades`"""

    def __init_subclass__(cls) -> None:
        return super().__init_subclass__()

    @override
    @classmethod
    def get_all(cls, db: Client, collection_name: str, count: int = 10, start_after=None) -> List[Modalidad] | None:
        documents = super().get_all(db, collection_name, count, start_after)
        if not documents:
            return []
        return [Modalidad(id=doc_id, **doc_data) for doc_data, doc_id in documents]

    @override
    @classmethod
    def get_by_id(cls, db, collection_name, id: str) -> Modalidad:
        doc, doc_id = super().get_by_id(db, collection_name, id)
        return Modalidad(**doc, id=doc_id)

    @override
    @classmethod
    def add(cls, db, collection_name, payload: ModalidadCreate) -> Modalidad:
        doc_data, id = super().add(db, collection_name, payload)
        return Modalidad(**doc_data, id=id)

    @override
    @classmethod
    def update(cls, db, collection_name, payload: ModalidadCreate, id: str) -> Modalidad:
        doc_data, doc_id = super().update(db, collection_name, payload, id)
        return Modalidad(**doc_data, id=doc_id)

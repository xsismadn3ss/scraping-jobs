from google.cloud.firestore import Client
from src.models.schemas.busqueda import Busqueda, BusquedaCreate
from src.controllers.base_controller import BaseController
from typing import override, List, Any


class BusquedasController(BaseController):
    """Controllador para la colección ``busquedas``"""

    def __init_subclass__(cls) -> None:
        return super().__init_subclass__()

    @override
    @classmethod
    def get_all(
        cls, db: Client, collection_name: str, count: int = 10, start_after=None
    ) -> List[Any] | None:
        documents = super().get_all(db, collection_name, count, start_after)

        if not documents:
            return []

        return [Busqueda(id=doc_id, **doc_data) for doc_data, doc_id, in documents]
    
    @classmethod
    @override
    def get_by_id(cls, db: Client, collection_name: str, id: str) -> Any:
        doc, doc_id = super().get_by_id(db, collection_name, id)
        return Busqueda(**doc, id=doc_id)

    @override
    @classmethod
    def add(cls, db, collection_name, payload: BusquedaCreate) -> Any:
        doc_data, id = super().add(db, collection_name, payload)
        return Busqueda(**doc_data, id=id)

    @override
    @classmethod
    def update(cls, db, collection_name, payload: BusquedaCreate, id: str) -> Any:
        doc_data, doc_id = super().update(db, collection_name, payload, id)
        return Busqueda(**doc_data, id=doc_id)

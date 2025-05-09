from google.cloud.firestore import Client
from src.models.schemas.oferta import OfertaCreate, OfertaLinked
from src.controllers.base_controller import BaseController
from typing import override, List, Any
from google.cloud.firestore import DocumentReference, CollectionReference


class OfertasController(BaseController):
    """Controlador para la colección ``ofertas``"""

    def __init_subclass__(cls) -> None:
        return super().__init_subclass__()

    @override
    @classmethod
    def get_all(
        cls, db: Client, collection_name: str, count: int = 10, start_after=None
    ) -> List[OfertaLinked] | None:
        documents = super().get_all(db, collection_name, count, start_after)

        if not documents:
            return []

        return [OfertaLinked(**doc_data, id=doc_id) for doc_data, doc_id in documents]

    @override
    @classmethod
    def get_by_id(cls, db, collection_name: str, id: str) -> Any:
        doc, doc_id = super().get_by_id(db, collection_name, id)
        return OfertaLinked(**doc, id=doc_id)

    @override
    @classmethod
    def add(cls, db: Client, collection_name: str, payload: OfertaCreate) -> Any:
        payload_f = payload.model_dump(exclude_none=True)

        
        for ref_field in ["empresa", "modalidad", "pagina", "busqueda"]:
            if ref_field in payload_f and isinstance(payload_f[ref_field], str):
                doc_ref: DocumentReference = db.document(payload_f[ref_field])
                cls.validate_document_ref(doc_ref)
                payload_f[ref_field] = doc_ref

        doc, doc_id = super().add(db, collection_name, payload_f)
        return OfertaLinked(**doc, id=doc_id)

    @override
    @classmethod
    def update(
        cls, db: Client, collection_name: str, payload: OfertaCreate, id: str
    ) -> Any:
        collection_ref: CollectionReference = db.collection(collection_name)
        cls.validate_collection_ref(collection_name)
        doc_ref: DocumentReference = collection_ref.document(id)
        cls.validate_document_ref(doc_ref)

        payload_f = payload.model_dump(exclude_none=True)

       
        for ref_field in ["empresa", "modalidad", "pagina", "busqueda"]:
            if ref_field in payload_f and isinstance(payload_f[ref_field], str):
                ref: DocumentReference = db.document(payload_f[ref_field])
                cls.validate_collection_ref(ref)
                payload_f[ref_field] = ref

      
        doc: dict = doc_ref.get().to_dict()  
        doc.update(payload_f)
        doc_ref.update(doc)
        doc_updated = doc_ref.get()
        return OfertaLinked(**doc_updated.to_dict(), id=doc_updated.id)  

    @override
    @classmethod
    def delete(cls, db, collection_name: str, id: str) -> bool:
        return super().delete(db, collection_name, id)

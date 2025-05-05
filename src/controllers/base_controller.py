from src.config import db as firestore_db
from typing import Any, List
from google.cloud.firestore import (
    DocumentReference,
    CollectionReference,
    DocumentSnapshot,
)
from google.protobuf.timestamp_pb2 import Timestamp
from google.cloud.firestore import Client
from src.controllers import console
from pydantic import BaseModel


class BaseController:
    """Clase base para los controladores de Firestore"""

    @classmethod
    def validate_collection_ref(cls, ref) -> bool:
        """Validar referencia a la colección"""
        if ref is None:
            raise ValueError(
                "No se encontró la referencia a la colección: {}".format(ref.id)
            )
        return True

    @classmethod
    def validate_document_ref(cls, ref) -> bool:
        """Validar referencia a la colección"""
        doc = ref.get()
        if not doc.exists:
            raise ValueError(
                "No se encontró la referencia al documento: {}".format(ref.id)
            )
        return True

    @classmethod
    def get_all(
        cls, db: Client, collection_name: str, count: int = 10, start_after=None
    ) -> List[Any] | None:
        """Obtener todos los documentos de la colección con soporte para paginación"""
        collection_ref: CollectionReference = db.collection(collection_name)
        cls.validate_collection_ref(ref=collection_ref)

        query = collection_ref.limit(count)
        if start_after:
            # Recuperar el documento de referencia para paginación
            start_after_doc = collection_ref.document(start_after).get()
            if not start_after_doc.exists:
                raise ValueError(f"No se encontró el documento con ID: {start_after}")
            query = query.start_after(start_after_doc)

        results = [(doc.to_dict(), doc.id) for doc in query.stream()]
        return results if results else None

    @classmethod
    def get_by_id(cls, db, collection_name: str, id: str) -> tuple[Any, int] | None:
        """Obtener un documento por su ID"""
        # obtener y validar coleción
        collecction_ref = db.collection(collection_name)
        cls.validate_collection_ref(ref=collecction_ref)

        doc_ref = collecction_ref.get(id)
        cls.validate_document_ref(ref=doc_ref)

        try:
            doc: DocumentSnapshot = doc_ref.get()
            return doc.to_dict(), doc.id
        except Exception as e:
            console.log(f"[bold red]Error: {e}[/]")
            return None

    @classmethod
    def add(cls, db, collection_name: str, payload: Any) -> Any:
        """Crear un nuevo documento en la colección"""
        collection_ref = db.collection(collection_name)
        cls.validate_collection_ref(collection_ref)

        try:
            if isinstance(payload, BaseModel):
                payload = payload.model_dump()

            data = collection_ref.add(payload)
            doc_ref = data[1]
            timestamp: Timestamp = data[0]

            doc = doc_ref.get()

            console.log(
                f"[bold green]Documento creado con ID:[/] [bold magenta]{doc_ref.id}[/]"
            )
            console.log(f"[bold green]Timestamp:[/] {timestamp}")

            return doc.to_dict(), doc.id

        except Exception as e:
            console.log(f"[bold red]Error: {e}[/]")
            return None

    @classmethod
    def update(cls, db, collection_name: str, payload: Any, id: str) -> Any:
        """Actualizar un documento en la colección"""

        collection_ref = db.collection(collection_name)
        cls.validate_collection_ref(collection_ref)

        doc_ref: DocumentReference = collection_ref.document(id)
        cls.validate_document_ref(ref=doc_ref)

        try:
            if isinstance(payload, BaseModel):
                payload = payload.model_dump()

            doc_ref.update(payload)
            doc_updated: DocumentSnapshot = doc_ref.get()

            return doc_updated.to_dict(), doc_updated.id
        except Exception as e:
            console.log(f"[bold red]Error: {e}[/]")
            return None

    @classmethod
    def delete(cls, db, collection_name: str, id: str) -> bool:
        """Eliminar un documento de la colección"""
        doc_ref: DocumentReference = db.collection(collection_name).document(id)

        try:
            doc_ref.delete()
            return True
        except Exception as e:
            console.log(f"[bold red]Error: {e}[/]")
            return False

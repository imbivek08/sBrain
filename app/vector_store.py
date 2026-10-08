import chromadb

from app.config import CHROMA_PATH


client = chromadb.PersistentClient(
    path=CHROMA_PATH
)

collection = client.get_or_create_collection(
    name="second_brain"
)


def add_document(
    document_id: str,
    text: str,
    embedding: list[float],
    metadata: dict,
):
    collection.upsert(
        ids=[document_id],
        documents=[text],
        embeddings=[embedding],
        metadatas=[metadata],
    )


def search(
    embedding: list[float],
    top_k: int = 5,
):
    return collection.query(
        query_embeddings=[embedding],
        n_results=top_k,
    )
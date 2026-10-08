import ollama
from app.config import EMBEDDING_MODEL


def create_embedding(text: str) -> list[float]:
    response = ollama.embed(
        model=EMBEDDING_MODEL,
        input=text,
    )

    return response["embeddings"][0]
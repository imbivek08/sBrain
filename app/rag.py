from app.embeddings import create_embedding
from app.vector_store import search


def retrieve_context(
    question: str,
    top_k: int = 3,
) -> list[str]:

    question_embedding = create_embedding(question)

    results = search(
        question_embedding,
        top_k=top_k,
    )

    return results["documents"][0]
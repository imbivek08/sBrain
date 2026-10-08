from pathlib import Path

from app.config import NOTES_PATH
from app.chunker import chunk_text
from app.embeddings import create_embedding
from app.vector_store import add_document


def load_markdown_files():

    notes_path = Path(NOTES_PATH)

    return list(
        notes_path.glob("**/*.md")
    )


def ingest_notes():

    files = load_markdown_files()

    for file_path in files:

        text = file_path.read_text(
            encoding="utf-8"
        )

        chunks = chunk_text(text)

        for index, chunk in enumerate(chunks):

            embedding = create_embedding(
                chunk
            )

            document_id = (
                f"{file_path}:{index}"
            )

            add_document(
                document_id=document_id,
                text=chunk,
                embedding=embedding,
                metadata={
                    "source": str(file_path),
                    "chunk": index,
                },
            )

            print(
                f"Indexed {file_path} "
                f"chunk {index}"
            )


if __name__ == "__main__":
    ingest_notes()
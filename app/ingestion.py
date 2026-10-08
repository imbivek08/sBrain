from pathlib import Path

from app.config import NOTES_PATH
from app.embeddings import create_embedding
from app.vector_store import add_document


def load_markdown_files():
    notes_path = Path(NOTES_PATH)

    return list(notes_path.glob("**/*.md"))


def ingest_notes():
    files = load_markdown_files()

    for file_path in files:
        text = file_path.read_text(
            encoding="utf-8"
        )

        embedding = create_embedding(text)

        add_document(
            document_id=str(file_path),
            text=text,
            embedding=embedding,
            metadata={
                "source": str(file_path),
            },
        )

        print(f"Indexed: {file_path}")


if __name__ == "__main__":
    ingest_notes()
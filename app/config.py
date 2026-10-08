import os

from dotenv import load_dotenv

load_dotenv()

OLLAMA_HOST = os.getenv(
    "OLLAMA_HOST",
    "http://localhost:11434",
)

LLM_MODEL = os.getenv(
    "LLM_MODEL",
    "qwen3:1.7b",
)

EMBEDDING_MODEL = os.getenv(
    "EMBEDDING_MODEL",
    "nomic-embed-text",
)

CHROMA_PATH = os.getenv(
    "CHROMA_PATH",
    "./data/chroma",
)

NOTES_PATH = os.getenv(
    "NOTES_PATH",
    "./data/notes",
)
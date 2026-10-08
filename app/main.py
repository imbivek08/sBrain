from fastapi import FastAPI
from pydantic import BaseModel

from app.rag import retrieve_context
from app.llm import generate_answer


app = FastAPI(
    title="Local Second Brain",
)


class Question(BaseModel):
    question: str


@app.get("/health")
def health():
    return {
        "status": "ok"
    }


@app.post("/ask")
def ask(request: Question):

    context = retrieve_context(
        request.question
    )

    answer = generate_answer(
        request.question,
        context,
    )

    return {
        "question": request.question,
        "answer": answer,
        "sources": context,
    }
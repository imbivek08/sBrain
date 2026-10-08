import ollama

from app.config import LLM_MODEL


def generate_answer(
    question: str,
    context: list[str],
) -> str:

    context_text = "\n\n---\n\n".join(context)

    prompt = f"""
You are my local personal knowledge assistant.

Answer the question using the provided notes.

If the answer cannot be found in the notes,
say that the information is not available in the notes.

Notes:

{context_text}

Question:

{question}

Answer:
"""

    response = ollama.chat(
        model=LLM_MODEL,
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
    )

    return response["message"]["content"]
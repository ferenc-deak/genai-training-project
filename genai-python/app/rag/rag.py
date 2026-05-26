import os
from dotenv import load_dotenv
from huggingface_hub import InferenceClient

from app.rag.retriever import get_retriever

load_dotenv()

# ----------------------------
# HuggingFace LLM Client
# ----------------------------
client = InferenceClient(
    api_key=os.getenv("HF_TOKEN")
)

# ----------------------------
# CACHE RETRIEVER (IMPORTANT)
# ----------------------------
_retriever = None


def get_db():
    """
    Initialize retriever once and reuse it.
    """
    global _retriever

    if _retriever is None:
        _retriever = get_retriever()

    return _retriever


# ----------------------------
# MAIN RAG FUNCTION
# ----------------------------
def ask_question(question: str):
    db = get_db()

    # Retrieve relevant documents
    docs = db.similarity_search(question, k=5)

    if not docs:
        return {
            "answer": "I don't know based on the provided documents.",
            "sources": []
        }

    # Build context
    context = "\n\n".join([doc.page_content for doc in docs])

    print("DOCS FOUND:", len(docs))
    print(docs[:1])

    prompt = f"""
You are a helpful assistant.

Rules:
- Use ONLY the context below
- If answer is not in context, say "I don't know"

CONTEXT:
{context}

QUESTION:
{question}

ANSWER:
"""

    # Call LLM (HF hosted model)
    response = client.chat.completions.create(
        model="Qwen/Qwen2.5-7B-Instruct",
        messages=[
            {"role": "system", "content": "You are a strict RAG assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=300,
        temperature=0.2
    )

    return {
        "answer": response.choices[0].message.content,
        "sources": [
            {
                "preview": doc.page_content[:150]
            }
            for doc in docs
        ]
    }
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
VECTORSTORE_PATH = os.path.normpath(
    os.path.join(BASE_DIR, "..", "..", "data", "chroma_db")
)

def search_docs(query: str, k: int = 5):
    db = get_retriever()

    results = db.similarity_search(query, k=k * 5)

    stop_words = {
        "the",
        "is",
        "a",
        "an",
        "of",
        "for",
        "to",
        "and",
        "what",
        "how"
    }

    query_words = [
        w.lower()
        for w in query.split()
        if w.lower() not in stop_words
    ]

    scored = []

    for r in results:
        text = r.page_content.lower()

        score = sum(
            1
            for word in query_words
            if word in text
        )

        scored.append((score, r))

    scored.sort(
        key=lambda x: x[0],
        reverse=True
    )

    return [
        doc
        for _, doc in scored[:k]
    ]

def get_retriever():
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    db = Chroma(
        persist_directory=VECTORSTORE_PATH,
        embedding_function=embeddings
    )

    return db
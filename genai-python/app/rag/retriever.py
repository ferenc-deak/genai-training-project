from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
VECTORSTORE_PATH = os.path.normpath(
    os.path.join(BASE_DIR, "..", "..", "data", "chroma_db")
)

def search_docs(query: str, k: int = 3):
    db = get_retriever()
    results = db.similarity_search(query, k=k)
    return [r.page_content for r in results]

def get_retriever():
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    db = Chroma(
        persist_directory=VECTORSTORE_PATH,
        embedding_function=embeddings
    )

    return db
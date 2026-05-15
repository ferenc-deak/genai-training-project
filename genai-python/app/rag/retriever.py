import os
from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

# ----------------------------
# SAME PATH AS INDEXER (CRITICAL)
# ----------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
VECTORSTORE_PATH = os.path.join(BASE_DIR, "..", "..", "data", "chroma_db")
VECTORSTORE_PATH = os.path.normpath(VECTORSTORE_PATH)


# ----------------------------
# LOAD EMBEDDINGS (MUST MATCH INDEXER)
# ----------------------------
def get_embeddings():
    return HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )


# ----------------------------
# LOAD VECTOR DB
# ----------------------------
def get_retriever():
    embeddings = get_embeddings()

    db = Chroma(
        persist_directory=VECTORSTORE_PATH,
        embedding_function=embeddings
    )

    return db
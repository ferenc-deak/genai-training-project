import sys
import os
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

# ----------------------------
# PATH SETUP (IMPORTANT FIX)
# ----------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATA_PATH = os.path.join(BASE_DIR, "..", "..", "data", "docs")
DATA_PATH = os.path.normpath(DATA_PATH)

VECTORSTORE_PATH = os.path.join(BASE_DIR, "..", "..", "data", "chroma_db")
VECTORSTORE_PATH = os.path.normpath(VECTORSTORE_PATH)


# ----------------------------
# LOAD TXT FILES
# ----------------------------
def load_docs():

    documents = []

    print("\nFILES FOUND IN FOLDER:")

    for file in os.listdir(DATA_PATH):

        filepath = os.path.join(DATA_PATH, file)

        if file.endswith(".txt"):

            print("LOADING:", file)

            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()

                print(f"{file}: {len(content)} characters")

                documents.append({
                    "content": content,
                    "source": file
                })

    print(f"\nTOTAL FILES LOADED: {len(documents)}")

    return documents


# ----------------------------
# BUILD VECTOR DB
# ----------------------------
def build_index():
    docs = load_docs()

    # Chunking strategy:
    # - chunk_size=100 keeps more related information together.
    # - chunk_overlap=20 preserves context between neighboring chunks,
    #   reducing the chance that important information is split.
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=100,
        chunk_overlap=20,
        separators=["\n\n", "\n", ". ", " "]
    )

    chunks = []
    metadatas = []
    for doc in docs:
        split_chunks = splitter.split_text(
        doc["content"]
    )

    chunks.extend(split_chunks)

    for _ in split_chunks:
        metadatas.append({
            "source": doc["source"]
    })

    print("\nTOTAL DOCUMENTS:", len(docs))
    print("TOTAL CHUNKS CREATED:", len(chunks))

    # Embeddings (MUST MATCH retriever.py)
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    # Create / overwrite DB
    db = Chroma.from_texts(
        texts=chunks,
        metadatas=metadatas,
        embedding=embeddings,
        persist_directory=VECTORSTORE_PATH
    )

    # db.persist()  # Not needed with Chroma 0.4+

    print("\n Vector DB created successfully at:", VECTORSTORE_PATH)


# ----------------------------
# RUN MANUALLY
# ----------------------------
if __name__ == "__main__":
    build_index()
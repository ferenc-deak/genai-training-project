import os

from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings


DATA_PATH = "data/docs"
VECTORSTORE_PATH = "vectorstore"


def load_docs():
    texts = []

    for file in os.listdir(DATA_PATH):
        filepath = os.path.join(DATA_PATH, file)

        if file.endswith(".txt"):
            with open(filepath, "r", encoding="utf-8") as f:
                texts.append(f.read())

    return texts


def build_index():
    docs = load_docs()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        separators=[
            "\n\n",
            "\n",
            ". ",
            " ",
        ],
    )

    chunks = []

    for doc in docs:
        chunks.extend(splitter.split_text(doc))

    print(f"Created {len(chunks)} chunks")

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    db = Chroma.from_texts(
        texts=chunks,
        embedding=embeddings,
        persist_directory=VECTORSTORE_PATH,
    )

    db.persist()

    print("✅ Vector DB created successfully!")


if __name__ == "__main__":
    build_index()
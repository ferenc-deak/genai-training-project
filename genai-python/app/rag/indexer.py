from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings


def create_vectorstore():

    # Load txt file
    loader = TextLoader(
        "docs/ai_intro.txt",
        encoding="utf-8"
    )

    documents = loader.load()

    # Split text into chunks
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=300,
        chunk_overlap=50
    )

    docs = splitter.split_documents(documents)

    # Embeddings model
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    # Create Chroma DB
    db = Chroma.from_documents(
        docs,
        embeddings,
        persist_directory="vectorstore"
    )

    db.persist()

    print("Vectorstore created successfully!")
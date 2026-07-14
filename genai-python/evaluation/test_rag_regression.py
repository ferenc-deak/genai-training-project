from app.rag.retriever import search_docs


def test_rag_retrieves_rag_document():

    docs = search_docs(
        "What is RAG?",
        k=5
    )

    sources = [
        doc.metadata.get("source")
        for doc in docs
    ]

    assert "rag.md" in sources



def test_rag_retrieves_embedding_document():

    docs = search_docs(
        "What is an embedding?",
        k=5
    )

    sources = [
        doc.metadata.get("source")
        for doc in docs
    ]

    assert "embeddings.md" in sources
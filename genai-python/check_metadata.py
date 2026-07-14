from app.rag.retriever import get_retriever


db = get_retriever()

docs = db.similarity_search(
    "What is RAG?",
    k=3
)


for doc in docs:
    print("CONTENT:")
    print(doc.page_content[:100])

    print("METADATA:")
    print(doc.metadata)

    print("----------------")
from app.retriever import get_retriever
from transformers import pipeline


# Load Llama 3.1 model from Hugging Face
llm = pipeline(
    "text-generation",
    model="meta-llama/Llama-3.1-8B-Instruct",
    device_map="auto"
)


def ask_question(question: str):
    retriever = get_retriever()

    # modern LangChain API
    docs = retriever.invoke(question)

    context = "\n\n".join([d.page_content for d in docs])

    prompt = f"""
You are an assistant that answers ONLY using the context below.

CONTEXT:
{context}

QUESTION:
{question}

If the answer is not in the context, say "I don't know".
"""

    response = llm(
        prompt,
        max_new_tokens=300,
        do_sample=True,
        temperature=0.2
    )

    answer = response[0]["generated_text"]

    return {
        "answer": answer,
        "sources": [d.page_content[:150] for d in docs]
    }
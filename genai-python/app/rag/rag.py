import os
from huggingface_hub import InferenceClient
from retriever import get_retriever

client = InferenceClient(
    api_key=os.getenv("HF_TOKEN")
)


def ask_question(question: str):

    retriever = get_retriever()

    docs = retriever.invoke(question)

    context = "\n\n".join([d.page_content for d in docs])

    if not docs:
        return {
            "answer": "I don't know based on the provided documents.",
            "sources": []
        }

    prompt = f"""
You are a helpful assistant.

Use ONLY the context below to answer.

CONTEXT:
{context}

QUESTION:
{question}

If the answer is not in the context, say "I don't know".
"""

    response = client.chat.completions.create(
        model="meta-llama/Llama-3.1-8B-Instruct",
        messages=[
            {"role": "user", "content": prompt}
        ],
        max_tokens=300,
        temperature=0.2
    )

    return {
        "answer": response.choices[0].message.content,
        "sources": [d.page_content[:150] for d in docs]
    }
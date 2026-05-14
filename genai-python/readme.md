1. How to run API
   python -m uvicorn app.main:app --reload
2. How to run evaluation
   python evaluate.py
3. How to test reproducibility
   python repro_steps.py

## Baseline Engineering Setup

1. I did a Deterministic LLM classifier:
   response = client.chat.completions.create(
   model="meta-llama/Llama-3.1-8B-Instruct",
   messages=[{"role": "user", "content": structured_prompt}],
   max_tokens=300,
   temperature=0
   )
   a. temperature=0 → no randomness
   b. same prompt → same output
   c. same model → same behavior
   structured_prompt = f"""
   You are a strict classification system...
   """ – forces the model to bahave like a classifier
2. Evaluation pipeline:
   with open("eval_dataset.jsonl", "r") as f:
   for line in f:
   sample = json.loads(line)

output = generate_agent(sample["input"])

3. I created a file called repro_test.py and it:
   Demonstrated reproducibility of results
   it was demonstrated by:
   a. repeating the same request
   b. showing identical outputs
   c. proving deterministic behavior

## 🧠 Transformer Learning Module (Experimental)

This project includes a small experimental module to help understand how Transformers work internally, especially the attention mechanism.

It is NOT a production model. It is purely for learning and visualization purposes.

---

## 📌 Goals

- Explore a minimal self-attention mechanism (Transformer concept)
- Visualize how attention is distributed between words
- Modify input sentences and observe how attention changes

---

## ⚙️ How it works

The module simulates a simplified Transformer attention mechanism:

- Each word is converted into a vector representation
- Query (Q), Key (K), and Value (V) matrices are computed
- Attention scores are calculated using dot-product similarity
- Softmax is applied to normalize attention weights
- The attention matrix shows how each word influences others

---

## ▶️ How to run the demo

Run the attention visualization script:

```bash
python app/attention_demo.py
```

# 🧠 Minimal Transformer + Attention Visualization

This project implements a **minimal Transformer model from scratch using PyTorch**.  
It is designed for learning and understanding how **self-attention works internally** in modern AI models like GPT.

The goal is not performance, but **visual explanation and experimentation**.

---

# 🚀 Features

- Minimal self-attention mechanism (Query, Key, Value)
- Simple tokenization of input sentences
- Attention matrix computation
- Visualization of attention maps using heatmaps
- Ability to modify inputs and observe behavior changes

---

# 📦 Tech Stack

- Python 3.12
- PyTorch
- Matplotlib
- Seaborn

I demonstrated:

✔ Transformer mechanics
✔ Attention computation
✔ Context sensitivity
✔ Visualization of internal weights

# RAG System (Retrieval-Augmented Generation)

This project implements a **Retrieval-Augmented Generation (RAG)** system that allows users to ask questions over a custom set of documents and receive AI-generated answers grounded in those documents.

---

## 🧠 What is RAG?

RAG (Retrieval-Augmented Generation) is an architecture that combines:

- **Information retrieval** (searching relevant document chunks)
- **Large Language Models (LLMs)** (generating natural language answers)

Instead of relying only on model training data, the system retrieves relevant information from external documents at query time and uses it to generate accurate answers.

---

## ⚙️ How it works

The system follows this pipeline:

1. User sends a question
2. Question is converted into an embedding
3. System searches similar document chunks from a vector database
4. Most relevant chunks are retrieved
5. Retrieved context is passed to an LLM
6. LLM generates an answer based only on that context

---

## 🏗️ Architecture

---

## 📁 Project Structure

```

rag-project/
│
├── app/
│   ├── main.py          # FastAPI entry point
│   ├── rag.py           # Core RAG logic
│   ├── ingest.py        # Document ingestion & embedding
│   ├── retriever.py     # Vector search logic
│
├── data/
│   └── docs/            # Source documents
│
├── vectorstore/         # Stored embeddings
├── tests/               # Evaluation & regression tests
├── requirements.txt
└── dockerfile
```

Steps:

You upload or store your documents (PDFs, notes, DB content, etc.)
The system splits them into small text chunks
Each chunk is converted into a vector (embedding)
When you ask a question:
your query is also converted into a vector
the system finds the most similar chunks
Those chunks are sent to the AI (OpenAI / Hugging Face)
The AI answers using only that context

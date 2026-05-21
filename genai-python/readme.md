1. How to run API
   Activate in git bash:
   source venv/Scripts/activate
2. python -m uvicorn app.main:app --reload
3. How to run evaluation
   python evaluate.py
4. How to test reproducibility
   python repro_steps.py

## 🧠 Baseline Engineering Setup

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

## RAG System (Retrieval-Augmented Generation)

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

## 🧠 Fine-Tuning & Adaptation

1. I created a dataset.jsonl file

2. I opened Open Google Colab

3. Upload your dataset - dataset.jsonl

4. Loaded dataset

5. Installed confirmed libraries and extensions: !pip install -q transformers datasets peft accelerate bitsandbytes

6. Loaded the model:

   from transformers import AutoTokenizer, AutoModelForCausalLM

   model_name = "microsoft/phi-3-mini-4k-instruct"

   tokenizer = AutoTokenizer.from_pretrained(model_name)

   model = AutoModelForCausalLM.from_pretrained(
   model_name,
   device_map="auto"
   )

7. Tokenizer - tokenizer = AutoTokenizer.from_pretrained(...)
   Converts text → numbers (tokens)
   Converts numbers → text
   This is just translation, not intelligence

   We built in Google Colab is basically a mini AI training pipeline.
   The objective was: Load a pretrained LLM → give it your custom dataset → fine-tune it with LoRA so it learns your own knowledge/style.

   In the lora_finetune.py - are the steps of a training script that tells the computer HOW to fine-tune a model using LoRA

## Prompting vs RAG vs Fine-Tuning vs Hybrid Systems

In modern GenAI systems, there are four main approaches to adapting large language models: prompting, retrieval-augmented generation (RAG), fine-tuning, and hybrid systems. Each method represents a different way of controlling model behavior, knowledge access, and system reliability.

1.  Prompting

Prompting is the simplest approach where the model is guided only through input instructions (prompts) at runtime. No changes are made to the model itself.

It relies entirely on the model’s built-in knowledge and the clarity of the instructions provided. Prompting is easy to implement and requires no additional infrastructure.

However, it is limited because it cannot access external or updated information and may produce inconsistent or incorrect outputs.

Best use cases: prototypes, chatbots, formatting tasks, simple assistants.

2.  RAG (Retrieval-Augmented Generation)

RAG improves LLM responses by adding an external knowledge retrieval step. Before generating an answer, the system searches a document store (often using embeddings) and provides relevant context to the model.

This makes the model more accurate and allows it to use up-to-date or private data without retraining.

The main challenge is ensuring good retrieval quality, since the final output depends heavily on the relevance of the retrieved documents.

Best use cases: document Q&A, enterprise knowledge bases, support systems.

3.  Fine-Tuning

Fine-tuning modifies the internal weights of a model using domain-specific training data. Instead of providing knowledge at runtime, the model learns patterns, behavior, or domain expertise during training.

This approach is useful when consistent behavior, style, or structured output is required.

However, it is expensive, harder to maintain, and does not easily adapt to new information unless retrained.

Best use cases: domain-specific assistants, classification tasks, structured outputs.

4.  Hybrid Systems

Hybrid systems combine multiple approaches—typically prompting, RAG, and fine-tuning—to achieve production-grade performance.

In these systems:

RAG provides external knowledge
Fine-tuning shapes model behavior
Prompting controls runtime instructions

This layered approach provides the best balance of accuracy, flexibility, and control, but it is also the most complex to design and maintain.

Best use cases: production AI products, enterprise systems, advanced assistants.

This the link to the Lora Fine tune in google console (lora-finetune.ipynb): https://colab.research.google.com/drive/1Db8HL098rW8cX4ujp5qx3bBDWQOwGrzW?usp=sharing

1. Prompting:
   a. Performance: Fastest,
   b. Complexity: Lowest,
   c. Cost: Low,
   d. Key Strength: Simplicity

2. RAG:
   a. Performance: Medium,
   b. Complexity: High,
   c. Cost: Medium,
   d. Key Strength: Fresh + factual answers

3. Fine-tuning:
   a. Performance: Fastest,
   b. Complexity: High,
   c. Cost: High (train), Low (run)
   d. Key Strength: Consistent behavior

4. Hybrid:
   a. Performance: Slowest
   b. Complexity: Highest
   c. Cost: Highest
   d. Key Strength: Best overall quality

## Tool Calling & MCP

# Run server

python -m app.main

# Run tests

pytest

# Tools

- add(a, b)
- divide(a, b)
- get_user(user_id)

# Rules

- No silent failures
- All inputs validated with Pydantic
- Errors return structured response with isError

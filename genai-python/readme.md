1. How to run API
   uvicorn app.main:app --reload
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

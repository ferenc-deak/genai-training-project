# 🧠 AI System Project Overview

This project is a modular AI system including RAG, tools (MCP), agents, evaluation, fine-tuning, and transformer experiments.

---

# 📁 Project Structure (Table Overview)

## 🗂️ Core System Modules

| File / Module        | Purpose         | Description                                      |
| -------------------- | --------------- | ------------------------------------------------ |
| app/main.py          | API Entry Point | FastAPI server, routes, and system orchestration |
| app/rag/rag.py       | RAG Core        | Retrieval-Augmented Generation pipeline          |
| app/rag/retriever.py | Vector Search   | Finds relevant document chunks via embeddings    |
| app/rag/ingestion.py | Data Ingestion  | Splits documents and creates embeddings          |
| vectorstore/         | Vector DB       | Stores embeddings for retrieval                  |
| docs/                | Knowledge Base  | Source documents for RAG                         |

---

## 🤖 Agent & Workflow System

| File / Module               | Purpose         | Description                           |
| --------------------------- | --------------- | ------------------------------------- |
| app/external.py             | Main Agent      | LLM orchestration and reasoning logic |
| app/planner.py              | Planner Agent   | Breaks tasks into structured steps    |
| app/executor.py             | Executor Agent  | Executes planned steps                |
| app/workflow/workflow.py    | Workflow Engine | Manages multi-agent execution         |
| app/workflow/state_store.py | State Store     | Persists workflow state               |

---

## 🔌 Tool Calling (MCP System)

| Layer        | Module            | Description                                                                  |
| ------------ | ----------------- | ---------------------------------------------------------------------------- |
| Tool Layer   | app/tools         | Implements core business logic (e.g., arithmetic operations, user retrieval) |
| MCP Server   | app/mcp/server.py | Exposes tools to the LLM and executes tool calls in a controlled environment |
| Schema Layer | app/schemas       | Defines Pydantic models for input validation and type safety                 |

---

## 🧪 Evaluation & Testing

| File / Module      | Purpose              | Description                                 |
| ------------------ | -------------------- | ------------------------------------------- |
| evaluate.py        | Evaluation Pipeline  | Runs dataset tests and measures performance |
| eval_dataset.jsonl | Dataset              | Evaluation data samples                     |
| repro_test.py      | Reproducibility Test | Ensures deterministic outputs               |

---

## 🧠 Learning Modules

| File / Module         | Purpose             | Description                                                   |
| --------------------- | ------------------- | ------------------------------------------------------------- |
| app/attention_demo.py | Transformer Demo    | Visualizes self-attention mechanism                           |
| lora_finetune.py      | Fine-Tuning         | LoRA-based model adaptation                                   |
| dataset.jsonl         | Training Data       | Dataset used for fine-tuning                                  |
| Run_lora_gpu.ipynb    | Fine-Tuning (Colab) | End-to-end LoRA fine-tuning of Phi-3 on GPU (Google Colab T4) |

---

## ⚙️ Performance Analysis

| File / Module       | Purpose            | Description                           |
| ------------------- | ------------------ | ------------------------------------- |
| latency_test.py     | Latency Test       | Measures response time vs batch size  |
| token_speed_test.py | Token Speed        | Measures tokens/sec vs context length |
| throughput_test.py  | Throughput Test    | System load analysis                  |
| report.py           | Performance Report | Aggregates benchmark results          |

---

# 🚀 How to Run

| Command                                 | Purpose                       |
| --------------------------------------- | ----------------------------- |
| source venv/Scripts/activate            | Activate environment          |
| python -m uvicorn app.main:app --reload | Run API server                |
| python evaluate.py                      | Run evaluation                |
| python repro_test.py                    | Run reproducibility tests     |
| python app/attention_demo.py            | Run transformer demo          |
| python -m app.mcp.server                | Runs inside package structure |
| run python train.py                     | Runs inside folder structure  |

---

# 🧠 Key Concepts

| Concept                 | Description                                        |
| ----------------------- | -------------------------------------------------- |
| RAG                     | Retrieval-Augmented Generation using vector search |
| MCP Tool Calling        | LLM selects and executes external tools            |
| Multi-Agent System      | Planner + Executor architecture                    |
| Determinism             | temperature=0 ensures reproducible outputs         |
| Fine-Tuning             | LoRA adaptation of pretrained models               |
| Attention Visualization | Understanding transformer internals                |
| System Evaluation       | Benchmarking and regression testing                |

## you should run python train.py from inside the folder to see the training loop

## 🧠 Fixed after feedback and implementations for Module 3

| Assessment               | Current Project                         | Status                                     |
| ------------------------ | --------------------------------------- | ------------------------------------------ |
| Shared embeddings        | `nn.Embedding`                          | ✅ Fixed                                   |
| Trainable Q/K/V          | `nn.Linear`                             | ✅ Fixed                                   |
| Trained weights          | `train.py` with Adam + CrossEntropyLoss | ✅ Fixed                                   |
| Meaningful visualization | `visualize.py` loads trained model      | ✅ Fixed                                   |
| `nn.Module`              | `TinyTransformer(nn.Module)`            | ✅ Fixed                                   |
| Positional encoding      | Not implemented                         | ⚠️ Mentioned as a minor note, not required |
| Multi-head attention     | Not implemented                         | ⚠️ Mentioned as a minor note, not required |
| Masking                  | Not implemented                         | ⚠️ Mentioned as a minor note, not required |

## Fixed after feedback and implementations for Module 4

## Chunking Strategy Evaluation

To improve retrieval quality, two chunking configurations were evaluated during development using the same document collection (`ai_intro.txt`, `fastapi.txt`, and `rag.txt`).

| Configuration | Chunk Size | Chunk Overlap | Evaluation                                                                                                                                                                      | Outcome  |
| ------------- | ---------: | ------------: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- |
| Initial       |        300 |            50 | Produced smaller chunks, but related information was occasionally split across chunk boundaries, resulting in less complete retrieval context.                                  | Rejected |
| Final         |        400 |            80 | Preserved more contextual information within each chunk while maintaining continuity through overlap. Manual testing showed more complete retrieved passages for RAG responses. | Selected |

### Why the final configuration was chosen

The project initially used a chunk size of **300** with an overlap of **50**. During manual testing, it was observed that some related information was divided between neighbouring chunks, reducing the amount of context returned during retrieval.

The chunk size was then increased to **400** and the overlap to **80**. This allowed more related information to remain within the same chunk while still preserving continuity between adjacent chunks. Testing the same document set showed that retrieved passages contained more complete context, making them more suitable for Retrieval-Augmented Generation (RAG).

For this reason, the **400/80** configuration was adopted as the final chunking strategy and is used by both the indexer and retriever.

## RAG Retrieval & Reranking Improvements

| Requirement                  | Status       | Implementation                                                                                                                                                                                                                                                                                                                                                                                          |
| ---------------------------- | ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Reranking / hybrid retrieval | ✅ Completed | Implemented a hybrid retrieval approach in `search_docs()`. The retriever over-fetches documents (`k*2`) using vector similarity search, applies a lexical reranking step based on query-word matches, and returns the top `k` most relevant chunks. The RAG pipeline now uses `search_docs()` directly inside `ask_question()`, ensuring reranked documents are used when generating the final answer. |

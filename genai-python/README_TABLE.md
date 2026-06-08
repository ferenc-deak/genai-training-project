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

| File / Module         | Purpose          | Description                         |
| --------------------- | ---------------- | ----------------------------------- |
| app/attention_demo.py | Transformer Demo | Visualizes self-attention mechanism |
| lora_finetune.py      | Fine-Tuning      | LoRA-based model adaptation         |
| dataset.jsonl         | Training Data    | Dataset used for fine-tuning        |

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

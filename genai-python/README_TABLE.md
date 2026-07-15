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

## 🧠 Module 3 – Transformer Improvements after Assessment Feedback

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

## 🧠 Module 4 – RAG Improvements after Assessment Feedback

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

## RAG Implementation Summary

### 1. Reranking / Hybrid Retrieval

| **Requirement**              | **Status**   |
| ---------------------------- | ------------ |
| Reranking / Hybrid Retrieval | ✅ Completed |

| **Implementation**                                                                                                                                                                                                                                                                                                                                                                                        |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Implemented a hybrid retrieval approach in `search_docs()`. The retriever over-fetches documents (`k × 2`) using vector similarity search, applies a lexical reranking step based on query-word matches, and returns the top `k` most relevant chunks. The RAG pipeline now uses `search_docs()` directly inside `ask_question()`, ensuring reranked documents are used when generating the final answer. |

---

| **Requirement**                                | **Status**   |
| ---------------------------------------------- | ------------ |
| Golden Dataset + Regression Tests + Evaluation | ✅ Completed |

| **Implementation**                                                                                                                                                                                                                                                                                                                                                                                                             |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Created a RAG-specific golden dataset (`evaluation/rag_dataset.jsonl`) mapping evaluation queries to their expected document sources. Implemented `evaluation/evaluate_rag.py` to compare baseline vector retrieval against hybrid retrieval using the Recall@5 metric. Added `evaluation/test_rag_regression.py` to verify retrieval behavior remains consistent across future changes and help detect retrieval regressions. |

# Module 5 – Comparison of Prompting, RAG, Fine-Tuning and Hybrid Approaches

## Comparison of AI Approaches

### 1. Prompting

**Advantages**

- Simple to implement.
- No additional infrastructure or training required.
- Low deployment cost.

**Disadvantages**

- Limited by the model's existing knowledge.
- More prone to hallucinations.
- Cannot learn new domain-specific information.

**Best Use Cases**

- General question answering.
- Brainstorming.
- Simple conversational tasks.

---

### 2. Retrieval-Augmented Generation (RAG)

**Advantages**

- Retrieves relevant information from external documents.
- Provides more accurate and up-to-date answers.
- Reduces hallucinations by grounding responses in retrieved sources.

**Disadvantages**

- Requires document ingestion and embedding generation.
- Requires maintaining a vector database.
- Retrieval quality depends on chunking and ranking strategies.

**Best Use Cases**

- Knowledge bases.
- Technical documentation.
- Company policies.
- Frequently changing information.

---

### 3. Fine-Tuning (LoRA)

**Advantages**

- Learns task-specific behaviour.
- Produces more consistent responses.
- LoRA trains only a small number of adapter parameters instead of the full model.

**Disadvantages**

- Requires labelled training data.
- Requires GPU resources for training.
- Requires retraining whenever knowledge changes.
- Does not automatically learn new factual information.

**Best Use Cases**

- Domain-specific assistants.
- Specialised writing styles.
- Instruction following.
- Classification tasks.

---

### 4. Hybrid (RAG + Fine-Tuning)

**Advantages**

- Combines the behavioural improvements of fine-tuning with the factual accuracy of RAG.
- Provides specialised responses while accessing current external knowledge.
- Reduces hallucinations while improving task-specific behaviour.

**Disadvantages**

- Highest implementation complexity.
- Requires maintaining both retrieval infrastructure and LoRA adapters.

**Best Use Cases**

- Production AI assistants.
- Enterprise knowledge assistants.
- Applications requiring specialised behaviour and continuously updated information.

---

## Trade-off Analysis

| Criterion                   | Prompting | RAG    | Fine-Tuning            | Hybrid |
| --------------------------- | --------- | ------ | ---------------------- | ------ |
| Implementation Complexity   | Low       | Medium | Medium                 | High   |
| Development Cost            | Low       | Medium | High                   | High   |
| Training Required           | No        | No     | Yes                    | Yes    |
| External Knowledge          | No        | Yes    | No                     | Yes    |
| Learns New Behaviour        | No        | No     | Yes                    | Yes    |
| Handles Updated Information | No        | Yes    | No                     | Yes    |
| Response Accuracy           | Medium    | High   | High for trained tasks | High   |

---

## Recommendation

For this project, the recommended approach is a **hybrid solution combining Retrieval-Augmented Generation (RAG) with LoRA fine-tuning**.

The RAG pipeline developed in Module 4 retrieves relevant document chunks using vector similarity search combined with lexical reranking before generating the final response. This enables the system to answer questions using the latest indexed documents without retraining the model whenever the knowledge base changes.

The LoRA fine-tuning implemented in Module 5 adapts the Phi-3 Mini model to better follow the project's instruction format while training only lightweight adapter parameters. This improves the model's behaviour without the computational cost of full model fine-tuning.

By combining both approaches, the system benefits from improved instruction following while maintaining access to current external knowledge.

---

## Decision Rationale

Fine-tuning should not be the default solution for every AI application.

If knowledge changes frequently, Retrieval-Augmented Generation is the preferred approach because new documents can simply be indexed without retraining the model.

Fine-tuning is most appropriate when the objective is to improve the model's behaviour, response style, or task-specific capabilities rather than introducing new factual knowledge.

For this project, a hybrid RAG + LoRA approach provides the best balance between factual accuracy, maintainability, and specialised behaviour.

---

## Fine-Tuning Evaluation

The LoRA fine-tuning process was successfully completed, producing a trained adapter with a final training loss of approximately **2.94** after one training epoch.

The objective of the fine-tuning process was to improve the model's instruction-following behaviour rather than introduce new factual knowledge. Since the knowledge available to the model remains unchanged, Retrieval-Augmented Generation continues to be the preferred solution for incorporating new or frequently changing information.

Overall, the project demonstrates that LoRA fine-tuning and RAG solve different problems. Fine-tuning adapts model behaviour, while RAG supplies current external knowledge. Combining both approaches provides a more flexible and effective solution than relying on either technique alone.

# Module 6 – Tool Calling & MCP Improvements

## Improvements Implemented

- Added schema-level validation for `DivideSchema` using a Pydantic `field_validator` to enforce that the divisor cannot be zero.
- Extended `test_contract.py` with negative validation tests to verify that invalid inputs raise `ValidationError`.
- Removed debugging artifacts (`test_mcp.py` and the commented-out debug line in `server.py`) to keep the project clean.

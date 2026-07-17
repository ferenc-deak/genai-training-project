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

# Module 4 – Retrieval-Augmented Generation (RAG)

## Improvements Implemented

| Improvement                  | Description                                                                                                                                                              |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Chunking Strategy Evaluation | Evaluated multiple chunking configurations and selected a chunk size of **400** with an overlap of **80** after comparing retrieval quality and contextual completeness. |
| Hybrid Retrieval & Reranking | Implemented hybrid retrieval by combining vector similarity search with lexical reranking to improve document relevance before answer generation.                        |
| Golden Dataset Evaluation    | Created a golden evaluation dataset to validate retrieval quality and compare retrieval approaches using Recall@5.                                                       |
| Regression Testing           | Added automated regression tests to ensure retrieval behaviour remains consistent after future changes to the RAG pipeline.                                              |

---

| Requirement | Status | Implementation |------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Chunking Strategy | ✅ Completed | Evaluated different chunk sizes and overlaps, selecting a **400-token chunk size** with **80-token overlap** because it preserved more contextual information while maintaining continuity between chunks. |
| Hybrid Retrieval & Reranking | ✅ Completed | Implemented a hybrid retrieval pipeline in `search_docs()` that over-fetches candidate documents using vector similarity search, applies lexical reranking based on query-term matches, and returns the most relevant document chunks. |
| RAG Integration | ✅ Completed | Updated the RAG pipeline so that `ask_question()` retrieves documents through the hybrid retrieval method before generating responses. |
| Golden Dataset Evaluation | ✅ Completed | Created `evaluation/rag_dataset.jsonl` containing evaluation queries mapped to their expected document sources for retrieval evaluation. |
| Retrieval Evaluation | ✅ Completed | Implemented `evaluation/evaluate_rag.py` to compare baseline vector retrieval against the hybrid retrieval approach using the Recall@5 evaluation metric. |
| Regression Testing | ✅ Completed | Implemented `evaluation/test_rag_regression.py` to verify retrieval consistency and detect regressions after future modifications to the retrieval pipeline. |

# Module 5 – Comparison of Prompting, RAG, Fine-Tuning and Hybrid Approaches

## Improvements Implemented

| Improvement                                   | Description                                                                                                                                                                      |
| --------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Prompting Analysis                            | Compared prompting as a lightweight approach requiring no additional training or infrastructure while highlighting its limitations regarding hallucinations and fixed knowledge. |
| Retrieval-Augmented Generation (RAG) Analysis | Evaluated RAG as a retrieval-based solution that improves factual accuracy by grounding responses in external documents while supporting frequently updated knowledge.           |
| LoRA Fine-Tuning Analysis                     | Analyzed LoRA fine-tuning as an efficient method for improving model behaviour and instruction following using lightweight adapter parameters.                                   |
| Hybrid Approach Evaluation                    | Compared a hybrid RAG + LoRA solution, demonstrating how retrieval and fine-tuning complement each other to improve both factual accuracy and task-specific behaviour.           |

---

| Requirement            | Status       | Implementation                                                                                                                                     |
| ---------------------- | ------------ | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| Prompting Comparison   | ✅ Completed | Documented the advantages, disadvantages, and appropriate use cases of prompting as a baseline AI approach.                                        |
| RAG Comparison         | ✅ Completed | Evaluated Retrieval-Augmented Generation, including its architecture, benefits, limitations, and recommended use cases.                            |
| Fine-Tuning Comparison | ✅ Completed | Compared LoRA fine-tuning, describing its purpose, strengths, limitations, and applicability to task-specific behaviour.                           |
| Hybrid Approach        | ✅ Completed | Evaluated a combined RAG + LoRA architecture and explained how it balances behavioural adaptation with external knowledge retrieval.               |
| Trade-off Analysis     | ✅ Completed | Compared implementation complexity, development cost, training requirements, knowledge updates, and response accuracy across all four approaches.  |
| Recommendation         | ✅ Completed | Recommended a hybrid RAG + LoRA solution based on the project's requirements for maintainability, factual accuracy, and specialised behaviour.     |
| Fine-Tuning Evaluation | ✅ Completed | Summarized the LoRA fine-tuning results, including the final training loss and the role of fine-tuning compared to Retrieval-Augmented Generation. |

# Module 6 – Tool Calling & MCP

## Improvements Implemented

| Improvement                | Description                                                                                                                                                                     |
| -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Schema Validation          | Added schema-level validation to `DivideSchema` using a Pydantic `field_validator` to prevent division by zero.                                                                 |
| Contract Testing           | Extended `test_contract.py` with negative validation tests to verify that invalid tool inputs correctly raise `ValidationError`.                                                |
| Project Cleanup            | Removed development and debugging artifacts (`test_mcp.py` and commented debug code in `server.py`) to improve project maintainability.                                         |
| Workflow State Persistence | Implemented persistent workflow state using `StateStore`, ensuring each workflow execution starts with a fresh state while saving the completed state to `workflow_state.json`. |

---

| Requirement | Status | Implementation || ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Tool Schema Validation | ✅ Completed | Implemented schema-level validation using a Pydantic `field_validator` to ensure invalid tool inputs, such as division by zero, are rejected before execution. |
| Contract Testing | ✅ Completed | Added positive and negative contract tests to validate tool schemas and verify that invalid inputs raise `ValidationError`. |
| MCP Cleanup | ✅ Completed | Removed temporary debugging files and commented debugging code to maintain a clean MCP implementation. |
| State Persistence | ✅ Completed | Implemented workflow state persistence using `StateStore`. Each workflow execution initializes a fresh state containing `task`, `plan`, `status`, `retrieved_context`, and `results`, then persists the completed workflow state to `workflow_state.json`. |

# Module 7 – Agentic Workflows & Multi-Agent Systems

## Improvements Implemented

| Improvement                   | Description                                                                                                                                     |
| ----------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| Workflow State Initialization | Updated `WorkflowEngine` to initialize a fresh workflow state for each execution, preventing stale workflow data from previous runs.            |
| LLM Dependency Injection      | Updated `run_workflow.py` and `main.py` to inject `SimpleLLM` into `WorkflowEngine`, preventing runtime errors caused by `llm=None`.            |
| Workflow State Persistence    | Continued using `StateStore` to persist the final workflow state to `workflow_state.json` after execution.                                      |
| Dynamic RAG Retrieval         | Updated executor agents to retrieve context using the current workflow task instead of a hardcoded query, making the workflow task-independent. |

---

| Requirement             | Status       | Implementation                                                                                                                                                                                               |
| ----------------------- | ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Two-Agent Workflow      | ✅ Completed | Implemented a planner–executor workflow using `WorkflowEngine`, where `PlannerAgent` generates an execution plan and `ExecutorAgent` (or `ExternalExecutorAgent`) executes each planned step sequentially.   |
| State Persistence       | ✅ Completed | Implemented workflow state persistence using `StateStore`. Each workflow execution starts with a fresh workflow state and saves the completed state to `workflow_state.json`.                                |
| Agent-to-Agent Boundary | ✅ Completed | Implemented interchangeable executor agents through WorkflowEngine, allowing the workflow to switch between a local and external executor implementation while preserving the overall workflow orchestration |
| Monitoring & Tracing    | ✅ Completed | Implemented structured workflow tracing using TraceLogger, recording workflow lifecycle events (workflow_start, planner_completed, executor_completed, and workflow_finished) in workflow_traces.log.        |

# Module 8 – Hardware Fundamentals (Performance Analysis)

## Improvements Implemented

| Improvement                  | Description                                                                                                                                           |
| ---------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| Real Latency Benchmark       | Replaced the simulated `time.sleep()` latency benchmark with real batched inference using the Phi-3 Mini model and measured actual execution latency. |
| Real Throughput Benchmark    | Replaced hardcoded throughput and TTFT values with measurements obtained from real model inference and execution timing.                              |
| Token Speed Benchmark        | Measured token generation speed across multiple context lengths using `model.generate()` on the Phi-3 Mini model.                                     |
| Benchmark Result Aggregation | Updated `report.py` to aggregate and display the measured outputs generated by the benchmark scripts instead of relying only on static text.          |

---

| Requirement                  | Status       | Implementation                                                                                                                                                                                   |
| ---------------------------- | ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Latency vs Batch Size        | ✅ Completed | Implemented real latency benchmarking by executing batched inference on the Phi-3 Mini model and measuring execution time for different batch sizes.                                             |
| Tokens/sec vs Context Length | ✅ Completed | Measured token generation speed across multiple context lengths using real model inference and execution timing.                                                                                 |
| Throughput vs TTFT           | ✅ Completed | Implemented real throughput and TTFT benchmarking using batched inference and calculated throughput from generated tokens and elapsed execution time.                                            |
| Performance Analysis         | ✅ Completed | Implemented an aggregated performance report that reads the benchmark outputs from all measurement scripts and summarizes the observed latency, throughput, TTFT, and context-length trade-offs. |

# Module 9 — Evaluation, Reliability & Safety (Capstone)

## Improvements Implemented

| Requirement               | Status | Implementation                                                                                                |
| ------------------------- | ------ | ------------------------------------------------------------------------------------------------------------- |
| RAG Regression Testing    | ✅     | Added automated regression tests validating grounded answers, expected sources and unknown-question handling. |
| Prompt Injection Testing  | ✅     | Added automated tests for instruction override, administrator privilege abuse and malicious prompt injection. |
| Agent Workflow Regression | ✅     | Replaced smoke test with assertion-based workflow validation.                                                 |
| Deterministic Evaluation  | ✅     | Evaluation mode now uses temperature=0 for reproducible outputs.                                              |

# 🧠 AI System Frontend (Angular) Overview

This frontend is an Angular-based UI that connects to an AI backend system to provide chat, structured responses, and context-aware interactions.

---

# 📁 Frontend Project Structure (Table Overview)

## 🗂️ Core Application Modules

| File / Module | Purpose | Description |
|--------------|---------|-------------|
| src/app/app.component.ts | Root Component | Main application shell |
| src/app/app.module.ts | App Module | Root Angular module configuration |
| src/app/services/ai.service.ts | AI Service | Handles HTTP requests to backend AI system |
| src/app/components/chat/ | Chat UI | Chat interface for user-AI interaction |
| src/app/components/message/ | Message Component | Displays individual chat messages |
| src/app/models/ | Data Models | TypeScript interfaces for API responses |

---

## 💬 Chat System

| File / Module | Purpose | Description |
|--------------|---------|-------------|
| chat.component.ts | Chat Controller | Manages user input and AI responses |
| chat.component.html | Chat UI Layout | Visual chat interface |
| chat.component.scss | Styling | UI design for chat system |
| message.component.ts | Message Renderer | Renders user and AI messages |

---

## 🤖 AI Integration Layer

| Layer | Module | Description |
|------|--------|-------------|
| Service Layer | ai.service.ts | Sends requests to backend AI API |
| HTTP Layer | HttpClient | Handles REST API communication |
| State Handling | RxJS Observables | Manages async AI responses |
| Environment Config | environment.ts | Stores API base URL and keys |

---

## 🧾 Data Models (Frontend Types)

| File | Purpose | Description |
|------|--------|-------------|
| message.model.ts | Chat Message | Defines structure of chat messages |
| ai-response.model.ts | AI Response | Defines structured AI output |
| chat-state.model.ts | State Model | Stores conversation state |

---

## 🎨 UI / Presentation Layer

| Module | Purpose | Description |
|--------|--------|-------------|
| Angular Components | UI Rendering | Displays chat interface |
| SCSS Styling | Design System | Controls layout and appearance |
| Angular Directives | UI Logic | Handles conditional rendering |
| Pipes | Data Formatting | Formats AI output for display |

---

## ⚙️ Configuration & Environment

| File | Purpose | Description |
|------|--------|-------------|
| environment.ts | Dev Config | Stores API URL and dev settings |
| environment.prod.ts | Production Config | Production API configuration |
| angular.json | Build Config | Angular build and asset settings |

---

# 🚀 How to Run Frontend

| Command | Purpose |
|--------|--------|
| npm install | Install dependencies |
| npm start | Run development server |
| ng serve | Alternative run command |
| http://localhost:4200 | Access application |

---

# 🔌 Backend Integration

| Feature | Description |
|--------|--------|
| REST API | Communicates with FastAPI backend |
| AI Chat Endpoint | Sends user prompts to `/chat` endpoint |
| Structured Output | Receives JSON responses (title, summary, tags) |
| Streaming (optional) | Supports token streaming responses |

---

# 🧠 Key Concepts (Frontend)

| Concept | Description |
|--------|--------|
| Component-based UI | Angular component architecture |
| Reactive programming | RxJS Observables for async AI calls |
| Service abstraction | AI logic separated from UI |
| State management | Local component + reactive streams |
| Environment config | Separate dev/prod API settings |
| API integration | HTTP communication with AI backend |

---

# 🧩 System Flow (Frontend → Backend)

| Step | Flow |
|------|------|
| 1 | User sends message in chat UI |
| 2 | Angular ChatComponent calls ai.service.ts |
| 3 | Service sends HTTP request to FastAPI backend |
| 4 | Backend processes via RAG / Agent system |
| 5 | Response returned (JSON structured AI output) |
| 6 | UI renders formatted response |

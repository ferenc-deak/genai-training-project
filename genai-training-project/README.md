# GenaiTrainingProject

Aplicație Angular care integrează un model AI pentru a oferi răspunsuri inteligente și structurate utilizatorului.

## Scop

Acest proiect demonstrează integrarea unui model GenAI într-o aplicație frontend folosind Angular și API calls.

Funcționalități:

- Chat AI
- Răspunsuri structurate (JSON)
- Context-based responses (mini RAG)

## Tehnologii

- Angular
- TypeScript
- OpenAI API (sau alt AI API)
- RxJS

## Setup

1. Clone repository:
   git clone https://github.com/username/genai-training-project.git

2. Install dependencies:
   npm install

3. Configure environment:
   Adaugă API key în:
   src/environments/environment.ts

4. Run:
   ng serve

Accesează: http://localhost:4200

## Configurare AI

Aplicația folosește un API AI extern.

Pentru rulare:

- adaugă API key în environment.ts
- modelul folosit: gpt-4o-mini (sau altul)

## Arhitectură

- ai.service.ts gestionează apelurile către API
- componentele UI afișează datele
- prompturile sunt definite pentru a obține răspunsuri structurate

## Prompturi

Prompturile utilizate sunt documentate în:
docs/prompts.md

Exemplu:
"Returnează răspunsul în JSON cu title, summary și tags"

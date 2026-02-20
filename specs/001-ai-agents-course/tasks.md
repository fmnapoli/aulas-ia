# Tasks: Curso Prático de Desenvolvimento de Agentes de IA

**Input**: Design documents from `/specs/001-ai-agents-course/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: Not explicitly requested in the specification. Test tasks not included.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization, root-level files, directory scaffolding

- [x] T001 Create root project file pyproject.toml with workspace config, shared dependencies (agno, google-genai, python-dotenv), and Python >=3.11 requirement
- [x] T002 Create .env.example at repository root with GOOGLE_API_KEY=your_key_here template
- [x] T003 [P] Create .gitignore at repository root (ignore .env, __pycache__, *.pyc, .venv, /tmp, *.db, /lancedb)
- [x] T004 [P] Create directory structure for all 10 lessons: aulas/aula-01-hello-agent/ through aulas/aula-10-projeto-final/ with assets/ subdirectory in each

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Root-level documentation and shared resources that ALL lessons depend on

**CRITICAL**: No lesson can be properly used until this phase is complete

- [x] T005 Create root README.md in Portuguese with: course overview, module/lesson table, prerequisites (Python 3.11+, uv, Gemini API key), quickstart instructions, and link to each lesson
- [x] T006 Create pyproject.toml in aulas/aula-01-hello-agent/ with dependencies: agno, google-genai, python-dotenv
- [x] T007 [P] Create pyproject.toml in aulas/aula-02-prompt-engineering/ with dependencies: agno, google-genai, python-dotenv
- [x] T008 [P] Create pyproject.toml in aulas/aula-03-tool-calling/ with dependencies: agno, google-genai, python-dotenv, duckduckgo-search
- [x] T009 [P] Create pyproject.toml in aulas/aula-04-react-agent/ with dependencies: agno, google-genai, python-dotenv, duckduckgo-search
- [x] T010 [P] Create pyproject.toml in aulas/aula-05-memory/ with dependencies: agno, google-genai, python-dotenv
- [x] T011 [P] Create pyproject.toml in aulas/aula-06-knowledge-rag/ with dependencies: agno, google-genai, python-dotenv, lancedb, tantivy
- [x] T012 [P] Create pyproject.toml in aulas/aula-07-planning/ with dependencies: agno, google-genai, python-dotenv, duckduckgo-search
- [x] T013 [P] Create pyproject.toml in aulas/aula-08-multi-agent-team/ with dependencies: agno, google-genai, python-dotenv, duckduckgo-search
- [x] T014 [P] Create pyproject.toml in aulas/aula-09-guardrails/ with dependencies: agno, google-genai, python-dotenv
- [x] T015 [P] Create pyproject.toml in aulas/aula-10-projeto-final/ with dependencies: agno, google-genai, python-dotenv, duckduckgo-search, lancedb, tantivy

**Checkpoint**: Project skeleton ready — lesson implementation can begin

---

## Phase 3: User Story 1 — Aluno Inicia e Conclui uma Aula Prática (Priority: P1) MVP

**Goal**: A student with Python 3.11+ and a free Gemini API key can complete a lesson autonomously in under 45 minutes, producing a working agent they can demonstrate.

**Independent Test**: Give Aula 01 to a junior developer — they should have a working agent in 30 minutes following only the README instructions.

### Aula 01: Olá, Agente!

- [x] T016 [US1] Write main.py in aulas/aula-01-hello-agent/main.py — basic Agent with Gemini(id="gemini-2.5-flash"), dotenv for GOOGLE_API_KEY loading, print_response with stream=True, markdown=True (~30 lines)
- [x] T017 [US1] Write README.md in aulas/aula-01-hello-agent/README.md following lesson contract template: objective (primeiro agente), concepts (Agent, Gemini, print_response), theory (o que é um LLM, o que é um agente, como funciona uma API), practice (step-by-step main.py walkthrough), troubleshooting (top 5 errors), challenge (mudar o prompt e observar diferenças)
- [x] T018 [US1] Create concept diagram in aulas/aula-01-hello-agent/assets/diagram.md — text-based diagram (Mermaid or ASCII) showing: User → Agent → LLM API → Response flow

### Aula 02: Prompt Engineering para Agentes

- [x] T019 [P] [US1] Write main.py in aulas/aula-02-prompt-engineering/main.py — Agent with instructions (system prompt), few-shot examples via instructions, Pydantic output_schema for structured output, demonstrate difference between with/without instructions (~60 lines)
- [x] T020 [P] [US1] Write README.md in aulas/aula-02-prompt-engineering/README.md — theory (system prompts, few-shot, structured output, Pydantic), concepts (instructions, output_schema, BaseModel, Field), practice, troubleshooting, challenge (criar seu próprio schema Pydantic)
- [x] T021 [P] [US1] Create concept diagram in aulas/aula-02-prompt-engineering/assets/diagram.md — text-based diagram showing: instructions → Agent → output_schema → Structured Response

**Checkpoint**: MVP complete — 2 fully functional lessons proving the student experience works. Validate by running both lessons end-to-end.

---

## Phase 4: User Story 2 — Aluno Constrói Agente Multi-Tool Completo (Priority: P2)

**Goal**: The student progresses from simple Agent to complex multi-agent Team across lessons 03-10, building increasingly powerful agents until the final project: a research assistant with Team orchestration.

**Independent Test**: After completing all lessons, the student can run the Aula 10 project final and get a structured research report from the Team of agents.

### Aula 03: Tool Calling

- [x] T022 [US2] Write tools.py in aulas/aula-03-tool-calling/tools.py — custom calculator tool using @tool decorator, demonstrating docstring as tool description, typed parameters (~20 lines)
- [x] T023 [US2] Write main.py in aulas/aula-03-tool-calling/main.py — Agent with tools=[DuckDuckGoTools(), calculator], demonstrate tool invocation with web search + calculation (~40 lines)
- [x] T024 [US2] Write README.md in aulas/aula-03-tool-calling/README.md — theory (function calling, tool descriptions, how LLMs select tools), concepts (tools, @tool, Toolkit, DuckDuckGoTools), practice, troubleshooting, challenge (criar um Toolkit customizado)
- [x] T025 [US2] Create concept diagram in aulas/aula-03-tool-calling/assets/diagram.md — User → Agent → Tool Selection → Tool Execution → Response

### Aula 04: Agente ReAct

- [x] T026 [P] [US2] Write main.py in aulas/aula-04-react-agent/main.py — Agent with ReasoningTools(add_instructions=True) + DuckDuckGoTools(), show_full_reasoning=True to visualize Think→Act→Observe loop (~40 lines)
- [x] T027 [P] [US2] Write README.md in aulas/aula-04-react-agent/README.md — theory (ReAct paper, Think→Act→Observe cycle, why reasoning improves tool use), concepts (ReasoningTools, reasoning, show_full_reasoning), practice, troubleshooting, challenge (comparar output com/sem ReasoningTools)
- [x] T028 [P] [US2] Create concept diagram in aulas/aula-04-react-agent/assets/diagram.md — ReAct loop: Think → Act → Observe → Think (repeat)

### Aula 05: Memory

- [x] T029 [P] [US2] Write main.py in aulas/aula-05-memory/main.py — Agent with SqliteDb(db_file="memory.db"), add_history_to_context=True, update_memory_on_run=True, demonstrate 3 sequential interactions with session_id showing memory persistence (~50 lines)
- [x] T030 [P] [US2] Write README.md in aulas/aula-05-memory/README.md — theory (short-term vs long-term memory, session persistence, fact extraction), concepts (SqliteDb, add_history_to_context, update_memory_on_run, session_id, user_id), practice, troubleshooting, challenge (usar learning=True para perfil automático)
- [x] T031 [P] [US2] Create concept diagram in aulas/aula-05-memory/assets/diagram.md — Agent ↔ SqliteDb: session history + extracted memories

### Aula 06: Knowledge + RAG

- [x] T032 [P] [US2] Create sample documents in aulas/aula-06-knowledge-rag/docs/ — 2-3 small markdown files about a specific topic (ex: receitas brasileiras, guia de Python) for the agent to query
- [x] T033 [US2] Write main.py in aulas/aula-06-knowledge-rag/main.py — Knowledge with LanceDb(uri="tmp/lancedb", embedder=GeminiEmbedder()), insert docs from docs/ directory, Agent with knowledge=knowledge and search_knowledge=True, query the knowledge base (~60 lines)
- [x] T034 [US2] Write README.md in aulas/aula-06-knowledge-rag/README.md — theory (embeddings, vector databases, RAG pipeline, chunking), concepts (Knowledge, GeminiEmbedder, LanceDb, PDFReader, search_knowledge), practice, troubleshooting, challenge (adicionar um PDF próprio como knowledge)
- [x] T035 [US2] Create concept diagram in aulas/aula-06-knowledge-rag/assets/diagram.md — RAG pipeline: Documents → Embeddings → VectorDB → Query → Relevant Chunks → Agent → Response

### Aula 07: Planejamento e Decomposição

- [x] T036 [P] [US2] Write main.py in aulas/aula-07-planning/main.py — Agent with reasoning=True and tools=[DuckDuckGoTools()], demonstrate multi-step task decomposition (ex: "Pesquise 3 frameworks de agentes e compare") showing planning before execution (~50 lines)
- [x] T037 [P] [US2] Write README.md in aulas/aula-07-planning/README.md — theory (task decomposition, chain-of-thought, planning strategies), concepts (reasoning=True, multi-step tool chaining), practice, troubleshooting, challenge (tarefa complexa com 5+ subtarefas)
- [x] T038 [P] [US2] Create concept diagram in aulas/aula-07-planning/assets/diagram.md — Complex Task → Plan (subtasks) → Execute each → Synthesize results

### Aula 08: Team (Multi-Agent)

- [x] T039 [US2] Write main.py in aulas/aula-08-multi-agent-team/main.py — create 2-3 specialized Agents (news_agent with HackerNewsTools, finance_agent with YFinanceTools or DuckDuckGoTools), Team with TeamMode.coordinate, demonstrate delegation and synthesis (~60 lines)
- [x] T040 [US2] Write README.md in aulas/aula-08-multi-agent-team/README.md — theory (multi-agent architectures, coordinator pattern, delegation, team modes), concepts (Team, TeamMode, members, coordinate/route/broadcast), practice, troubleshooting, challenge (criar Team com TeamMode.route)
- [x] T041 [US2] Create concept diagram in aulas/aula-08-multi-agent-team/assets/diagram.md — Team Leader → delegates to Agent 1, Agent 2, Agent 3 → synthesizes results

### Aula 09: Guardrails e Segurança

- [x] T042 [P] [US2] Write guardrails.py in aulas/aula-09-guardrails/guardrails.py — custom guardrail extending BaseGuardrail that blocks specific topics or validates input length (~30 lines)
- [x] T043 [US2] Write main.py in aulas/aula-09-guardrails/main.py — Agent with pre_hooks=[PIIDetectionGuardrail(), CustomGuardrail()], demonstrate blocked input + allowed input, show error handling with InputCheckError (~50 lines)
- [x] T044 [US2] Write README.md in aulas/aula-09-guardrails/README.md — theory (AI safety, input validation, output filtering, PII protection, prompt injection), concepts (pre_hooks, PIIDetectionGuardrail, PromptInjectionGuardrail, BaseGuardrail, InputCheckError, CheckTrigger), practice, troubleshooting, challenge (criar guardrail de output)
- [x] T045 [US2] Create concept diagram in aulas/aula-09-guardrails/assets/diagram.md — Input → Pre-hooks (guardrails) → Agent → Post-hooks → Output

### Aula 10: Projeto Final — Assistente de Pesquisa

- [x] T046 [US2] Write agents/researcher.py in aulas/aula-10-projeto-final/agents/researcher.py — Agent "Researcher" with DuckDuckGoTools(), role of searching web for sources on a given topic (~20 lines)
- [x] T047 [P] [US2] Write agents/analyst.py in aulas/aula-10-projeto-final/agents/analyst.py — Agent "Analyst" with Knowledge(LanceDb + GeminiEmbedder), role of analyzing and cross-referencing sources (~25 lines)
- [x] T048 [P] [US2] Write agents/writer.py in aulas/aula-10-projeto-final/agents/writer.py — Agent "Writer" with instructions to produce structured Markdown reports, output_schema for ReportSection (~20 lines)
- [x] T049 [US2] Write main.py in aulas/aula-10-projeto-final/main.py — Team(name="Research Assistant", model=Gemini(...), members=[researcher, analyst, writer], mode=TeamMode.coordinate), demonstrate end-to-end: user gives topic → Team researches, analyzes, writes report (~40 lines)
- [x] T050 [US2] Write README.md in aulas/aula-10-projeto-final/README.md — theory (putting it all together: Team + Knowledge + Tools + Guardrails), concepts review (all Agno concepts learned), practice (run the complete assistant), troubleshooting, challenge (adicionar 4o agente "Reviewer" ao Team)
- [x] T051 [US2] Create concept diagram in aulas/aula-10-projeto-final/assets/diagram.md — Full system: User → Team Leader → Researcher (web) + Analyst (knowledge) + Writer (report) → Structured Report

**Checkpoint**: Full course progression complete. Validate by running Aula 10 end-to-end — the Team should produce a structured research report.

---

## Phase 5: User Story 3 — Instrutor Adapta o Conteúdo (Priority: P3)

**Goal**: An instructor can select individual lessons for workshops, understand dependencies, and adapt examples for their organization.

**Independent Test**: An instructor selects 3 lessons for a half-day workshop and verifies they work independently.

- [x] T052 [US3] Update root README.md to include module dependency matrix: table showing which lessons depend on which, and which can be taken independently
- [x] T053 [P] [US3] Add "Pré-requisitos" section to every README.md (aulas/aula-01 through aulas/aula-10) listing exact lesson dependencies from data-model.md dependency graph
- [x] T054 [P] [US3] Add "Próxima Aula" section to every README.md (aulas/aula-01 through aulas/aula-09) linking to the next lesson with a brief preview

**Checkpoint**: An instructor can pick any subset of lessons and know exactly what's needed.

---

## Phase 6: Polish & Cross-Cutting Concerns

**Purpose**: Quality improvements across all lessons

- [ ] T055 Validate all 10 lessons execute successfully: run `uv sync && uv run python main.py` in each aulas/aula-XX directory
- [ ] T056 [P] Review all README.md files for consistent formatting per lesson contract template in specs/001-ai-agents-course/contracts/lesson-contract.md
- [x] T057 [P] Verify all pyproject.toml files have correct dependencies by checking imports in each main.py
- [ ] T058 Run quickstart.md validation: follow specs/001-ai-agents-course/quickstart.md from scratch and verify complete flow works

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies — can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion — BLOCKS all lessons
- **US1 (Phase 3)**: Depends on Foundational — produces MVP (Aulas 01-02)
- **US2 (Phase 4)**: Depends on Foundational — can start in parallel with US1 for Aulas 03+ but Aula 04 depends on Aula 03, Aula 07 depends on 03+04, Aula 10 depends on all
- **US3 (Phase 5)**: Depends on US1 + US2 completion (needs all READMEs to exist)
- **Polish (Phase 6)**: Depends on all stories being complete

### Lesson Dependencies (from data-model.md)

```text
Aula 01 (no deps) ──┬── Aula 02 (deps: 01)
                     ├── Aula 03 (deps: 01) ──┬── Aula 04 (deps: 03)
                     │                        ├── Aula 07 (deps: 03, 04)
                     │                        └── Aula 08 (deps: 03)
                     ├── Aula 05 (deps: 01)
                     ├── Aula 06 (deps: 01)
                     └── Aula 09 (deps: 01)

All ────── Aula 10 (deps: all)
```

### Within Each Lesson

1. pyproject.toml (already created in Phase 2)
2. Custom modules (tools.py, guardrails.py, agents/) if needed
3. main.py (depends on custom modules)
4. README.md (depends on main.py being finalized)
5. Diagram (can be parallel with README)

### Parallel Opportunities

Within Phase 2 (pyproject.toml files): T007-T015 are all [P] — 9 tasks in parallel

Within Phase 4 (lessons), these groups can run in parallel:
- **Group A**: Aulas 02, 05, 06, 09 (all depend only on Aula 01)
- **Group B**: Aulas 03 → 04 → 07 (sequential chain)
- **Group C**: Aula 08 (depends on 03 only)
- **Group D**: Aula 10 (depends on all — must be last)

---

## Parallel Example: Phase 2 (pyproject.toml creation)

```text
# All 9 pyproject.toml files can be created simultaneously:
Task: T007 "Create pyproject.toml in aulas/aula-02-prompt-engineering/"
Task: T008 "Create pyproject.toml in aulas/aula-03-tool-calling/"
Task: T009 "Create pyproject.toml in aulas/aula-04-react-agent/"
Task: T010 "Create pyproject.toml in aulas/aula-05-memory/"
Task: T011 "Create pyproject.toml in aulas/aula-06-knowledge-rag/"
Task: T012 "Create pyproject.toml in aulas/aula-07-planning/"
Task: T013 "Create pyproject.toml in aulas/aula-08-multi-agent-team/"
Task: T014 "Create pyproject.toml in aulas/aula-09-guardrails/"
Task: T015 "Create pyproject.toml in aulas/aula-10-projeto-final/"
```

## Parallel Example: Phase 4 Group A (independent lessons)

```text
# Aulas that depend only on Aula 01 can start simultaneously:
Task: T019-T021 "Aula 02: Prompt Engineering"
Task: T029-T031 "Aula 05: Memory"
Task: T032-T035 "Aula 06: Knowledge + RAG"
Task: T042-T045 "Aula 09: Guardrails"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup (T001-T004)
2. Complete Phase 2: Foundational (T005-T015)
3. Complete Phase 3: User Story 1 — Aulas 01 + 02 (T016-T021)
4. **STOP and VALIDATE**: Run both lessons end-to-end with a fresh Gemini API key
5. Demo/share if ready — course already delivers value with 2 functional lessons

### Incremental Delivery

1. Setup + Foundational → Skeleton ready
2. Aulas 01-02 → MVP! Student can learn Agent basics + Prompt Engineering
3. Aulas 03-04 → Add tool-calling + ReAct (builds on fundamentals)
4. Aulas 05-06 → Add memory + RAG (independent from 03-04)
5. Aulas 07-08 → Add planning + multi-agent (requires 03-04)
6. Aulas 09-10 → Add guardrails + project final (capstone)
7. US3 + Polish → Instructor-ready, validated

### Parallel Team Strategy

With 3 developers after Phase 2:
- **Dev A**: Aulas 01, 02, 03, 04, 07 (sequential dependency chain)
- **Dev B**: Aulas 05, 06, 08 (independent from Dev A after Aula 01)
- **Dev C**: Aulas 09, 10 (Aula 09 independent, Aula 10 last after all others)

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- All main.py files MUST load GOOGLE_API_KEY via dotenv
- All main.py files MUST use Gemini(id="gemini-2.5-flash") as default model
- All README.md files MUST follow lesson contract template
- Code in English, text in Portuguese
- Diagrams use text-based format (Mermaid or ASCII) — no image generation needed
- Commit after each completed lesson (main.py + README.md + diagram)

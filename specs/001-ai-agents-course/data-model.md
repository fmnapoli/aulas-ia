# Data Model: Curso Prático de Desenvolvimento de Agentes de IA

**Date**: 2026-02-19  
**Feature**: `001-ai-agents-course`

## Overview

Este projeto é um curso educacional (não uma aplicação de software), então o "data model" descreve a estrutura do conteúdo e os artefatos Agno produzidos, não um schema de banco de dados.

## Entity: Módulo (Module)

Agrupamento temático de aulas.

| Atributo | Tipo | Descrição |
|----------|------|-----------|
| number | int | Número sequencial (1-5) |
| title | str | Nome do módulo (ex: "Fundamentos") |
| lessons | list[Lesson] | 2-3 aulas pertencentes ao módulo |

### Instâncias

| # | Título | Aulas |
|---|--------|-------|
| 1 | Fundamentos | 01, 02 |
| 2 | Ferramentas e Ações | 03, 04 |
| 3 | Memória e Contexto | 05, 06 |
| 4 | Orquestração Avançada | 07, 08 |
| 5 | Produção e Projeto Final | 09, 10 |

## Entity: Aula (Lesson)

Unidade de aprendizado independente.

| Atributo | Tipo | Descrição |
|----------|------|-----------|
| number | int | Número sequencial (01-10) |
| slug | str | Identificador do diretório (ex: "aula-01-hello-agent") |
| title | str | Título curto em português |
| objective | str | O que o aluno aprende/constrói |
| agno_concepts | list[str] | Conceitos Agno introduzidos (ex: ["Agent", "Gemini"]) |
| dependencies | list[int] | Aulas pré-requisito (ex: [1, 2]) |
| estimated_time | int | Minutos estimados (max 45) |
| artifact | str | Descrição do artefato produzido |

### Instâncias

| # | Slug | Título | Conceitos Agno | Deps | Artefato |
|---|------|--------|----------------|------|----------|
| 01 | aula-01-hello-agent | Olá, Agente! | Agent, Gemini, print_response | — | Agente conversacional simples |
| 02 | aula-02-prompt-engineering | Prompt Engineering | instructions, output_schema, Pydantic | 01 | Agente com structured output |
| 03 | aula-03-tool-calling | Tool Calling | tools, @tool, Toolkit, DuckDuckGoTools | 01 | Agente com busca web + calculadora |
| 04 | aula-04-react-agent | Agente ReAct | ReasoningTools, reasoning, show_full_reasoning | 03 | Agente que raciocina antes de agir |
| 05 | aula-05-memory | Memory | SqliteDb, add_history_to_context, update_memory_on_run, session_id | 01 | Agente com memória persistente |
| 06 | aula-06-knowledge-rag | Knowledge + RAG | Knowledge, GeminiEmbedder, LanceDb, PDFReader, search_knowledge | 01 | Agente que consulta documentos |
| 07 | aula-07-planning | Planejamento | reasoning=True, tool chaining, multi-step | 03, 04 | Agente que decompõe tarefas |
| 08 | aula-08-multi-agent-team | Team (Multi-Agent) | Team, TeamMode, members, coordinate | 03 | Team de agentes especializados |
| 09 | aula-09-guardrails | Guardrails | pre_hooks, PIIDetectionGuardrail, BaseGuardrail, InputCheckError | 01 | Agente com validação de I/O |
| 10 | aula-10-projeto-final | Projeto Final | Team, Knowledge, Tools, DuckDuckGoTools | all | Assistente de pesquisa completo |

## Entity: Artefato Agno por Aula

Mapeamento entre aula e os constructs Agno utilizados.

### Aula 01 — Agent básico
```python
Agent(model=Gemini(id="gemini-2.0-flash"), markdown=True)
```

### Aula 02 — Structured Output
```python
Agent(model=Gemini(...), instructions="...", output_schema=MyModel)
```

### Aula 03 — Tools
```python
Agent(model=Gemini(...), tools=[DuckDuckGoTools(), calculator])
```

### Aula 04 — ReAct
```python
Agent(model=Gemini(...), tools=[ReasoningTools(add_instructions=True), DuckDuckGoTools()])
```

### Aula 05 — Memory
```python
Agent(model=Gemini(...), db=SqliteDb(db_file="memory.db"), add_history_to_context=True, update_memory_on_run=True)
```

### Aula 06 — Knowledge/RAG
```python
knowledge = Knowledge(vector_db=LanceDb(uri="/tmp/lancedb", table_name="docs", embedder=GeminiEmbedder()))
Agent(model=Gemini(...), knowledge=knowledge, search_knowledge=True)
```

### Aula 07 — Planning
```python
Agent(model=Gemini(...), reasoning=True, tools=[DuckDuckGoTools(), ...])
```

### Aula 08 — Team
```python
Team(name="...", model=Gemini(...), members=[agent1, agent2], mode=TeamMode.coordinate)
```

### Aula 09 — Guardrails
```python
Agent(model=Gemini(...), pre_hooks=[PIIDetectionGuardrail(), CustomGuardrail()])
```

### Aula 10 — Projeto Final (Team + Knowledge + Tools)
```python
researcher = Agent(name="Researcher", tools=[DuckDuckGoTools()])
analyst = Agent(name="Analyst", knowledge=knowledge, search_knowledge=True)
writer = Agent(name="Writer", instructions="Write structured reports")
team = Team(name="Research Assistant", model=Gemini(...), members=[researcher, analyst, writer], mode=TeamMode.coordinate)
```

## Grafo de Dependências entre Aulas

```text
01 ──┬── 02
     ├── 03 ──┬── 04
     │        ├── 07
     │        └── 08
     ├── 05
     ├── 06
     └── 09

All ────── 10 (Projeto Final)
```

## Estado / Lifecycle

O curso não tem estados de aplicação. O "lifecycle" é a progressão do aluno:

```text
Setup (instalar Python, obter API key)
  → Módulo 1 (fundamentos)
    → Módulo 2 (tools)
      → Módulo 3 (memória/knowledge)
        → Módulo 4 (orquestração)
          → Módulo 5 (guardrails + projeto final)
```

Cada aula é auto-contida (pode ser executada isoladamente se dependências estiverem satisfeitas).

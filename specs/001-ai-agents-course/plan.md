# Implementation Plan: Curso Prático de Desenvolvimento de Agentes de IA

**Branch**: `001-ai-agents-course` | **Date**: 2026-02-19 | **Spec**: [spec.md](./spec.md)
**Input**: Feature specification from `/specs/001-ai-agents-course/spec.md`

## Summary

Curso de 10 aulas práticas que ensina desenvolvimento de agentes de IA usando Agno (framework Python open-source) com Google Gemini como LLM padrão. Cada aula produz um agente funcional, progredindo de conceitos básicos (Agent conversacional) até sistemas multi-agente (Team com orquestração). Projeto final: assistente de pesquisa com Team de agentes especializados.

## Technical Context

**Language/Version**: Python 3.11+  
**Primary Dependencies**: agno (framework de agentes), google-genai (Gemini API client), pydantic (structured output)  
**Storage**: SQLite via `agno.db.sqlite` (persistência de sessões e memória)  
**Testing**: pytest (validação dos exemplos de cada aula)  
**Target Platform**: Local (terminal/CLI), qualquer OS com Python  
**Project Type**: Monorepo educacional — cada aula é um diretório independente com código e README  
**Performance Goals**: N/A (curso educacional, não aplicação de produção)  
**Constraints**: Free tier do Gemini API (rate limits), sem GPU, sem Docker, sem deploy  
**Scale/Scope**: 10 aulas, ~50-100 linhas de código Python por aula, 1 agente funcional por aula

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

Sem constitution definida (`.specify/memory/constitution.md` não existe). Gate passa automaticamente — nenhuma restrição de projeto registrada. Recomenda-se criar constitution futuramente para governar padrões de código e estrutura do curso.

## Project Structure

### Documentation (this feature)

```text
specs/001-ai-agents-course/
├── plan.md              # This file
├── research.md          # Phase 0 output
├── data-model.md        # Phase 1 output
├── quickstart.md        # Phase 1 output
├── contracts/           # Phase 1 output (N/A — não é API)
└── tasks.md             # Phase 2 output (/speckit.tasks command)
```

### Source Code (repository root)

```text
aulas/
├── aula-01-hello-agent/
│   ├── README.md            # Explicação teórica + instruções (PT)
│   ├── main.py              # Exemplo prático completo (EN)
│   ├── pyproject.toml       # Dependências da aula
│   └── assets/              # Diagramas e ilustrações
│       └── diagram.png
├── aula-02-prompt-engineering/
│   ├── README.md
│   ├── main.py
│   ├── pyproject.toml
│   └── assets/
├── aula-03-tool-calling/
│   ├── README.md
│   ├── main.py
│   ├── tools.py             # Custom tools (aulas que definem tools)
│   ├── pyproject.toml
│   └── assets/
├── aula-04-react-agent/
│   ├── README.md
│   ├── main.py
│   ├── pyproject.toml
│   └── assets/
├── aula-05-memory/
│   ├── README.md
│   ├── main.py
│   ├── pyproject.toml
│   └── assets/
├── aula-06-knowledge-rag/
│   ├── README.md
│   ├── main.py
│   ├── docs/                # Documentos de exemplo para RAG
│   ├── pyproject.toml
│   └── assets/
├── aula-07-planning/
│   ├── README.md
│   ├── main.py
│   ├── pyproject.toml
│   └── assets/
├── aula-08-multi-agent-team/
│   ├── README.md
│   ├── main.py
│   ├── pyproject.toml
│   └── assets/
├── aula-09-guardrails/
│   ├── README.md
│   ├── main.py
│   ├── guardrails.py        # Custom guardrails
│   ├── pyproject.toml
│   └── assets/
└── aula-10-projeto-final/
    ├── README.md
    ├── main.py
    ├── agents/              # Agentes especializados do Team
    │   ├── researcher.py
    │   ├── analyst.py
    │   └── writer.py
    ├── pyproject.toml
    └── assets/

pyproject.toml               # Raiz — dependências compartilhadas + workspace
README.md                    # Visão geral do curso (PT)
.env.example                 # Template para GOOGLE_API_KEY
```

**Structure Decision**: Monorepo com diretórios independentes por aula. Cada aula é auto-contida com seu próprio `pyproject.toml` para que alunos possam executar qualquer aula isoladamente. Um `pyproject.toml` raiz opcional para quem quiser instalar tudo de uma vez.

## Complexity Tracking

Nenhuma violação de constitution a justificar.

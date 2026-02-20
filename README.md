# Curso Prático de Desenvolvimento de Agentes de IA

Aprenda a construir agentes de IA do zero usando **Agno** e **Google Gemini** — do primeiro "Olá, Agente!" até um sistema multi-agente completo.

## O que você vai aprender

| Módulo | Aula | Tema | Conceitos Agno |
|--------|------|------|----------------|
| 1. Fundamentos | 01 | Olá, Agente! | Agent, Gemini, print_response |
| | 02 | Prompt Engineering | instructions, output_schema, Pydantic |
| 2. Ferramentas | 03 | Tool Calling | tools, @tool, DuckDuckGoTools |
| | 04 | Agente ReAct | ReasoningTools, reasoning |
| 3. Memória | 05 | Memory | SqliteDb, session_id, update_memory_on_run |
| | 06 | Knowledge + RAG | Knowledge, GeminiEmbedder, LanceDb |
| 4. Orquestração | 07 | Planejamento | reasoning=True, multi-step |
| | 08 | Multi-Agent Team | Team, TeamMode, coordinate |
| 5. Produção | 09 | Guardrails | pre_hooks, BaseGuardrail |
| | 10 | Projeto Final | Team + Knowledge + Tools |

## Pré-requisitos

- **Python 3.11+** ([python.org](https://python.org))
- **uv** (gerenciador de pacotes): `curl -LsSf https://astral.sh/uv/install.sh | sh`
- **API Key do Google Gemini** (gratuita, sem cartão): [aistudio.google.com/apikey](https://aistudio.google.com/apikey)

## Início Rápido

```bash
# 1. Clone o repositório
git clone https://github.com/fmnapoli/aulas-ia.git
cd aulas-ia

# 2. Configure sua API key
cp .env.example .env
# Edite .env e coloque sua GOOGLE_API_KEY

# 3. Execute a primeira aula
cd aulas/aula-01-hello-agent
uv sync
uv run python main.py
```

## Estrutura do Repositório

```
aulas-ia/
├── README.md              # Este arquivo
├── .env.example           # Template para API key
├── pyproject.toml         # Dependências compartilhadas
└── aulas/
    ├── aula-01-hello-agent/
    │   ├── README.md      # Teoria + instruções (PT)
    │   ├── main.py        # Código do exemplo (EN)
    │   └── pyproject.toml # Dependências da aula
    ├── aula-02-prompt-engineering/
    ├── ...
    └── aula-10-projeto-final/
```

Cada aula é **auto-contida** — pode ser executada independentemente (respeitando as dependências abaixo).

## Dependências entre Aulas

| Aula | Depende de | Pode ser feita isoladamente? |
|------|-----------|-------------------------------|
| 01 — Olá, Agente! | — | Sim |
| 02 — Prompt Engineering | 01 | Sim (com conhecimento básico de Agent) |
| 03 — Tool Calling | 01 | Sim (com conhecimento básico de Agent) |
| 04 — Agente ReAct | 03 | Precisa entender tool calling |
| 05 — Memory | 01 | Sim (com conhecimento básico de Agent) |
| 06 — Knowledge + RAG | 01 | Sim (com conhecimento básico de Agent) |
| 07 — Planejamento | 03, 04 | Precisa entender tools + ReAct |
| 08 — Multi-Agent Team | 03 | Precisa entender tool calling |
| 09 — Guardrails | 01 | Sim (com conhecimento básico de Agent) |
| 10 — Projeto Final | Todas | Capstone — usa todos os conceitos |

> **Para instrutores**: As aulas 02, 03, 05, 06 e 09 dependem apenas da Aula 01, permitindo montar workshops com subconjuntos do curso.

## Formato de Cada Aula

- **Teoria** (~15 min de leitura) — conceitos explicados com diagramas
- **Prática** (~30 min) — exemplo completo que produz um agente funcional
- **Desafio** (opcional) — exercício extra para quem quer ir além
- **Troubleshooting** — soluções para os erros mais comuns

## Custo

| Item | Custo |
|------|-------|
| Python + uv | Gratuito |
| Google Gemini API (free tier) | Gratuito |
| Total do curso | **$0 - $5** |

## Tecnologias

- [Agno](https://agno.com) — Framework open-source para agentes de IA
- [Google Gemini](https://aistudio.google.com) — LLM com free tier generoso
- [LanceDb](https://lancedb.com) — Vector database local (para RAG)

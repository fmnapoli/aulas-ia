# Research: Curso Prático de Desenvolvimento de Agentes de IA

**Date**: 2026-02-19  
**Feature**: `001-ai-agents-course`

## R1: Framework Principal — Agno

**Decision**: Agno (https://agno.com) como framework único para todas as aulas.

**Rationale**: Framework open-source Python com API concisa e cobertura completa dos conceitos do curso: Agent, Team, Workflow, Memory, Knowledge, Tools, Guardrails, Reasoning. Suporte nativo a Google Gemini. Performance superior a alternativas (529x mais rápido que LangGraph na instanciação de agentes).

**Alternatives considered**:
- LangChain/LangGraph: API mais verbosa, curva de aprendizado maior, overhead desnecessário para um curso introdutório
- CrewAI: Focado em multi-agent mas API menos flexível para ensinar conceitos individuais
- OpenAI Agents SDK: Acoplado ao OpenAI, sem suporte nativo a Gemini
- Raw SDK calls: Muito código boilerplate, alunos gastariam tempo em infraestrutura em vez de conceitos

## R2: LLM Provider — Google Gemini via Google AI API

**Decision**: Google Gemini (gemini-2.5-flash) direto via Google AI API com `GOOGLE_API_KEY`.

**Rationale**: Free tier generoso sem cartão de crédito. Qualidade suficiente para todos os exercícios. Agno tem suporte nativo: `from agno.models.google import Gemini`.

**Alternatives considered**:
- OpenAI: Requer cartão de crédito, custo mais alto
- OpenRouter: Intermediário desnecessário, adiciona complexidade
- Groq: Modelos open-source com outputs menos consistentes
- Ollama: Fora de escopo (requer hardware potente)

**Configuração Agno**:
```python
from agno.models.google import Gemini
model = Gemini(id="gemini-2.5-flash")
```

## R3: Embeddings para RAG (Aula 06) — GeminiEmbedder

**Decision**: Usar `GeminiEmbedder` do Agno para embeddings, mantendo tudo no ecossistema Google/Gemini.

**Rationale**: Evita dependência adicional de API (OpenAI). Usa a mesma `GOOGLE_API_KEY`. Aluno precisa de apenas uma conta/key para todo o curso.

**Alternatives considered**:
- OpenAIEmbedder: Requer API key separada, custo adicional
- OllamaEmbedder: Requer Ollama local, fora de escopo

**Configuração Agno**:
```python
from agno.knowledge.embedder.google import GeminiEmbedder
embedder = GeminiEmbedder()
```

## R4: Vector Database para RAG (Aula 06) — LanceDb

**Decision**: LanceDb como vector database (armazenamento local em arquivo).

**Rationale**: Zero setup — não requer servidor, container Docker, ou serviço cloud. Funciona com arquivos locais (`uri="/tmp/lancedb"`). Ideal para ambiente educacional onde simplicidade é prioridade.

**Alternatives considered**:
- PgVector: Requer PostgreSQL rodando (Docker ou instalação), complexo demais para uma aula
- ChromaDb: Opção viável mas LanceDb é mais leve e nativamente suportado
- Pinecone/Weaviate: SaaS, fora de escopo

**Configuração Agno**:
```python
from agno.vectordb.lancedb import LanceDb
vector_db = LanceDb(table_name="docs", uri="/tmp/lancedb")
```

## R5: Persistência de Sessão/Memória (Aula 05) — SqliteDb

**Decision**: SqliteDb do Agno para persistência de sessões e memória conversacional.

**Rationale**: Arquivo local, zero setup, built-in no Agno. Perfeito para demonstrar persistência sem infraestrutura.

**Configuração Agno**:
```python
from agno.db.sqlite import SqliteDb
db = SqliteDb(db_file="agent.db")
```

**Parâmetros de memória no Agent**:
| Parâmetro | Tipo | Uso |
|-----------|------|-----|
| `db` | `SqliteDb` | Backend de armazenamento |
| `add_history_to_context` | `bool` | Incluir histórico no prompt |
| `num_history_runs` | `int` | Quantas interações anteriores incluir |
| `update_memory_on_run` | `bool` | Extrair e armazenar fatos automaticamente |
| `learning` | `bool` | Extração automática de perfil do usuário |

## R6: Padrão ReAct (Aula 04) — ReasoningTools

**Decision**: Usar `ReasoningTools` do Agno para implementar o padrão ReAct (Reason + Act).

**Rationale**: Agno oferece 3 abordagens para reasoning:
1. `reasoning=True` — Chain-of-Thought estruturado (mais simples)
2. `ReasoningTools` — padrão ReAct com tools `think()` e `analyze()` (mais didático)
3. `reasoning_model` — modelo dedicado para reasoning

Para a Aula 04, usar `ReasoningTools` é o mais didático porque torna o ciclo Think → Act → Observe explícito e visível.

**Configuração Agno**:
```python
from agno.tools.reasoning import ReasoningTools
agent = Agent(
    model=Gemini(id="gemini-2.5-flash"),
    tools=[ReasoningTools(add_instructions=True)],
    show_full_reasoning=True,
)
```

## R7: Multi-Agent / Team (Aula 08) — Team com TeamMode

**Decision**: Usar `Team` do Agno com `TeamMode.coordinate` como modo principal.

**Rationale**: O modo `coordinate` é o mais didático — mostra decomposição, delegação e síntese. Modos disponíveis:

| Modo | Comportamento |
|------|---------------|
| `TeamMode.coordinate` | Líder decompõe, delega, sintetiza (padrão) |
| `TeamMode.route` | Líder roteia para um especialista |
| `TeamMode.broadcast` | Envia para todos, sintetiza |
| `TeamMode.tasks` | Loop iterativo de tarefas até conclusão |

**Configuração Agno**:
```python
from agno.team import Team
from agno.team.mode import TeamMode

team = Team(
    name="Research Team",
    model=Gemini(id="gemini-2.5-flash"),
    members=[agent1, agent2, agent3],
    mode=TeamMode.coordinate,
    instructions="Coordinate research and synthesize findings.",
)
```

## R8: Guardrails (Aula 09) — Built-in + Custom

**Decision**: Demonstrar guardrails built-in do Agno + criação de custom guardrails.

**Rationale**: Agno tem guardrails nativos (`PIIDetectionGuardrail`, `PromptInjectionGuardrail`) que funcionam como pre-hooks. Custom guardrails via `BaseGuardrail` permitem ensinar o conceito de validação.

**Configuração Agno**:
```python
# Built-in
from agno.guardrails import PIIDetectionGuardrail, PromptInjectionGuardrail
agent = Agent(pre_hooks=[PIIDetectionGuardrail(), PromptInjectionGuardrail()])

# Custom
from agno.guardrails import BaseGuardrail
from agno.exceptions import InputCheckError, CheckTrigger
from agno.run.agent import RunInput

class CustomGuardrail(BaseGuardrail):
    def check(self, run_input: RunInput) -> None:
        # validation logic
        pass
    async def async_check(self, run_input: RunInput) -> None:
        self.check(run_input)
```

## R9: Tools Built-in Relevantes para o Curso

**Decision**: Usar DuckDuckGoTools (busca web) e custom tools (funções Python) como base.

| Aula | Tools |
|------|-------|
| 03 - Tool Calling | `DuckDuckGoTools` (busca web) + custom calculator tool |
| 04 - ReAct | `ReasoningTools` + `DuckDuckGoTools` |
| 06 - RAG | Knowledge + custom tools para queries |
| 10 - Projeto Final | `DuckDuckGoTools` + custom tools + Knowledge |

**Criação de custom tools** (3 formas):
```python
# 1. Função simples
def my_tool(param: str) -> str:
    """Docstring vira a descrição da tool."""
    return result

# 2. Decorator @tool
from agno.tools import tool
@tool
def my_tool(param: str) -> str:
    ...

# 3. Toolkit class (tools agrupadas com estado compartilhado)
from agno.tools import Toolkit
class MyTools(Toolkit):
    def __init__(self):
        super().__init__(name="my_tools", tools=[self.my_method])
    def my_method(self, param: str) -> str:
        ...
```

## R10: Structured Output (Aula 02)

**Decision**: Usar `output_schema` com Pydantic models no Agno.

**Rationale**: Integração nativa com Pydantic. Aluno aprende a forçar respostas estruturadas do LLM.

**Configuração Agno**:
```python
from pydantic import BaseModel, Field
from agno.agent import Agent

class Analysis(BaseModel):
    summary: str
    key_points: list[str]
    confidence: float = Field(ge=0, le=1)

agent = Agent(
    model=Gemini(id="gemini-2.5-flash"),
    output_schema=Analysis,
)
response = agent.run("Analyze the impact of AI on education")
result: Analysis = response.content
```

## R11: Gerenciamento de Dependências — uv + pyproject.toml

**Decision**: Usar `uv` como gerenciador de pacotes e `pyproject.toml` para dependências.

**Rationale**: `uv` é o padrão moderno em 2026 — 10-100x mais rápido que pip, resolve dependências corretamente, suporta workspaces. Cada aula terá seu próprio `pyproject.toml`.

**Dependências base por aula**:
```toml
[project]
name = "aula-01-hello-agent"
version = "0.1.0"
requires-python = ">=3.11"
dependencies = [
    "agno",
    "google-genai",
]
```

**Dependências adicionais por aula**:
| Aula | Dependências extras |
|------|-------------------|
| 03 | `duckduckgo-search` |
| 05 | (nenhuma — SqliteDb é built-in) |
| 06 | `lancedb`, `tantivy` |
| 09 | (nenhuma — guardrails são built-in) |
| 10 | `duckduckgo-search`, `lancedb`, `tantivy` |

## Tabela de Imports Chave

| Feature | Import |
|---------|--------|
| Agent | `from agno.agent import Agent` |
| Gemini | `from agno.models.google import Gemini` |
| SqliteDb | `from agno.db.sqlite import SqliteDb` |
| Knowledge | `from agno.knowledge.knowledge import Knowledge` |
| GeminiEmbedder | `from agno.knowledge.embedder.google import GeminiEmbedder` |
| LanceDb | `from agno.vectordb.lancedb import LanceDb` |
| Team | `from agno.team import Team` |
| TeamMode | `from agno.team.mode import TeamMode` |
| ReasoningTools | `from agno.tools.reasoning import ReasoningTools` |
| DuckDuckGoTools | `from agno.tools.duckduckgo import DuckDuckGoTools` |
| @tool | `from agno.tools import tool` |
| Toolkit | `from agno.tools import Toolkit` |
| Guardrails | `from agno.guardrails import BaseGuardrail, PIIDetectionGuardrail` |
| Structured Output | `output_schema=PydanticModel` (parâmetro do Agent) |
| PDFReader | `from agno.knowledge.reader.pdf_reader import PDFReader` |

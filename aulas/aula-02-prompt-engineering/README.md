# Aula 02: Prompt Engineering para Agentes

## Objetivo

Aprender a controlar o comportamento de um agente usando system prompts avançados (instructions) e forçar respostas estruturadas com Pydantic (output_schema). Ao final, você terá um agente que retorna dados tipados em vez de texto livre.

## Conceitos

- `instructions` — lista de instruções que definem o comportamento do agente (system prompt)
- `output_schema` — schema Pydantic que força o agente a retornar dados estruturados
- `BaseModel` / `Field` — classes Pydantic para definir o formato da resposta
- `.run()` — executa o agente e retorna um objeto `RunOutput` (em vez de imprimir)

## Pré-requisitos

- [Aula 01](../aula-01-hello-agent/README.md) completada
- `.env` com GOOGLE_API_KEY configurada

## Teoria

### System Prompts (instructions)

O system prompt é a "personalidade" do agente. Ele define:

- **Quem** o agente é (papel, especialidade)
- **Como** deve responder (formato, idioma, tom)
- **O que** deve ou não fazer (limites, regras)

No Agno, `instructions` aceita uma string ou uma lista de strings:

```python
# String simples
Agent(instructions="Você é um professor de Python.")

# Lista (mais organizado)
Agent(instructions=[
    "Você é um professor de Python.",
    "Responda em português.",
    "Use exemplos de código.",
])
```

### Structured Output

Em vez de receber texto livre, você pode forçar o agente a retornar dados tipados usando Pydantic:

```
┌──────────┐     prompt      ┌─────────┐     API      ┌─────────┐
│   Você   │ ──────────────> │  Agent  │ ───────────> │ Gemini  │
│          │                 │         │              │         │
│          │  TechAnalysis   │  output │  JSON válido │         │
│          │ <────────────── │  schema │ <─────────── │         │
└──────────┘   (Pydantic)    └─────────┘              └─────────┘
```

O Agno converte o schema Pydantic em instruções para o LLM, forçando-o a retornar JSON válido que é automaticamente parseado de volta para um objeto Python tipado.

### Por que structured output?

- **Previsibilidade** — sempre recebe o mesmo formato
- **Validação** — Pydantic valida tipos, ranges, e constraints
- **Integração** — fácil de usar em pipelines, APIs, dashboards
- **Type safety** — IDE com autocomplete nos campos

> Diagrama completo disponível em [assets/diagram.md](assets/diagram.md).

## Prática

### Passo 1: Setup

```bash
cd aulas/aula-02-prompt-engineering
uv sync
```

### Passo 2: Código

O `main.py` tem duas partes:

**Parte 1 — Instructions avançadas:**
```python
analyst = Agent(
    instructions=[
        "Você é um analista de tecnologia especializado em IA.",
        "Sempre responda em português.",
        "Estruture suas respostas com: Resumo, Pontos Positivos, Pontos Negativos.",
        "Seja objetivo e use no máximo 200 palavras.",
    ],
)
```

**Parte 2 — Structured output com Pydantic:**
```python
class TechAnalysis(BaseModel):
    technology: str
    summary: str
    pros: list[str]
    cons: list[str]
    score: float = Field(ge=0, le=10)

agent = Agent(output_schema=TechAnalysis)
response = agent.run("Analise o framework Agno")
analysis: TechAnalysis = response.content  # Objeto tipado!
```

Note a diferença: `.print_response()` imprime no terminal, `.run()` retorna um `RunOutput` com o campo `.content` contendo o objeto Pydantic.

### Passo 3: Executar

```bash
uv run python main.py
```

Resultado esperado:

```
=== Parte 1: System Prompt Detalhado ===
┃ **Resumo**: Agentes de IA estão transformando...
┃ **Pontos Positivos**: ...
┃ **Pontos Negativos**: ...

=== Parte 2: Structured Output (Pydantic) ===
Tecnologia: Agno
Resumo: Framework Python para agentes de IA...
Pontos positivos: API simples, Multi-modelo, Performance
Pontos negativos: Comunidade pequena, Documentação em evolução, ...
Nota: 8.5/10
```

## Desafio

1. Crie um schema `MovieReview` com campos: `title`, `genre`, `rating` (0-5), `review` (max 100 palavras), `recommended` (bool)
2. Use o agente para gerar reviews de 3 filmes diferentes
3. Experimente adicionar `Field(min_length=10)` e veja o que acontece quando o LLM tenta responder com algo muito curto

## Troubleshooting

| Erro | Solução |
|------|---------|
| `ValidationError` do Pydantic | O LLM retornou dados fora do schema — tente reformular o prompt |
| `response.content` é string em vez de objeto | Verifique se `output_schema` está definido no Agent |
| Resposta vazia ou truncada | Aumente o contexto no prompt ou simplifique o schema |
| `ImportError: pydantic` | Execute `uv sync` — pydantic é dependência transitiva do agno |
| Score fora do range 0-10 | Field(ge=0, le=10) valida — se falhar, o Agno retenta automaticamente |

## Próxima Aula

[Aula 03: Tool Calling](../aula-03-tool-calling/README.md) — Conecte seu agente a ferramentas externas como busca web e calculadora.

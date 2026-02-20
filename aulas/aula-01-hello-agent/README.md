# Aula 01: Olá, Agente!

## Objetivo

Criar seu primeiro agente de IA conversacional usando o framework Agno com o modelo Google Gemini. Ao final desta aula, você terá um agente funcional que responde perguntas no terminal.

## Conceitos

- `Agent` — classe principal do Agno que encapsula um agente de IA
- `Gemini` — integração com o modelo Google Gemini
- `instructions` — prompt de sistema que define o comportamento do agente
- `print_response` — método que envia uma mensagem e imprime a resposta
- `stream=True` — exibe a resposta em tempo real (token por token)

## Pré-requisitos

- Python 3.11+ instalado
- uv instalado (`curl -LsSf https://astral.sh/uv/install.sh | sh`)
- API Key do Google Gemini (gratuita): [aistudio.google.com/apikey](https://aistudio.google.com/apikey)

## Teoria

### O que é um LLM?

Um **Large Language Model** (LLM) é um modelo de IA treinado em bilhões de textos. Ele recebe texto como entrada e gera texto como saída. Exemplos: GPT, Claude, Gemini, Llama.

### O que é um Agente de IA?

Um **agente** é um programa que usa um LLM como "cérebro" para tomar decisões. Diferente de uma simples chamada de API, um agente pode:

- Seguir instruções específicas (system prompt)
- Usar ferramentas externas (aulas futuras)
- Manter memória de conversas (aulas futuras)
- Colaborar com outros agentes (aulas futuras)

### Como funciona?

```
┌─────────┐    mensagem    ┌─────────┐    API call    ┌─────────┐
│  Você   │ ─────────────> │  Agent  │ ─────────────> │ Gemini  │
│ (user)  │ <───────────── │ (Agno)  │ <───────────── │  (LLM)  │
└─────────┘    resposta    └─────────┘    response    └─────────┘
```

O **Agent** do Agno gerencia toda a comunicação com o LLM: envia suas instruções, sua mensagem, e formata a resposta.

### Por que Agno?

Agno é um framework Python open-source para agentes de IA. Vantagens:

- API simples e intuitiva
- Suporta múltiplos modelos (Gemini, GPT, Claude, etc.)
- Recursos nativos: tools, memory, knowledge, teams, guardrails
- Performance superior (529x mais rápido que LangGraph na instanciação)

> Diagrama completo disponível em [assets/diagram.md](assets/diagram.md).

## Prática

### Passo 1: Setup

```bash
cd aulas/aula-01-hello-agent
uv sync
```

Configure sua API key (se ainda não fez):

```bash
# Na raiz do projeto
cp .env.example .env
# Edite .env e coloque: GOOGLE_API_KEY=sua_key_aqui
```

### Passo 2: Código

Abra o arquivo `main.py` e analise:

```python
from dotenv import load_dotenv
from agno.agent import Agent
from agno.models.google import Gemini

load_dotenv()  # Carrega GOOGLE_API_KEY do arquivo .env

agent = Agent(
    model=Gemini(id="gemini-2.5-flash"),  # Modelo a usar
    instructions="Você é um assistente simpático...",  # System prompt
    markdown=True,  # Formata resposta em Markdown
)

agent.print_response("Olá!", stream=True)  # Envia mensagem e imprime
```

**Pontos-chave:**

1. `load_dotenv()` carrega a API key do arquivo `.env`
2. `Gemini(id="gemini-2.5-flash")` seleciona o modelo (rápido e gratuito)
3. `instructions` define a "personalidade" do agente
4. `print_response()` envia a mensagem e imprime a resposta formatada
5. `stream=True` mostra a resposta em tempo real

### Passo 3: Executar

```bash
uv run python main.py
```

Resultado esperado:

```
┃ Olá! Eu sou um assistente de IA...
┃ ...
```

Você acabou de criar seu primeiro agente de IA!

## Desafio

1. Mude o `instructions` para dar ao agente uma personalidade diferente (ex: pirata, professor, chef de cozinha)
2. Faça o agente responder em inglês mudando as instruções
3. Troque `gemini-2.5-flash` por `gemini-2.5-pro` e compare as respostas

## Troubleshooting

| Erro | Solução |
|------|---------|
| `ModuleNotFoundError: No module named 'agno'` | Execute `uv sync` no diretório da aula |
| `GOOGLE_API_KEY not found` | Crie o arquivo `.env` com sua key (veja Passo 1) |
| `google.api_core.exceptions.PermissionDenied` | Sua API key está inválida — gere uma nova em aistudio.google.com |
| `RateLimitError` | Free tier do Gemini tem limites — aguarde 1 minuto |
| `ConnectionError` | Verifique sua conexão com a internet |

## Próxima Aula

[Aula 02: Prompt Engineering](../aula-02-prompt-engineering/README.md) — Aprenda a controlar o comportamento do agente com system prompts avançados e structured output usando Pydantic.

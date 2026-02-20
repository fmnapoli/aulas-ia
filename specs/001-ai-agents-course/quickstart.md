# Quickstart: Curso Prático de Desenvolvimento de Agentes de IA

**Date**: 2026-02-19  
**Feature**: `001-ai-agents-course`

## Pré-requisitos

1. **Python 3.11+** instalado
2. **uv** (gerenciador de pacotes) instalado
3. **API Key do Google Gemini** (gratuita, sem cartão de crédito)

## Setup Inicial (uma vez)

### 1. Clonar o repositório

```bash
git clone https://github.com/<org>/aulas-ia.git
cd aulas-ia
```

### 2. Obter API Key do Google Gemini

1. Acesse https://aistudio.google.com/apikey
2. Clique em "Create API Key"
3. Copie a key gerada

### 3. Configurar variável de ambiente

```bash
cp .env.example .env
# Edite .env e coloque sua GOOGLE_API_KEY
```

Conteúdo do `.env`:
```
GOOGLE_API_KEY=sua_key_aqui
```

### 4. Instalar uv (se não tiver)

```bash
# Linux/macOS
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

## Executar uma Aula

Cada aula é independente. Para executar qualquer aula:

```bash
# Entrar no diretório da aula
cd aulas/aula-01-hello-agent

# Instalar dependências (uv cria venv automaticamente)
uv sync

# Executar o exemplo
uv run python main.py
```

## Verificação Rápida (Aula 01)

Após o setup, teste se tudo funciona:

```bash
cd aulas/aula-01-hello-agent
uv sync
uv run python main.py
```

Resultado esperado:
```
┃ Agent Response
┃ Olá! Eu sou seu primeiro agente de IA...
```

Se funcionar, o setup está completo. Siga para a Aula 01 (`aulas/aula-01-hello-agent/README.md`).

## Estrutura do Repositório

```text
aulas-ia/
├── README.md                  # Visão geral do curso
├── .env.example               # Template para API key
├── pyproject.toml             # Dependências compartilhadas
└── aulas/
    ├── aula-01-hello-agent/   # Cada aula é auto-contida
    │   ├── README.md          # Teoria + instruções (PT)
    │   ├── main.py            # Código do exemplo (EN)
    │   └── pyproject.toml     # Dependências da aula
    ├── aula-02-prompt-engineering/
    ├── ...
    └── aula-10-projeto-final/
```

## Troubleshooting Comum

| Problema | Solução |
|----------|---------|
| `ModuleNotFoundError: agno` | Execute `uv sync` no diretório da aula |
| `google.api_core.exceptions.PermissionDenied` | Verifique se `GOOGLE_API_KEY` está no `.env` |
| `GOOGLE_API_KEY not set` | Execute `export GOOGLE_API_KEY=sua_key` ou use arquivo `.env` |
| `RateLimitError` | Free tier do Gemini tem limites — aguarde 1 minuto e tente novamente |
| `python: command not found` | Instale Python 3.11+ via https://python.org |
| `uv: command not found` | Instale uv: `curl -LsSf https://astral.sh/uv/install.sh \| sh` |

## Custo Estimado

| Item | Custo |
|------|-------|
| Python | Gratuito |
| uv | Gratuito |
| Google Gemini API (free tier) | Gratuito |
| Google Gemini API (se exceder free tier) | < $5 total para todas as aulas |
| LanceDb (vector database local) | Gratuito |
| **Total** | **$0 - $5** |

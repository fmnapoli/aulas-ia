# Lesson Contract: Estrutura Padrão de Cada Aula

**Date**: 2026-02-19

## Contrato

Este projeto não expõe APIs REST/GraphQL. O "contrato" é a estrutura padronizada que toda aula DEVE seguir para garantir consistência e qualidade.

## Estrutura de Diretório (obrigatória)

```text
aulas/aula-XX-slug/
├── README.md          # Obrigatório — conteúdo teórico + instruções
├── main.py            # Obrigatório — exemplo prático completo
├── pyproject.toml     # Obrigatório — dependências da aula
└── assets/            # Obrigatório — diagramas e ilustrações
    └── diagram.png    # Pelo menos 1 diagrama por aula (FR-009)
```

Arquivos opcionais (quando necessário):
```text
├── tools.py           # Custom tools (aulas 03, 04, 07, 10)
├── guardrails.py      # Custom guardrails (aula 09)
├── agents/            # Múltiplos agentes (aula 10)
│   ├── researcher.py
│   ├── analyst.py
│   └── writer.py
└── docs/              # Documentos de exemplo para RAG (aula 06)
```

## README.md — Template (obrigatório)

Cada README.md DEVE seguir esta estrutura:

```markdown
# Aula XX: Título da Aula

## Objetivo
[1-2 frases: o que o aluno vai aprender e construir]

## Conceitos
[Lista dos conceitos Agno introduzidos nesta aula]

## Pré-requisitos
- Aula(s) anterior(es) completada(s) (se houver)
- Dependências específicas (se houver)

## Teoria (máx. 15 min de leitura)
[Explicação do conceito com exemplos visuais]
[Diagrama: assets/diagram.png]

## Prática
### Passo 1: Setup
[Instruções de instalação]

### Passo 2: Código
[Explicação passo-a-passo do main.py]

### Passo 3: Executar
[Comando para rodar + output esperado]

## Desafio (opcional)
[Exercício extra para quem quer ir além]

## Troubleshooting
[Top 5 erros mais comuns e suas soluções]

## Próxima Aula
[Link e preview da próxima aula]
```

## main.py — Padrão (obrigatório)

Todo `main.py` DEVE:
1. Ser executável diretamente: `uv run python main.py`
2. Carregar `GOOGLE_API_KEY` via dotenv ou variável de ambiente
3. Produzir output visível no terminal
4. Ter no máximo ~50-100 linhas (excluindo comentários)
5. Usar nomes de variáveis e funções em inglês
6. Usar Gemini como modelo padrão

```python
"""Aula XX: Título — Descrição breve."""

from agno.agent import Agent
from agno.models.google import Gemini

# ... setup ...

agent = Agent(
    model=Gemini(id="gemini-2.5-flash"),
    # ... configuração específica da aula ...
)

# Demonstração
agent.print_response("...", stream=True)
```

## pyproject.toml — Padrão (obrigatório)

```toml
[project]
name = "aula-XX-slug"
version = "0.1.0"
description = "Aula XX: Título"
requires-python = ">=3.11"
dependencies = [
    "agno",
    "google-genai",
    "python-dotenv",
]

# Dependências extras conforme a aula:
# "duckduckgo-search"  → aulas 03, 04, 10
# "lancedb"            → aulas 06, 10
# "tantivy"            → aulas 06, 10 (hybrid search com LanceDb)
```

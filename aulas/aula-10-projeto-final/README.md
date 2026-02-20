# Aula 10: Projeto Final — Assistente de Pesquisa

## Objetivo

Construir um assistente de pesquisa completo que combina os conceitos de todas as aulas anteriores: Team multi-agente com coordenação, Tool Calling para busca web, e geração de relatórios estruturados. Ao final, você terá um sistema que pesquisa, analisa e produz relatórios automaticamente.

## Conceitos

- `Team` — orquestra múltiplos agentes especializados
- `TeamMode.coordinate` — líder delega tarefas e coordena o fluxo
- `DuckDuckGoTools` — ferramenta de busca web integrada
- Agentes especializados — cada um com papel e instruções específicas
- Pipeline de pesquisa — Researcher → Analyst → Writer

## Pré-requisitos

- Todas as aulas anteriores (01-09) completadas
- `.env` com GOOGLE_API_KEY configurada

## Teoria

### Recapitulação — O que aprendemos

Este projeto final integra conceitos de todo o curso:

| Aula | Conceito | Uso no projeto |
|------|----------|----------------|
| 01-02 | Agent, Instructions, Structured Output | Base de todos os agentes |
| 03 | Tool Calling | Researcher usa DuckDuckGoTools |
| 04 | ReAct Loop | Researcher raciocina sobre resultados |
| 05 | Memory | Contexto compartilhado via Team |
| 06 | Knowledge / RAG | Analyst cruza informações |
| 07 | Planning | Team Leader planeja delegações |
| 08 | Multi-Agent Team | Coordenação entre 3 agentes |
| 09 | Guardrails | Pode ser adicionado como extensão |

### Arquitetura do sistema

O assistente usa um **Team com modo coordinate**, onde um líder (Team Leader) delega tarefas em sequência para três agentes especializados:

```
Usuário → Team Leader → Researcher (busca web)
                       → Analyst (análise cruzada)
                       → Writer (relatório em PT-BR)
                       → Relatório Final
```

### Por que separar em agentes?

**Princípio da responsabilidade única**: cada agente é especialista em uma tarefa. Isso resulta em:

- **Qualidade** — instruções focadas produzem melhores resultados
- **Manutenção** — fácil trocar ou melhorar um agente sem afetar outros
- **Escalabilidade** — adicionar novos agentes (ex: Reviewer) sem reescrever
- **Debug** — identificar qual etapa falhou quando algo dá errado

### TeamMode.coordinate

No modo `coordinate`, o Team Leader:

1. Recebe a tarefa do usuário
2. Decide a ordem de delegação
3. Passa o contexto entre agentes
4. Consolida o resultado final

O líder usa o LLM para tomar decisões inteligentes sobre como delegar, mas segue as `instructions` definidas no Team.

> Diagrama completo disponível em [assets/diagram.md](assets/diagram.md).

## Prática

### Passo 1: Setup

```bash
cd aulas/aula-10-projeto-final
uv sync
```

### Passo 2: Código

O projeto tem 3 agentes em `agents/`:

**Researcher** (`agents/researcher.py`) — pesquisador com acesso à web:
```python
researcher = Agent(
    name="Researcher",
    role="Search the web for relevant sources on a given topic",
    model=Gemini(id="gemini-2.5-flash"),
    tools=[DuckDuckGoTools()],
    instructions=[
        "Search the web thoroughly for the given topic.",
        "Find at least 3-5 relevant and recent sources.",
        "Provide URLs and key findings from each source.",
        "Focus on factual, verifiable information.",
    ],
)
```

**Analyst** (`agents/analyst.py`) — analisa e cruza informações:
```python
analyst = Agent(
    name="Analyst",
    role="Analyze and cross-reference research findings",
    instructions=[
        "Analyze the research findings provided.",
        "Identify common themes, contradictions, and key insights.",
        "Cross-reference information from multiple sources.",
        "Highlight the most important and reliable findings.",
    ],
)
```

**Writer** (`agents/writer.py`) — escreve o relatório final em português:
```python
writer = Agent(
    name="Writer",
    role="Write structured research reports in Portuguese",
    instructions=[
        "Write a well-structured research report in Portuguese.",
        "Use the following structure: Resumo, Principais Descobertas, Análise, Conclusão.",
        "Use markdown formatting with headers, bullet points, and emphasis.",
        "Be objective and cite sources when available.",
        "Keep the report concise but comprehensive (max 500 words).",
    ],
)
```

O `main.py` cria o Team que coordena os três agentes:

```python
research_team = Team(
    name="Research Assistant",
    model=Gemini(id="gemini-2.5-flash"),
    members=[researcher, analyst, writer],
    mode=TeamMode.coordinate,
    instructions=[
        "You lead a research team that produces structured reports.",
        "1. First, delegate to Researcher to find sources on the topic.",
        "2. Then, delegate to Analyst to analyze and cross-reference findings.",
        "3. Finally, delegate to Writer to produce a structured report in Portuguese.",
        "Ensure the final output is a complete, well-structured research report.",
    ],
)
```

As `instructions` do Team definem a sequência de delegação. O líder segue esse pipeline: Researcher → Analyst → Writer.

### Passo 3: Executar

```bash
uv run python main.py
```

Resultado esperado (exemplo resumido):

```
=== Assistente de Pesquisa ===

Tema: O estado atual dos agentes de IA em 2026

┃ ## Resumo
┃ Os agentes de IA em 2026 evoluíram significativamente...
┃
┃ ## Principais Descobertas
┃ - **Frameworks**: Agno, LangGraph, CrewAI e AutoGen lideram o mercado...
┃ - **Produção**: Empresas adotam agentes para atendimento, pesquisa e automação...
┃ - **Desafios**: Alucinações, custo de inferência e segurança permanecem...
┃
┃ ## Análise
┃ A tendência é clara: agentes estão migrando de experimentação para produção...
┃
┃ ## Conclusão
┃ O ecossistema de agentes de IA amadureceu consideravelmente em 2026...
```

O tempo de execução pode ser de 30-60 segundos, pois envolve múltiplas chamadas ao LLM e buscas web.

## Desafio

1. Adicione um 4o agente **Reviewer** que revisa o relatório do Writer, verificando qualidade, coerência e cobertura do tema
2. Adicione **guardrails** (Aula 09) ao Team para validar o tema de pesquisa antes de iniciar
3. Adicione **memory** (Aula 05) para que o assistente lembre de pesquisas anteriores
4. Experimente trocar `TeamMode.coordinate` por `TeamMode.collaborate` e compare os resultados

## Troubleshooting

| Erro | Solução |
|------|---------|
| `ModuleNotFoundError: ddgs` | Execute `uv sync` — `ddgs` é dependência de `DuckDuckGoTools` |
| Timeout na busca web | DuckDuckGo pode estar lento — tente novamente |
| Relatório em inglês | Verifique as instructions do Writer — deve especificar português |
| Team não delega na ordem | As instructions do Team podem precisar ser mais explícitas |
| `RateLimitError` | Múltiplos agentes fazem várias chamadas — aguarde 1 minuto |
| Resposta incompleta | Aumente o tempo de espera ou simplifique o tema de pesquisa |

## Parabéns!

Você completou o curso de Agentes de IA! Agora você sabe:

- Criar agentes com diferentes personalidades e instruções
- Usar tool calling para conectar agentes ao mundo real
- Implementar memória e knowledge base (RAG)
- Planejar e raciocinar com agentes
- Orquestrar múltiplos agentes em equipes
- Proteger agentes com guardrails de segurança
- Combinar tudo em um sistema de produção

O próximo passo é criar seus próprios agentes para resolver problemas reais!

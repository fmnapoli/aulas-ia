# Diagrama: Arquitetura do Assistente de Pesquisa

```mermaid
flowchart TD
    U[Usuário] -->|Tema de pesquisa| TL[Team Leader<br/>Coordenador]

    TL -->|1. Delegação| R[Researcher<br/>Pesquisador]
    R -->|Busca web| DDG[DuckDuckGo<br/>Tools]
    DDG -->|Resultados| R
    R -->|Fontes encontradas| TL

    TL -->|2. Delegação| AN[Analyst<br/>Analista]
    AN -->|Análise cruzada| TL

    TL -->|3. Delegação| W[Writer<br/>Redator]
    W -->|Relatório em PT-BR| TL

    TL -->|Relatório final| U

    style TL fill:#1565c0,stroke:#0d47a1,color:#fff
    style R fill:#f9a825,stroke:#f57f17,color:#000
    style AN fill:#f9a825,stroke:#f57f17,color:#000
    style W fill:#f9a825,stroke:#f57f17,color:#000
    style DDG fill:#7b1fa2,stroke:#4a148c,color:#fff
```

## Fluxo detalhado de coordenação

```mermaid
sequenceDiagram
    participant U as Usuário
    participant TL as Team Leader
    participant R as Researcher
    participant DDG as DuckDuckGo
    participant AN as Analyst
    participant W as Writer

    U->>TL: "Pesquise sobre agentes de IA em 2026"

    Note over TL: Etapa 1: Pesquisa
    TL->>R: Delegação: buscar fontes
    R->>DDG: Busca web
    DDG-->>R: Resultados (URLs + conteúdo)
    R->>DDG: Busca refinada
    DDG-->>R: Mais resultados
    R-->>TL: 3-5 fontes com resumos

    Note over TL: Etapa 2: Análise
    TL->>AN: Delegação: analisar fontes
    Note over AN: Cruza informações<br/>Identifica padrões<br/>Avalia confiabilidade
    AN-->>TL: Insights + temas comuns

    Note over TL: Etapa 3: Redação
    TL->>W: Delegação: escrever relatório
    Note over W: Estrutura:<br/>Resumo<br/>Descobertas<br/>Análise<br/>Conclusão
    W-->>TL: Relatório em português

    TL-->>U: Relatório final formatado
```

## Conceitos combinados das aulas anteriores

```mermaid
mindmap
  root((Projeto Final))
    Aula 01-02
      Agent básico
      Instructions
      Structured Output
    Aula 03-04
      Tool Calling
      ReAct Loop
    Aula 05-06
      Memory
      Knowledge / RAG
    Aula 07
      Planning
      Raciocínio
    Aula 08
      Multi-Agent Team
      Coordenação
    Aula 09
      Guardrails
      Segurança
    Projeto Final
      Team coordinate
      Web Search Tools
      Relatório estruturado
```

## Versão texto

```
┌──────────┐                    ┌───────────────────┐
│ Usuário  │ ─── tema ───────> │   Team Leader     │
│          │                    │   (Coordenador)   │
│          │                    └────────┬──────────┘
│          │                             │
│          │                    ┌────────▼──────────┐
│          │                    │   1. Researcher   │ ──── DuckDuckGo
│          │                    │   (Pesquisador)   │ <─── Resultados
│          │                    └────────┬──────────┘
│          │                             │ fontes
│          │                    ┌────────▼──────────┐
│          │                    │   2. Analyst      │
│          │                    │   (Analista)      │
│          │                    └────────┬──────────┘
│          │                             │ insights
│          │                    ┌────────▼──────────┐
│          │                    │   3. Writer       │
│          │                    │   (Redator)       │
│          │                    └────────┬──────────┘
│          │                             │ relatório
│          │ <── relatório final ────────┘
└──────────┘
```

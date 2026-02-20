# Diagrama: Ciclo ReAct (Reasoning + Acting)

```mermaid
flowchart TD
    Q[Pergunta do Usuário] --> T1

    subgraph loop ["Ciclo ReAct (repete até ter resposta)"]
        T1["🧠 Think<br/>Raciocinar sobre o problema"]
        T1 --> A1["⚡ Act<br/>Decidir e executar ação"]
        A1 --> O1["👁 Observe<br/>Analisar o resultado"]
        O1 --> D{Tem informação<br/>suficiente?}
        D -->|Não| T1
    end

    D -->|Sim| R[Resposta Final]

    style T1 fill:#4a90d9,color:#fff
    style A1 fill:#e67e22,color:#fff
    style O1 fill:#27ae60,color:#fff
    style R fill:#8e44ad,color:#fff
```

## Ciclo detalhado com ferramentas

```mermaid
sequenceDiagram
    participant U as Usuário
    participant A as Agent (Agno)
    participant L as Gemini (LLM)
    participant R as ReasoningTools
    participant S as DuckDuckGoTools

    U->>A: "Compare Agno e LangGraph"
    A->>L: Mensagem + tools disponíveis

    rect rgb(66, 133, 244, 0.1)
        Note over L,R: Ciclo 1: Think → Act → Observe
        L->>R: think("Preciso pesquisar sobre Agno")
        R-->>L: pensamento registrado
        L->>S: duckduckgo_search("Agno framework AI agents")
        S-->>L: Resultados da busca sobre Agno
    end

    rect rgb(234, 67, 53, 0.1)
        Note over L,R: Ciclo 2: Think → Act → Observe
        L->>R: think("Agora preciso pesquisar LangGraph")
        R-->>L: pensamento registrado
        L->>S: duckduckgo_search("LangGraph framework AI agents")
        S-->>L: Resultados da busca sobre LangGraph
    end

    rect rgb(52, 168, 83, 0.1)
        Note over L,R: Ciclo 3: Think → Responder
        L->>R: think("Tenho dados suficientes para comparar")
        R-->>L: pensamento registrado
    end

    L-->>A: Resposta comparativa final
    A-->>U: Resposta formatada
```

## Comparação: com e sem ReAct

```mermaid
flowchart LR
    subgraph sem ["Sem ReasoningTools"]
        direction TB
        S1[Pergunta] --> S2[Busca] --> S3[Resposta]
    end

    subgraph com ["Com ReasoningTools"]
        direction TB
        C1[Pergunta] --> C2[Think: planejar]
        C2 --> C3[Act: buscar Agno]
        C3 --> C4[Observe: analisar]
        C4 --> C5[Think: o que falta?]
        C5 --> C6[Act: buscar LangGraph]
        C6 --> C7[Observe: comparar]
        C7 --> C8[Think: sintetizar]
        C8 --> C9[Resposta]
    end

    style com fill:#e8f5e9
    style sem fill:#fff3e0
```

## Versão texto

```
┌─────────────────────────────────────────────────────────┐
│                    CICLO ReAct                          │
│                                                         │
│  ┌──────────┐    ┌──────────┐    ┌──────────┐          │
│  │  THINK   │───>│   ACT    │───>│ OBSERVE  │          │
│  │ Raciocin │    │ Executar │    │ Analisar │          │
│  │ ar sobre │    │ ação /   │    │ resulta- │          │
│  │ problema │    │ tool     │    │ do       │          │
│  └──────────┘    └──────────┘    └────┬─────┘          │
│       ▲                               │                 │
│       │          Informação           │                 │
│       │          insuficiente         │                 │
│       └───────────────────────────────┘                 │
│                       │                                 │
│                Informação suficiente                    │
│                       ▼                                 │
│              ┌──────────────┐                           │
│              │   RESPOSTA   │                           │
│              │    FINAL     │                           │
│              └──────────────┘                           │
└─────────────────────────────────────────────────────────┘
```

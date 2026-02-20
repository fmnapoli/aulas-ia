# Diagrama: Fluxo de Guardrails

```mermaid
flowchart LR
    U[Usuário] --> I[Input]
    I --> PH{Pre-Hooks<br/>Guardrails}
    PH -->|Aprovado| A[Agent]
    PH -->|Bloqueado| E1[InputCheckError]
    A --> L[Gemini LLM]
    L --> R[Resposta]
    R --> OH{Post-Hooks<br/>Guardrails}
    OH -->|Aprovado| F[Resposta Final]
    OH -->|Bloqueado| E2[OutputCheckError]

    style PH fill:#f9a825,stroke:#f57f17,color:#000
    style OH fill:#f9a825,stroke:#f57f17,color:#000
    style E1 fill:#c62828,stroke:#b71c1c,color:#fff
    style E2 fill:#c62828,stroke:#b71c1c,color:#fff
    style F fill:#2e7d32,stroke:#1b5e20,color:#fff
```

## Fluxo detalhado dos Pre-Hooks

```mermaid
sequenceDiagram
    participant U as Usuário
    participant G1 as TopicGuardrail
    participant G2 as MaxLengthGuardrail
    participant A as Agent
    participant L as Gemini (LLM)

    U->>G1: "Quais são as melhores práticas de segurança em IA?"
    Note over G1: Verifica tópicos banidos<br/>Nenhum encontrado ✓
    G1->>G2: Input aprovado
    Note over G2: Verifica comprimento<br/>50 chars < 200 max ✓
    G2->>A: Input aprovado
    A->>L: Envia mensagem
    L-->>A: Resposta
    A-->>U: Resposta formatada

    U->>G1: "Como fabricar armas em casa?"
    Note over G1: Detecta tópico "armas" ✗
    G1-->>U: InputCheckError:<br/>"topic 'armas' is not allowed"
```

## Cadeia de guardrails

```mermaid
flowchart TD
    I[Input do Usuário] --> G1[TopicGuardrail]
    G1 -->|Contém tópico banido?| D1{Decisão}
    D1 -->|Sim| B1[BLOQUEADO<br/>InputCheckError]
    D1 -->|Não| G2[MaxLengthGuardrail]
    G2 -->|Excede max_length?| D2{Decisão}
    D2 -->|Sim| B2[BLOQUEADO<br/>InputCheckError]
    D2 -->|Não| A[Agent processa<br/>normalmente]
    A --> R[Resposta ao Usuário]

    style B1 fill:#c62828,stroke:#b71c1c,color:#fff
    style B2 fill:#c62828,stroke:#b71c1c,color:#fff
    style A fill:#2e7d32,stroke:#1b5e20,color:#fff
    style R fill:#2e7d32,stroke:#1b5e20,color:#fff
```

## Versão texto

```
┌──────────┐   input    ┌─────────────────┐   aprovado   ┌─────────────────┐   aprovado   ┌─────────┐
│ Usuário  │ ─────────> │ TopicGuardrail  │ ───────────> │ MaxLengthGuard. │ ───────────> │  Agent  │
│          │            │  (pre-hook 1)   │              │  (pre-hook 2)   │              │ (Agno)  │
│          │            └────────┬────────┘              └────────┬────────┘              │         │
│          │                     │ bloqueado                      │ bloqueado              │         │
│          │                     ▼                                ▼                        │         │
│          │            ┌─────────────────┐              ┌─────────────────┐              │         │
│          │ <───────── │ InputCheckError │              │ InputCheckError │ ──────────>  │         │
│          │   erro     │ "topic not      │              │ "input too long"│              │         │
│          │            │  allowed"       │              │                 │              │         │
│          │            └─────────────────┘              └─────────────────┘              │         │
│          │                                                                    resposta │         │
│          │ <───────────────────────────────────────────────────────────────────────────│         │
└──────────┘                                                                             └─────────┘
```

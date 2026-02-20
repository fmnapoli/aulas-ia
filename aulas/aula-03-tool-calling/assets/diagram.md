# Diagrama: Fluxo de Tool Calling

```mermaid
sequenceDiagram
    participant U as Usuário
    participant A as Agent (Agno)
    participant L as Gemini (LLM)
    participant T as Ferramenta

    U->>A: "Quanto é 15% de 1250?"
    A->>L: System prompt + mensagem + lista de tools
    Note over L: Analisa a pergunta<br/>e seleciona a tool<br/>com base na descrição
    L-->>A: tool_call: calculate("1250 * 0.15")
    A->>T: Executa calculate("1250 * 0.15")
    T-->>A: "Result of '1250 * 0.15' = 187.5"
    A->>L: Resultado da ferramenta
    Note over L: Gera resposta final<br/>usando o resultado
    L-->>A: "15% de 1250 é 187,50"
    A-->>U: Resposta formatada
```

## Como o LLM seleciona a ferramenta

```mermaid
flowchart TD
    A[Mensagem do Usuário] --> B{LLM analisa a intenção}
    B -->|Precisa de dados atuais| C[DuckDuckGoTools]
    B -->|Precisa calcular| D[calculate]
    B -->|Precisa converter temp.| E[convert_temperature]
    B -->|Não precisa de tool| F[Responde direto]
    C --> G[Executa ferramenta]
    D --> G
    E --> G
    G --> H[Resultado retorna ao LLM]
    H --> I[LLM gera resposta final]
    F --> I
    I --> J[Resposta ao Usuário]
```

## Versão texto

```
┌──────────┐   mensagem   ┌─────────┐   msg + tools   ┌─────────┐
│ Usuário  │ ───────────> │  Agent  │ ──────────────> │ Gemini  │
│          │              │ (Agno)  │                 │  (LLM)  │
│          │              │         │  tool_call:     │         │
│          │              │         │ <────────────── │         │
│          │              │         │                 │         │
│          │              │  ┌──────────────┐         │         │
│          │              │  │  Ferramenta  │         │         │
│          │              │  │ (calculate)  │         │         │
│          │              │  └──────────────┘         │         │
│          │              │         │                 │         │
│          │              │         │  resultado      │         │
│          │              │         │ ──────────────> │         │
│          │   resposta   │         │  resposta final │         │
│          │ <─────────── │         │ <────────────── │         │
└──────────┘              └─────────┘                 └─────────┘
```

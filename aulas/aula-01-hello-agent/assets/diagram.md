# Diagrama: Fluxo do Agente Conversacional

```mermaid
sequenceDiagram
    participant U as Usuário
    participant A as Agent (Agno)
    participant G as Gemini API

    U->>A: "Olá! Quem é você?"
    Note over A: Combina instructions<br/>+ mensagem do usuário
    A->>G: System prompt + User message
    G-->>A: Resposta gerada
    A-->>U: Resposta formatada (Markdown)
```

## Versão texto

```
┌─────────┐    mensagem    ┌─────────┐    API call    ┌─────────┐
│  Você   │ ─────────────> │  Agent  │ ─────────────> │ Gemini  │
│ (user)  │ <───────────── │ (Agno)  │ <───────────── │  (LLM)  │
└─────────┘    resposta    └─────────┘    response    └─────────┘
```

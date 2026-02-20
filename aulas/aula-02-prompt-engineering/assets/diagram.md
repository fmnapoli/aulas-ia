# Diagrama: Structured Output com Pydantic

```mermaid
sequenceDiagram
    participant U as Usuário
    participant A as Agent (Agno)
    participant G as Gemini API

    U->>A: "Analise o framework X"
    Note over A: instructions +<br/>output_schema (Pydantic)
    A->>G: System prompt + Schema JSON + User message
    G-->>A: JSON válido conforme schema
    Note over A: Pydantic valida<br/>e parseia o JSON
    A-->>U: TechAnalysis(technology=..., score=8.5)
```

## Versão texto

```
┌──────────┐     prompt      ┌─────────┐     API      ┌─────────┐
│   Você   │ ──────────────> │  Agent  │ ───────────> │ Gemini  │
│          │                 │         │              │         │
│          │  TechAnalysis   │  output │  JSON válido │         │
│          │ <────────────── │  schema │ <─────────── │         │
└──────────┘   (Pydantic)    └─────────┘              └─────────┘

instructions = ["Você é um analista...", "Responda em PT..."]
output_schema = TechAnalysis (BaseModel)
    ├── technology: str
    ├── summary: str
    ├── pros: list[str]
    ├── cons: list[str]
    └── score: float (0-10)
```

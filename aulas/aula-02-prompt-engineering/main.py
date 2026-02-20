"""Aula 02: Prompt Engineering — System prompts, few-shot e structured output.

Demonstra duas técnicas fundamentais de prompt engineering:
1. System prompt detalhado (instructions) para controlar estilo e formato da resposta
2. Structured output com Pydantic para forçar respostas tipadas e validadas
"""

from dotenv import load_dotenv
from pydantic import BaseModel, Field

from agno.agent import Agent
from agno.models.google import Gemini

# Carrega variáveis de ambiente do arquivo .env (GOOGLE_API_KEY)
load_dotenv(override=True)


# --- Parte 1: System prompt com instruções detalhadas ---

analyst = Agent(
    model=Gemini(id="gemini-2.5-flash"),
    instructions=[
        "Você é um analista de tecnologia especializado em IA.",
        "Sempre responda em português.",
        "Estruture suas respostas com: Resumo, Pontos Positivos, Pontos Negativos.",
        "Seja objetivo e use no máximo 200 palavras.",
    ],
    markdown=True,
)

print("=== Parte 1: System Prompt Detalhado ===\n")
analyst.print_response(
    "Analise o impacto dos agentes de IA no desenvolvimento de software.", stream=True
)


# --- Parte 2: Structured output com Pydantic ---


class TechAnalysis(BaseModel):
    """Análise estruturada de uma tecnologia."""

    technology: str = Field(description="Nome da tecnologia analisada")
    summary: str = Field(description="Resumo breve em 1-2 frases")
    pros: list[str] = Field(description="Lista de 3 vantagens")
    cons: list[str] = Field(description="Lista de 3 desvantagens")
    score: float = Field(ge=0, le=10, description="Nota de 0 a 10")


structured_agent = Agent(
    model=Gemini(id="gemini-2.5-flash"),
    instructions="Analise a tecnologia dada de forma objetiva. Responda em português.",
    output_schema=TechAnalysis,
)

print("\n\n=== Parte 2: Structured Output (Pydantic) ===\n")
response = structured_agent.run("Analise o framework Agno para agentes de IA.")

# Exibe os campos da resposta estruturada
if isinstance(response.content, TechAnalysis):
    analysis = response.content
    print(f"Tecnologia: {analysis.technology}")
    print(f"Resumo: {analysis.summary}")
    print(f"Pontos positivos: {', '.join(analysis.pros)}")
    print(f"Pontos negativos: {', '.join(analysis.cons)}")
    print(f"Nota: {analysis.score}/10")
else:
    print(response.content)

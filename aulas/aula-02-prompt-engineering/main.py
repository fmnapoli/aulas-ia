"""Aula 02: Prompt Engineering — System prompts, few-shot e structured output."""

from dotenv import load_dotenv
from pydantic import BaseModel, Field

from agno.agent import Agent
from agno.models.google import Gemini

load_dotenv()


# --- Part 1: System prompt with detailed instructions ---

analyst = Agent(
    model=Gemini(id="gemini-2.0-flash"),
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


# --- Part 2: Structured output with Pydantic ---


class TechAnalysis(BaseModel):
    """Structured analysis of a technology."""

    technology: str = Field(description="Name of the technology analyzed")
    summary: str = Field(description="Brief summary in 1-2 sentences")
    pros: list[str] = Field(description="List of 3 advantages")
    cons: list[str] = Field(description="List of 3 disadvantages")
    score: float = Field(ge=0, le=10, description="Score from 0 to 10")


structured_agent = Agent(
    model=Gemini(id="gemini-2.0-flash"),
    instructions="Analyze the given technology objectively. Respond in Portuguese.",
    output_schema=TechAnalysis,
)

print("\n\n=== Parte 2: Structured Output (Pydantic) ===\n")
response = structured_agent.run("Analise o framework Agno para agentes de IA.")

if isinstance(response.content, TechAnalysis):
    analysis = response.content
    print(f"Tecnologia: {analysis.technology}")
    print(f"Resumo: {analysis.summary}")
    print(f"Pontos positivos: {', '.join(analysis.pros)}")
    print(f"Pontos negativos: {', '.join(analysis.cons)}")
    print(f"Nota: {analysis.score}/10")
else:
    print(response.content)

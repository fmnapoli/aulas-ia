"""Aula 03: Tool Calling — Agent with external tools (search, calculator, converter)."""

from agno.agent import Agent
from agno.models.google import Gemini
from agno.tools.duckduckgo import DuckDuckGoTools
from dotenv import load_dotenv
from tools import calculate, convert_temperature

load_dotenv()

agent = Agent(
    model=Gemini(id="gemini-2.5-flash"),
    tools=[DuckDuckGoTools(), calculate, convert_temperature],
    instructions=[
        "Você é um assistente inteligente com acesso a ferramentas.",
        "Use a ferramenta de busca para perguntas sobre fatos atuais.",
        "Use a calculadora para expressões matemáticas.",
        "Use o conversor de temperatura quando pedirem conversões.",
        "Sempre responda em português.",
    ],
    show_tool_calls=True,
    markdown=True,
)


# --- Interaction 1: Web search ---
print("=" * 60)
print("INTERAÇÃO 1: Busca na Web")
print("=" * 60)
agent.print_response(
    "Quais são as últimas novidades sobre inteligência artificial em 2025?",
    stream=True,
)

# --- Interaction 2: Calculator ---
print("\n" + "=" * 60)
print("INTERAÇÃO 2: Calculadora")
print("=" * 60)
agent.print_response(
    "Quanto é 15% de 1250? E qual é a raiz quadrada de 144?",
    stream=True,
)

# --- Interaction 3: Temperature conversion ---
print("\n" + "=" * 60)
print("INTERAÇÃO 3: Conversor de Temperatura")
print("=" * 60)
agent.print_response(
    "Converta 98.6°F para Celsius e também para Kelvin.",
    stream=True,
)

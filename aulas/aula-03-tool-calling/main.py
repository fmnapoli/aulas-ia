"""Aula 03: Tool Calling — Agente com ferramentas externas.

Demonstra como conectar um agente a ferramentas externas:
- DuckDuckGoTools: busca na web em tempo real
- calculate: calculadora customizada (decorator @tool)
- convert_temperature: conversor de temperatura customizado

O LLM decide automaticamente qual ferramenta usar com base na pergunta.
"""

from agno.agent import Agent
from agno.models.google import Gemini
from agno.tools.duckduckgo import DuckDuckGoTools
from dotenv import load_dotenv
from tools import calculate, convert_temperature

# Carrega variáveis de ambiente do arquivo .env (GOOGLE_API_KEY)
load_dotenv(override=True)

# Cria agente com 3 ferramentas: busca web + calculadora + conversor
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
    markdown=True,
)


# --- Interação 1: Busca na web ---
print("=" * 60)
print("INTERAÇÃO 1: Busca na Web")
print("=" * 60)
agent.print_response(
    "Quais são as últimas novidades sobre inteligência artificial em 2025?",
    stream=True,
)

# --- Interação 2: Calculadora ---
print("\n" + "=" * 60)
print("INTERAÇÃO 2: Calculadora")
print("=" * 60)
agent.print_response(
    "Quanto é 15% de 1250? E qual é a raiz quadrada de 144?",
    stream=True,
)

# --- Interação 3: Conversor de temperatura ---
print("\n" + "=" * 60)
print("INTERAÇÃO 3: Conversor de Temperatura")
print("=" * 60)
agent.print_response(
    "Converta 98.6°F para Celsius e também para Kelvin.",
    stream=True,
)

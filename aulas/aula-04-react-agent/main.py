"""Aula 04: Agente ReAct — Raciocínio + Ação no loop Think-Act-Observe.

Compara dois agentes:
1. Agente básico: responde diretamente usando ferramentas
2. Agente ReAct: raciocina passo a passo antes de agir (Think → Act → Observe)

O ReasoningTools adiciona capacidade de raciocínio explícito ao agente,
permitindo visualizar o processo de pensamento antes de cada ação.
"""

from agno.agent import Agent
from agno.models.google import Gemini
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.reasoning import ReasoningTools
from dotenv import load_dotenv

# Carrega variáveis de ambiente do arquivo .env (GOOGLE_API_KEY)
load_dotenv(override=True)


# --- Agente SEM raciocínio (baseline para comparação) ---

basic_agent = Agent(
    model=Gemini(id="gemini-2.5-flash"),
    tools=[DuckDuckGoTools()],
    instructions=[
        "Você é um assistente de pesquisa.",
        "Responda em português de forma completa e estruturada.",
    ],
    markdown=True,
)

# --- Agente COM ReasoningTools (padrão ReAct) ---

react_agent = Agent(
    model=Gemini(id="gemini-2.5-flash"),
    tools=[
        ReasoningTools(add_instructions=True),  # Adiciona capacidade de raciocínio
        DuckDuckGoTools(),
    ],
    instructions=[
        "Você é um assistente de pesquisa que raciocina passo a passo.",
        "Responda em português de forma completa e estruturada.",
    ],
    markdown=True,
)


# Pergunta de pesquisa para comparação
RESEARCH_QUESTION = (
    "Compare os frameworks Agno e LangGraph para desenvolvimento de agentes de IA. "
    "Quais são as vantagens e desvantagens de cada um? "
    "Qual seria mais indicado para um projeto de produção em 2025?"
)


# --- Comparação: sem raciocínio ---
print("=" * 60)
print("SEM ReasoningTools (resposta direta)")
print("=" * 60)
basic_agent.print_response(RESEARCH_QUESTION, stream=True)


# --- Comparação: com raciocínio (visibilidade total) ---
print("\n\n" + "=" * 60)
print("COM ReasoningTools (Think → Act → Observe)")
print("=" * 60)
react_agent.print_response(
    RESEARCH_QUESTION,
    stream=True,
    show_full_reasoning=True,  # Exibe os passos de raciocínio
)

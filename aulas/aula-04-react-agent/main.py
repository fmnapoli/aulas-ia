"""Aula 04: ReAct Agent — Reasoning + Acting in a Think-Act-Observe loop."""

from agno.agent import Agent
from agno.models.google import Gemini
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.reasoning import ReasoningTools
from dotenv import load_dotenv

load_dotenv()


# --- Agent WITHOUT reasoning (baseline) ---

basic_agent = Agent(
    model=Gemini(id="gemini-2.5-flash"),
    tools=[DuckDuckGoTools()],
    instructions=[
        "Você é um assistente de pesquisa.",
        "Responda em português de forma completa e estruturada.",
    ],
    show_tool_calls=True,
    markdown=True,
)

# --- Agent WITH ReasoningTools (ReAct pattern) ---

react_agent = Agent(
    model=Gemini(id="gemini-2.5-flash"),
    tools=[
        ReasoningTools(add_instructions=True),
        DuckDuckGoTools(),
    ],
    instructions=[
        "Você é um assistente de pesquisa que raciocina passo a passo.",
        "Responda em português de forma completa e estruturada.",
    ],
    show_tool_calls=True,
    markdown=True,
)


RESEARCH_QUESTION = (
    "Compare os frameworks Agno e LangGraph para desenvolvimento de agentes de IA. "
    "Quais são as vantagens e desvantagens de cada um? "
    "Qual seria mais indicado para um projeto de produção em 2025?"
)


# --- Comparison: without reasoning ---
print("=" * 60)
print("SEM ReasoningTools (resposta direta)")
print("=" * 60)
basic_agent.print_response(RESEARCH_QUESTION, stream=True)


# --- Comparison: with reasoning (full visibility) ---
print("\n\n" + "=" * 60)
print("COM ReasoningTools (Think → Act → Observe)")
print("=" * 60)
react_agent.print_response(
    RESEARCH_QUESTION,
    stream=True,
    show_full_reasoning=True,
)

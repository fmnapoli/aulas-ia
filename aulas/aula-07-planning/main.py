from agno.agent import Agent
from agno.models.google import Gemini
from agno.tools.duckduckgo import DuckDuckGoTools
from dotenv import load_dotenv

load_dotenv()

planner = Agent(
    model=Gemini(id="gemini-2.5-flash"),
    reasoning=True,
    tools=[DuckDuckGoTools()],
    instructions=[
        "Você é um analista que decompõe tarefas complexas em subtarefas.",
        "Sempre planeje antes de agir.",
        "Pesquise na web para obter dados atualizados.",
        "Apresente resultados estruturados em português.",
    ],
    show_full_reasoning=True,
    markdown=True,
)

print("=== Tarefa Complexa com Planejamento ===\n")
planner.print_response(
    "Compare os frameworks Agno, LangChain e CrewAI para desenvolvimento de agentes de IA. "
    "Para cada um, pesquise: facilidade de uso, performance, e comunidade. "
    "No final, dê uma recomendação.",
    stream=True,
)

"""Aula 07: Planejamento e Decomposição — Agente que planeja antes de agir.

Demonstra como um agente decompõe tarefas complexas em subtarefas menores:
- ReasoningTools: raciocínio explícito passo a passo (chain-of-thought)
- DuckDuckGoTools: busca na web para obter dados atualizados
- show_full_reasoning: exibe o processo de raciocínio completo

O agente planeja a pesquisa, executa buscas para cada subtópico
e sintetiza os resultados em uma análise comparativa.
"""

from agno.agent import Agent
from agno.models.google import Gemini
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.reasoning import ReasoningTools
from dotenv import load_dotenv

# Carrega variáveis de ambiente do arquivo .env (GOOGLE_API_KEY)
load_dotenv(override=True)

# Cria agente planejador com raciocínio e busca web
planner = Agent(
    model=Gemini(id="gemini-2.5-flash"),
    tools=[
        ReasoningTools(add_instructions=True),  # Raciocínio passo a passo
        DuckDuckGoTools(),  # Busca na web
    ],
    instructions=[
        "Você é um analista que decompõe tarefas complexas em subtarefas.",
        "Sempre planeje antes de agir.",
        "Pesquise na web para obter dados atualizados.",
        "Apresente resultados estruturados em português.",
    ],
    markdown=True,
)

# Tarefa complexa que exige planejamento e múltiplas buscas
print("=== Tarefa Complexa com Planejamento ===\n")
planner.print_response(
    "Compare os frameworks Agno, LangChain e CrewAI para desenvolvimento de agentes de IA. "
    "Para cada um, pesquise: facilidade de uso, performance, e comunidade. "
    "No final, dê uma recomendação.",
    stream=True,
    show_full_reasoning=True,  # Exibe o processo de raciocínio
)

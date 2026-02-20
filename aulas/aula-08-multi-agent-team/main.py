"""Aula 08: Multi-Agent Team — Equipe de agentes especializados.

Demonstra como criar um Team (equipe) de agentes com papéis distintos:
- Researcher: pesquisa informações na web usando DuckDuckGoTools
- Writer: escreve conteúdo estruturado em português

O Team usa TeamMode.coordinate, onde um líder coordena a delegação
de tarefas para cada agente especializado e sintetiza o resultado final.
"""

from agno.agent import Agent
from agno.models.google import Gemini
from agno.team import Team
from agno.team.mode import TeamMode
from agno.tools.duckduckgo import DuckDuckGoTools
from dotenv import load_dotenv

# Carrega variáveis de ambiente do arquivo .env (GOOGLE_API_KEY)
load_dotenv(override=True)

# Modelo compartilhado entre todos os agentes
model = Gemini(id="gemini-2.5-flash")

# Agente pesquisador: busca informações na web
researcher = Agent(
    name="Researcher",
    role="Pesquisar informações atualizadas na web",
    model=model,
    tools=[DuckDuckGoTools()],
    instructions="Pesquise na web e forneça informações factuais e atualizadas.",
)

# Agente redator: escreve conteúdo estruturado
writer = Agent(
    name="Writer",
    role="Escrever conteúdo claro e estruturado em português",
    model=model,
    instructions=[
        "Escreva conteúdo bem estruturado em português.",
        "Use formatação Markdown com cabeçalhos e listas.",
        "Seja conciso mas informativo.",
    ],
)

# Cria o Team com modo de coordenação
team = Team(
    name="Content Team",
    model=model,
    members=[researcher, writer],
    mode=TeamMode.coordinate,  # Líder coordena a delegação de tarefas
    instructions=[
        "Você coordena uma equipe de pesquisa e redação.",
        "Primeiro, delegue a pesquisa ao Researcher.",
        "Depois, delegue a redação ao Writer com base nos achados.",
        "Sintetize o resultado final.",
    ],
    markdown=True,
)

# Executa a tarefa com o Team coordenado
print("=== Team Coordenado ===\n")
team.print_response(
    "Crie um resumo sobre as tendências de IA em 2026, "
    "incluindo agentes autônomos e modelos multimodais.",
    stream=True,
)

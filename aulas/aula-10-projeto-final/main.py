from dotenv import load_dotenv
from agno.models.google import Gemini
from agno.team import Team
from agno.team.mode import TeamMode

from agents import researcher, analyst, writer

load_dotenv()

research_team = Team(
    name="Research Assistant",
    model=Gemini(id="gemini-2.5-flash"),
    members=[researcher, analyst, writer],
    mode=TeamMode.coordinate,
    instructions=[
        "You lead a research team that produces structured reports.",
        "1. First, delegate to Researcher to find sources on the topic.",
        "2. Then, delegate to Analyst to analyze and cross-reference findings.",
        "3. Finally, delegate to Writer to produce a structured report in Portuguese.",
        "Ensure the final output is a complete, well-structured research report.",
    ],
    markdown=True,
)

print("=== Assistente de Pesquisa ===\n")
print("Tema: O estado atual dos agentes de IA em 2026\n")

research_team.print_response(
    "Pesquise sobre o estado atual dos agentes de IA em 2026. "
    "Inclua: principais frameworks, casos de uso em produção, "
    "desafios atuais e tendências futuras.",
    stream=True,
)

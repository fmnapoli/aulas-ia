from agno.agent import Agent
from agno.models.google import Gemini
from agno.team import Team
from agno.team.mode import TeamMode
from agno.tools.duckduckgo import DuckDuckGoTools
from dotenv import load_dotenv

load_dotenv()

model = Gemini(id="gemini-2.5-flash")

researcher = Agent(
    name="Researcher",
    role="Search the web for current information",
    model=model,
    tools=[DuckDuckGoTools()],
    instructions="Search the web and provide factual, up-to-date information.",
)

writer = Agent(
    name="Writer",
    role="Write clear, structured content in Portuguese",
    model=model,
    instructions=[
        "Write well-structured content in Portuguese.",
        "Use markdown formatting with headers and bullet points.",
        "Be concise but informative.",
    ],
)

team = Team(
    name="Content Team",
    model=model,
    members=[researcher, writer],
    mode=TeamMode.coordinate,
    instructions=[
        "You coordinate a research and writing team.",
        "First, delegate research to the Researcher.",
        "Then, delegate writing to the Writer based on research findings.",
        "Synthesize the final output.",
    ],
    markdown=True,
)

print("=== Team Coordenado ===\n")
team.print_response(
    "Crie um resumo sobre as tendências de IA em 2026, "
    "incluindo agentes autônomos e modelos multimodais.",
    stream=True,
)

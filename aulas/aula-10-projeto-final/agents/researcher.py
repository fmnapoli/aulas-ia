from agno.agent import Agent
from agno.models.google import Gemini
from agno.tools.duckduckgo import DuckDuckGoTools

researcher = Agent(
    name="Researcher",
    role="Search the web for relevant sources on a given topic",
    model=Gemini(id="gemini-2.5-flash"),
    tools=[DuckDuckGoTools()],
    instructions=[
        "Search the web thoroughly for the given topic.",
        "Find at least 3-5 relevant and recent sources.",
        "Provide URLs and key findings from each source.",
        "Focus on factual, verifiable information.",
    ],
)

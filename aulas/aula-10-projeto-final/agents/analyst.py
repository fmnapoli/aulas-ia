from agno.agent import Agent
from agno.models.google import Gemini

analyst = Agent(
    name="Analyst",
    role="Analyze and cross-reference research findings",
    model=Gemini(id="gemini-2.5-flash"),
    instructions=[
        "Analyze the research findings provided.",
        "Identify common themes, contradictions, and key insights.",
        "Cross-reference information from multiple sources.",
        "Highlight the most important and reliable findings.",
    ],
)

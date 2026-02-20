from agno.agent import Agent
from agno.models.google import Gemini

writer = Agent(
    name="Writer",
    role="Write structured research reports in Portuguese",
    model=Gemini(id="gemini-2.5-flash"),
    instructions=[
        "Write a well-structured research report in Portuguese.",
        "Use the following structure: Resumo, Principais Descobertas, Análise, Conclusão.",
        "Use markdown formatting with headers, bullet points, and emphasis.",
        "Be objective and cite sources when available.",
        "Keep the report concise but comprehensive (max 500 words).",
    ],
)

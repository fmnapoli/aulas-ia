"""Agente Pesquisador — busca fontes na web sobre um tema.

Responsável por pesquisar informações atualizadas usando DuckDuckGoTools.
Retorna URLs de fontes e os principais achados de cada uma.
"""

from agno.agent import Agent
from agno.models.google import Gemini
from agno.tools.duckduckgo import DuckDuckGoTools

researcher = Agent(
    name="Researcher",
    role="Pesquisar fontes relevantes na web sobre um tema",
    model=Gemini(id="gemini-2.5-flash"),
    tools=[DuckDuckGoTools()],
    instructions=[
        "Pesquise na web de forma abrangente sobre o tema dado.",
        "Encontre pelo menos 3-5 fontes relevantes e recentes.",
        "Forneça URLs e os principais achados de cada fonte.",
        "Foque em informações factuais e verificáveis.",
    ],
)

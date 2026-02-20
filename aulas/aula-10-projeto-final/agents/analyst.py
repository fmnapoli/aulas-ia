"""Agente Analista — analisa e cruza referências das fontes pesquisadas.

Responsável por identificar temas comuns, contradições e insights-chave
a partir dos dados coletados pelo Pesquisador.
"""

from agno.agent import Agent
from agno.models.google import Gemini

analyst = Agent(
    name="Analyst",
    role="Analisar e cruzar referências dos achados da pesquisa",
    model=Gemini(id="gemini-2.5-flash"),
    instructions=[
        "Analise os achados da pesquisa fornecidos.",
        "Identifique temas comuns, contradições e insights-chave.",
        "Cruze informações de múltiplas fontes.",
        "Destaque os achados mais importantes e confiáveis.",
    ],
)

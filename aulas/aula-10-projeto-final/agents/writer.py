"""Agente Redator — escreve relatórios de pesquisa estruturados em português.

Responsável por produzir o relatório final com base na análise,
seguindo uma estrutura padronizada: Resumo, Descobertas, Análise, Conclusão.
"""

from agno.agent import Agent
from agno.models.google import Gemini

writer = Agent(
    name="Writer",
    role="Escrever relatórios de pesquisa estruturados em português",
    model=Gemini(id="gemini-2.5-flash"),
    instructions=[
        "Escreva um relatório de pesquisa bem estruturado em português.",
        "Use a seguinte estrutura: Resumo, Principais Descobertas, Análise, Conclusão.",
        "Use formatação Markdown com cabeçalhos, listas e ênfase.",
        "Seja objetivo e cite fontes quando disponíveis.",
        "Mantenha o relatório conciso mas abrangente (máximo 500 palavras).",
    ],
)

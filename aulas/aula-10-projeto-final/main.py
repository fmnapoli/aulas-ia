"""Aula 10: Projeto Final — Assistente de Pesquisa com Team multi-agente.

Combina todos os conceitos do curso em um sistema completo:
- Team com TeamMode.coordinate para orquestração
- Researcher: busca fontes na web (Tool Calling)
- Analyst: analisa e cruza referências
- Writer: produz relatório estruturado em português

Pipeline: Tema → Researcher (busca) → Analyst (análise) → Writer (relatório) → Resultado
"""

from dotenv import load_dotenv

from agno.models.google import Gemini
from agno.team import Team
from agno.team.mode import TeamMode
from agents import analyst, researcher, writer

# Carrega variáveis de ambiente do arquivo .env (GOOGLE_API_KEY)
load_dotenv(override=True)

# Cria o Team de pesquisa com 3 agentes especializados
research_team = Team(
    name="Research Assistant",
    model=Gemini(id="gemini-2.5-flash"),
    members=[researcher, analyst, writer],
    mode=TeamMode.coordinate,  # Líder coordena a delegação de tarefas
    instructions=[
        "Você lidera uma equipe de pesquisa que produz relatórios estruturados.",
        "1. Primeiro, delegue ao Researcher para buscar fontes sobre o tema.",
        "2. Depois, delegue ao Analyst para analisar e cruzar referências.",
        "3. Por fim, delegue ao Writer para produzir um relatório em português.",
        "Garanta que o resultado final seja um relatório completo e bem estruturado.",
    ],
    markdown=True,
)

# Executa a pesquisa completa
print("=== Assistente de Pesquisa ===\n")
print("Tema: O estado atual dos agentes de IA em 2026\n")

research_team.print_response(
    "Pesquise sobre o estado atual dos agentes de IA em 2026. "
    "Inclua: principais frameworks, casos de uso em produção, "
    "desafios atuais e tendências futuras.",
    stream=True,
)

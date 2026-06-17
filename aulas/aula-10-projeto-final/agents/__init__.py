"""Pacote de agentes especializados para o Assistente de Pesquisa.

Exporta os três agentes que compõem o Team:
- researcher: pesquisa fontes na web
- analyst: analisa e cruza referências
- writer: escreve o relatório final
"""

from agents.analyst import analyst
from agents.researcher import researcher
from agents.writer import writer

__all__ = ["researcher", "analyst", "writer"]

"""Aula 01: Olá, Agente! — Primeiro agente conversacional com Agno.

Demonstra a criação de um agente básico usando o framework Agno
com o modelo Google Gemini. O agente responde a perguntas simples
em português, com streaming e formatação Markdown.
"""

from dotenv import load_dotenv

from agno.agent import Agent
from agno.models.google import Gemini

# Carrega variáveis de ambiente do arquivo .env (GOOGLE_API_KEY)
load_dotenv(override=True)

# Cria o agente com modelo Gemini, instruções em português e saída em Markdown
agent = Agent(
    model=Gemini(id="gemini-2.5-flash"),
    instructions="Você é um assistente simpático e prestativo. Responda em português.",
    markdown=True,
)

# Primeira interação: saudação simples
agent.print_response("Olá! Quem é você e o que você pode fazer?", stream=True)

print("\n---\n")

# Segunda interação: pergunta sobre agentes de IA
agent.print_response("Explique em 3 frases o que é um agente de IA.", stream=True)

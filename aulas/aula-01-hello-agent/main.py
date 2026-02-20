"""Aula 01: Olá, Agente! — Primeiro agente conversacional com Agno."""

from dotenv import load_dotenv

from agno.agent import Agent
from agno.models.google import Gemini

load_dotenv()

agent = Agent(
    model=Gemini(id="gemini-2.5-flash"),
    instructions="Você é um assistente simpático e prestativo. Responda em português.",
    markdown=True,
)

# First interaction: a simple greeting
agent.print_response("Olá! Quem é você e o que você pode fazer?", stream=True)

print("\n---\n")

# Second interaction: demonstrate the agent answering a question
agent.print_response(
    "Explique em 3 frases o que é um agente de IA.", stream=True
)

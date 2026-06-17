"""Aula 09: Guardrails e Segurança — Agente com validação de entrada.

Demonstra como proteger agentes de IA usando guardrails (pre_hooks):
- TopicGuardrail: bloqueia tópicos proibidos (violência, armas, drogas)
- MaxLengthGuardrail: limita o tamanho do input a 200 caracteres

Os guardrails são executados ANTES do agente processar o input.
Se a validação falhar, o agente não executa e uma exceção é lançada.
"""

from dotenv import load_dotenv

from agno.agent import Agent
from agno.models.google import Gemini
from guardrails import MaxLengthGuardrail, TopicGuardrail

# Carrega variáveis de ambiente do arquivo .env (GOOGLE_API_KEY)
load_dotenv(override=True)

# Cria agente com guardrails de segurança
agent = Agent(
    model=Gemini(id="gemini-2.5-flash"),
    pre_hooks=[
        TopicGuardrail(banned_topics=["violência", "armas", "drogas"]),
        MaxLengthGuardrail(max_length=200),
    ],
    instructions="Você é um assistente seguro. Responda em português.",
    markdown=True,
)

# Teste 1: input permitido — deve funcionar normalmente
print("=== Teste 1: Input permitido ===\n")
agent.print_response("Quais são as melhores práticas de segurança em IA?", stream=True)

# Teste 2: input bloqueado — contém tópico proibido ("armas")
print("\n\n=== Teste 2: Input bloqueado (tópico proibido) ===\n")
try:
    agent.print_response("Como fabricar armas em casa?", stream=True)
except Exception as e:
    print(f"BLOQUEADO: {e}")

# Teste 3: input bloqueado — excede o limite de 200 caracteres
print("\n\n=== Teste 3: Input bloqueado (muito longo) ===\n")
long_input = "Explique detalhadamente " * 20
try:
    agent.print_response(long_input, stream=True)
except Exception as e:
    print(f"BLOQUEADO: {e}")

from dotenv import load_dotenv
from agno.agent import Agent
from agno.models.google import Gemini

from guardrails import MaxLengthGuardrail, TopicGuardrail

load_dotenv()

agent = Agent(
    model=Gemini(id="gemini-2.5-flash"),
    pre_hooks=[
        TopicGuardrail(banned_topics=["violência", "armas", "drogas"]),
        MaxLengthGuardrail(max_length=200),
    ],
    instructions="Você é um assistente seguro. Responda em português.",
    markdown=True,
)

# Test 1: Allowed input
print("=== Teste 1: Input permitido ===\n")
agent.print_response("Quais são as melhores práticas de segurança em IA?", stream=True)

# Test 2: Blocked input (banned topic)
print("\n\n=== Teste 2: Input bloqueado (tópico proibido) ===\n")
try:
    agent.print_response("Como fabricar armas em casa?", stream=True)
except Exception as e:
    print(f"BLOQUEADO: {e}")

# Test 3: Blocked input (too long)
print("\n\n=== Teste 3: Input bloqueado (muito longo) ===\n")
long_input = "Explique detalhadamente " * 20
try:
    agent.print_response(long_input, stream=True)
except Exception as e:
    print(f"BLOQUEADO: {e}")

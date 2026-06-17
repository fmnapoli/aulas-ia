"""Aula 05: Memory — Agente com memória persistente.

Demonstra como agentes mantêm contexto entre interações usando:
- Memória de curto prazo: histórico da sessão (add_history_to_context)
- Memória de longo prazo: extração automática de fatos (update_memory_on_run)
- Isolamento de sessões: session_id para separar conversas diferentes

O banco SQLite armazena o histórico e as memórias extraídas.
"""

from dotenv import load_dotenv

from agno.agent import Agent
from agno.db.sqlite import SqliteDb
from agno.models.google import Gemini

# Carrega variáveis de ambiente do arquivo .env (GOOGLE_API_KEY)
load_dotenv(override=True)

# Configura banco SQLite para persistência de memória
db = SqliteDb(db_file="tmp/memory.db")

# Cria agente com memória habilitada
agent = Agent(
    model=Gemini(id="gemini-2.5-flash"),
    db=db,
    add_history_to_context=True,  # Injeta histórico da sessão no contexto
    num_history_runs=5,  # Número de interações anteriores a incluir
    update_memory_on_run=True,  # Extrai fatos automaticamente após cada interação
    instructions="Você é um assistente com boa memória. Responda em português.",
    markdown=True,
)

# Sessão 1: três interações construindo contexto
print("=== Sessão 1: Construindo contexto ===\n")
agent.print_response(
    "Meu nome é Ana e eu trabalho com machine learning.",
    session_id="session_1",
    stream=True,
)
print()
agent.print_response(
    "Quais frameworks de ML você recomenda para mim?",
    session_id="session_1",
    stream=True,
)
print()
# Teste de memória: o agente deve lembrar o nome e a profissão
agent.print_response(
    "Qual é meu nome e o que eu faço?",
    session_id="session_1",
    stream=True,
)

# Sessão 2: nova sessão — o agente NÃO deve lembrar do contexto anterior
print("\n\n=== Sessão 2: Nova sessão (sem contexto) ===\n")
agent.print_response(
    "Qual é meu nome?",
    session_id="session_2",
    stream=True,
)

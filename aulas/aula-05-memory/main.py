from dotenv import load_dotenv
from agno.agent import Agent
from agno.models.google import Gemini
from agno.db.sqlite import SqliteDb

load_dotenv()

db = SqliteDb(db_file="tmp/memory.db")

agent = Agent(
    model=Gemini(id="gemini-2.5-flash"),
    db=db,
    add_history_to_context=True,
    num_history_runs=5,
    update_memory_on_run=True,
    instructions="Você é um assistente com boa memória. Responda em português.",
    markdown=True,
)

# Session 1: 3 interactions building context
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
agent.print_response(
    "Qual é meu nome e o que eu faço?",
    session_id="session_1",
    stream=True,
)

# Session 2: New session — agent should NOT remember session context
print("\n\n=== Sessão 2: Nova sessão (sem contexto) ===\n")
agent.print_response(
    "Qual é meu nome?",
    session_id="session_2",
    stream=True,
)

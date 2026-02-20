from dotenv import load_dotenv
from agno.agent import Agent
from agno.models.google import Gemini
from agno.knowledge.embedder.google import GeminiEmbedder
from agno.knowledge.knowledge import Knowledge
from agno.knowledge.reader.markdown import MarkdownReader
from agno.vectordb.lancedb import LanceDb, SearchType

load_dotenv()

knowledge = Knowledge(
    vector_db=LanceDb(
        table_name="course_docs",
        uri="tmp/lancedb",
        search_type=SearchType.vector,
        embedder=GeminiEmbedder(),
    ),
)

# Load markdown documents into the vector database
knowledge.insert(path="docs/python-guide.md", reader=MarkdownReader())
knowledge.insert(path="docs/agno-overview.md", reader=MarkdownReader())

agent = Agent(
    model=Gemini(id="gemini-2.5-flash"),
    knowledge=knowledge,
    search_knowledge=True,
    instructions="Responda em português usando a base de conhecimento quando relevante.",
    markdown=True,
)

# Query the knowledge base
print("=== Pergunta 1: Boas práticas Python ===\n")
agent.print_response("Quais são as melhores práticas de Python?", stream=True)

print("\n\n=== Pergunta 2: Framework Agno ===\n")
agent.print_response(
    "O que é o framework Agno e quais são seus recursos?", stream=True
)

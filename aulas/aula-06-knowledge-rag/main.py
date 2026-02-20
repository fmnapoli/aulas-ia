"""Aula 06: Knowledge + RAG — Agente que consulta base de conhecimento.

Demonstra Retrieval Augmented Generation (RAG):
1. Carrega documentos Markdown em um vector database (LanceDb)
2. Gera embeddings com GeminiEmbedder para busca por similaridade
3. O agente consulta a base de conhecimento automaticamente ao responder

Pipeline: Documentos → Embeddings → VectorDB → Query → Chunks relevantes → Agente → Resposta
"""

from dotenv import load_dotenv

from agno.agent import Agent
from agno.knowledge.embedder.google import GeminiEmbedder
from agno.knowledge.knowledge import Knowledge
from agno.knowledge.reader.markdown_reader import MarkdownReader
from agno.models.google import Gemini
from agno.vectordb.lancedb import LanceDb, SearchType

# Carrega variáveis de ambiente do arquivo .env (GOOGLE_API_KEY)
load_dotenv(override=True)

# Configura a base de conhecimento com LanceDb como vector database
knowledge = Knowledge(
    vector_db=LanceDb(
        table_name="course_docs",
        uri="tmp/lancedb",
        search_type=SearchType.vector,  # Busca por similaridade vetorial
        embedder=GeminiEmbedder(),  # Gera embeddings via Google Gemini
    ),
)

# Carrega documentos Markdown na base de conhecimento
knowledge.insert(path="docs/python-guide.md", reader=MarkdownReader())
knowledge.insert(path="docs/agno-overview.md", reader=MarkdownReader())

# Cria agente com acesso à base de conhecimento
agent = Agent(
    model=Gemini(id="gemini-2.5-flash"),
    knowledge=knowledge,
    search_knowledge=True,  # Habilita busca automática na base
    instructions="Responda em português usando a base de conhecimento quando relevante.",
    markdown=True,
)

# Consulta 1: busca informações sobre Python na base
print("=== Pergunta 1: Boas práticas Python ===\n")
agent.print_response("Quais são as melhores práticas de Python?", stream=True)

# Consulta 2: busca informações sobre Agno na base
print("\n\n=== Pergunta 2: Framework Agno ===\n")
agent.print_response("O que é o framework Agno e quais são seus recursos?", stream=True)

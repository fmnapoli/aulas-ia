# Visão Geral do Framework Agno

## O que é o Agno?

- **Agno** é um framework Python para construir agentes de IA multi-modais e sistemas multi-agentes
- Projetado para ser **leve e rápido** — criação de agentes em microssegundos, sem overhead de frameworks pesados
- Suporta **múltiplos provedores de LLM**: OpenAI, Google Gemini, Anthropic, Ollama, entre outros
- Licença **open-source** com comunidade ativa no GitHub

## Recursos Principais

- **Tool Calling** — conecte agentes a ferramentas externas como busca web, APIs, bancos de dados e código Python
- **Structured Output** — force o agente a retornar dados tipados usando schemas Pydantic em vez de texto livre
- **Memory** — memória persistente com suporte a SQLite e PostgreSQL para conversas multi-turno
- **Knowledge + RAG** — integre bases de conhecimento com vector databases (LanceDB, PgVector) para Retrieval Augmented Generation
- **Multi-Agent Teams** — crie equipes de agentes que colaboram, delegam tarefas e compartilham contexto

## Arquitetura

- Baseado em **composição** — cada recurso (tools, memory, knowledge) é um componente plugável
- Suporta **streaming** nativo para respostas em tempo real
- **Session management** — controle de sessões com session_id para isolamento de contexto
- Integra com **embedders** de diferentes provedores para geração de vetores semânticos

## Casos de Uso

- Chatbots com memória persistente e personalidade configurável
- Agentes de pesquisa que consultam documentos via RAG
- Sistemas de análise que retornam dados estruturados
- Pipelines multi-agente para tarefas complexas com planejamento e delegação

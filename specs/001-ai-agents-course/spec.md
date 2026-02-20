# Feature Specification: Curso Prático de Desenvolvimento de Agentes de IA

**Feature Branch**: `001-ai-agents-course`  
**Created**: 2026-02-19  
**Status**: Draft  
**Input**: User description: "Criar um curso rápido sobre desenvolvimento de agentes de IA, usando as tecnologias atuais 2026 - cursos com exemplos práticos a cada aula (que não deve ser muito longa)"

## Clarifications

### Session 2026-02-19

- Q: Qual framework principal para os exemplos do curso? → A: Agno (https://agno.com) — framework open-source Python para agentes com suporte nativo a memory, knowledge, tools, guardrails, teams, workflows e multi-agent systems.
- Q: Qual provedor de LLM padrão nos exemplos? → A: Google Gemini (gemini-2.5-flash) diretamente via Google AI API. Free tier generoso, sem cartão de crédito para começar.
- Q: O que fica explicitamente fora de escopo? → A: Deploy em produção, fine-tuning de modelos, modelos locais (Ollama), frontend/UI, MLOps.
- Q: Qual o tema do projeto final (Aula 10)? → A: Assistente de pesquisa — Team de agentes que busca na web, analisa fontes e gera relatório estruturado.
- Q: Idioma do conteúdo escrito das aulas? → A: Português para texto (READMEs, teoria, explicações), inglês para código (variáveis, funções, comentários inline).

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Aluno Inicia e Conclui uma Aula Prática (Priority: P1)

Um desenvolvedor com experiência básica em programação quer aprender a construir agentes de IA. Ele acessa uma aula do curso, lê o conteúdo teórico (máximo 15 minutos de leitura), e em seguida executa o exemplo prático completo na sua máquina local usando o framework Agno. Ao final da aula, ele tem um agente funcional que pode demonstrar.

**Why this priority**: Esta é a experiência central do curso. Se um aluno não consegue completar uma aula prática de forma autônoma, o curso falha no seu propósito fundamental. Cada aula deve ser uma unidade independente de aprendizado com resultado tangível.

**Independent Test**: Pode ser testado dando a aula a um desenvolvedor júnior e verificando se ele consegue seguir as instruções e ter o agente funcionando em até 45 minutos.

**Acceptance Scenarios**:

1. **Given** um aluno com Python 3.11+ instalado e uma API key gratuita do Google Gemini, **When** ele segue as instruções da Aula 01, **Then** ele tem um agente conversacional Agno funcional rodando localmente em até 30 minutos
2. **Given** um aluno que completou a aula anterior, **When** ele inicia a próxima aula, **Then** o contexto da aula anterior é revisado em no máximo 2 minutos antes de avançar
3. **Given** um aluno que encontra um erro durante o exemplo prático, **When** ele consulta a seção de troubleshooting da aula, **Then** ele encontra a solução para os 5 erros mais comuns daquele exercício

---

### User Story 2 - Aluno Constrói um Agente Multi-Tool Completo (Priority: P2)

Ao longo do curso, o aluno progride de agentes simples (Agent) para agentes com ferramentas (tools), memória (memory/knowledge), e sistemas multi-agente (Team). No final do curso, ele tem um sistema multi-agent funcional usando Agno que resolve problemas reais.

**Why this priority**: A progressão de complexidade é o que transforma o curso de uma coleção de tutoriais em uma jornada de aprendizado coesa. Os alunos precisam sentir que estão construindo algo cada vez mais poderoso.

**Independent Test**: Pode ser testado verificando se o agente final do aluno consegue executar uma tarefa que requer pelo menos 3 ferramentas diferentes em sequência.

**Acceptance Scenarios**:

1. **Given** um aluno que completou as aulas 1 a 4, **When** ele inicia a aula sobre tool-calling, **Then** ele entende como conectar um Agent Agno a ferramentas externas e constrói um agente que busca informações na web
2. **Given** um aluno que completou todas as aulas, **When** ele executa o projeto final, **Then** ele tem um assistente de pesquisa com Team (buscador + analista + redator) que recebe um tema, pesquisa na web, analisa fontes e gera um relatório estruturado

---

### User Story 3 - Instrutor Adapta o Conteúdo para sua Audiência (Priority: P3)

Um instrutor ou líder técnico quer usar o material do curso em treinamentos internos ou workshops. Ele consegue entender a estrutura modular das aulas, selecionar quais módulos usar, e adaptar os exemplos para o contexto da sua organização.

**Why this priority**: A reusabilidade do material amplia o impacto do curso além do aluno individual. Porém, o foco principal é a experiência do aluno.

**Independent Test**: Pode ser testado pedindo a um instrutor que selecione 3 aulas para um workshop de meio dia e verifique se o material é auto-contido o suficiente para funcionar fora de ordem.

**Acceptance Scenarios**:

1. **Given** um instrutor com acesso ao repositório do curso, **When** ele seleciona aulas individuais, **Then** cada aula tem dependências claramente documentadas e pode ser adaptada independentemente

---

### Edge Cases

- O que acontece quando o aluno não tem acesso a uma API key paga? (Deve haver alternativas gratuitas ou com free tier documentadas)
- Como o curso lida com mudanças rápidas nos SDKs e frameworks de IA? (Versionamento claro do Agno e notas de atualização)
- O que acontece se o aluno tenta executar os exemplos em um ambiente sem GPU? (Todos os exemplos devem rodar em CPU, usando APIs de LLM na nuvem)
- Como o curso lida com alunos que não falam inglês fluentemente? (Texto em português, código em inglês — padrão de cursos técnicos brasileiros)

## Out of Scope

- Deploy em produção (cloud, containers, serverless)
- Fine-tuning de modelos de linguagem
- Modelos locais (Ollama, llama.cpp, etc.)
- Frontend/UI (React, Streamlit, Gradio, etc.)
- Treinamento ou pré-treinamento de modelos
- Infraestrutura de MLOps / pipelines de dados

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: O curso DEVE conter entre 8 e 12 aulas, cada uma completável em no máximo 45 minutos (15 min teoria + 30 min prática)
- **FR-002**: Cada aula DEVE produzir um artefato funcional (agente, ferramenta, ou componente) que o aluno pode executar localmente
- **FR-003**: O curso DEVE seguir uma progressão de complexidade: fundamentos → agentes simples → tools → memória → orquestração → multi-agente → projeto final
- **FR-004**: Cada aula DEVE incluir: objetivo claro, conceito teórico breve, exemplo prático completo com código, exercício desafio opcional, e troubleshooting dos erros comuns
- **FR-005**: O curso DEVE usar Agno (https://agno.com) como framework principal para todos os exemplos de agentes, aproveitando seus recursos nativos: Agent, Team, Workflow, Memory, Knowledge, Tools e Guardrails
- **FR-006**: Todos os exemplos DEVEM usar Google Gemini (gemini-2.5-flash) como modelo padrão via Google AI API, aproveitando o free tier generoso (sem cartão de crédito). Custo total < $5 para completar o curso
- **FR-007**: O repositório DEVE conter o código completo de cada aula em diretórios separados, com README individual e requirements.txt/pyproject.toml
- **FR-008**: O curso DEVE cobrir os padrões fundamentais de agentes de IA: ReAct, tool-calling, RAG, memória conversacional, planejamento, e orquestração multi-agente
- **FR-009**: Cada aula DEVE incluir um diagrama ou ilustração que explique visualmente o conceito sendo ensinado
- **FR-010**: O curso DEVE incluir um projeto final integrativo que combine pelo menos 3 padrões aprendidos nas aulas anteriores

### Key Entities

- **Aula (Lesson)**: Unidade de aprendizado com número sequencial, título, objetivo, conteúdo teórico, exemplo prático, exercício desafio e troubleshooting. Cada aula pertence a um módulo temático.
- **Agent**: Classe principal do Agno. Artefato de software produzido em cada aula. Tem model, tools, instructions, knowledge e memory.
- **Team**: Classe Agno para orquestração multi-agente. Composta por múltiplos Agent members com coordenação automática.
- **Tool**: Capacidade externa conectada a um Agent. Tem uma interface definida (input/output), descrição, e implementação.
- **Knowledge**: Sistema do Agno para RAG. Permite ao Agent consultar bases de conhecimento (documentos, embeddings).
- **Memory**: Sistema do Agno para persistência de contexto conversacional e aprendizado ao longo de sessões.
- **Módulo (Module)**: Agrupamento temático de 2-3 aulas relacionadas (ex: "Fundamentos", "Ferramentas", "Orquestração").

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: 90% dos alunos que iniciam uma aula conseguem completar o exemplo prático com sucesso na primeira tentativa seguindo as instruções
- **SC-002**: O tempo médio para completar cada aula é de no máximo 45 minutos (incluindo setup inicial na primeira aula)
- **SC-003**: Cada aula produz um agente ou componente que funciona de forma independente e pode ser demonstrado em menos de 2 minutos
- **SC-004**: O custo total de API para um aluno completar todas as aulas do curso é inferior a $5 USD
- **SC-005**: O curso cobre pelo menos 6 dos 8 padrões fundamentais de agentes de IA reconhecidos pela comunidade (ReAct, tool-calling, RAG, memória, planejamento, multi-agente, reflexão, human-in-the-loop)
- **SC-006**: 80% dos alunos que completam o curso conseguem construir um agente multi-tool funcional no projeto final sem assistência adicional

## Assumptions

- Os alunos têm experiência básica em programação (Python nível intermediário) e familiaridade com linha de comando
- Os alunos têm acesso a um computador com internet e podem instalar software localmente (Python, pip/uv, editor de código)
- Google Gemini API continuará oferecendo free tier em 2026 via Google AI Studio
- O curso será distribuído como repositório Git público, com conteúdo em Markdown (português) e código Python (inglês)
- Python continua sendo a linguagem dominante para desenvolvimento de agentes de IA em 2026
- Agno está estável e com API consolidada em 2026, com documentação em https://docs.agno.com

## Proposed Course Structure

### Módulo 1: Fundamentos
- **Aula 01**: Olá, Agente! — Primeiro Agent Agno conversacional (conceitos de LLM, prompt, API)
- **Aula 02**: Prompt Engineering para Agentes — System prompts (instructions), few-shot, structured output

### Módulo 2: Ferramentas e Ações
- **Aula 03**: Tool Calling — Agent com tools (busca web, calculadora)
- **Aula 04**: Agente ReAct — Raciocínio + Ação em loop (Thought → Action → Observation)

### Módulo 3: Memória e Contexto
- **Aula 05**: Memory — Agent com memória conversacional e contexto persistente
- **Aula 06**: Knowledge + RAG — Agent que consulta base de conhecimento com embeddings

### Módulo 4: Orquestração Avançada
- **Aula 07**: Planejamento e Decomposição — Agent que quebra tarefas complexas em subtarefas
- **Aula 08**: Team (Multi-Agent) — Múltiplos agentes colaborando via Team (supervisor + especialistas)

### Módulo 5: Produção e Projeto Final
- **Aula 09**: Guardrails e Segurança — Validação de outputs, limites, human-in-the-loop
- **Aula 10**: Projeto Final — Assistente de pesquisa com Team (buscador + analista + redator) que pesquisa na web, analisa fontes e gera relatório estruturado

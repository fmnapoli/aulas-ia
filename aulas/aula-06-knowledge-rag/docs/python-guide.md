# Guia de Boas Práticas Python

## Fundamentos

- Use **type hints** em todas as funções para documentar entradas e saídas: `def soma(a: int, b: int) -> int:`
- Prefira **f-strings** para formatação de texto: `f"Olá, {nome}"` em vez de concatenação com `+`
- Siga a convenção **PEP 8** para nomes: `snake_case` para funções e variáveis, `PascalCase` para classes
- Use **list comprehensions** para transformar listas: `[x * 2 for x in lista]` é mais legível que loops equivalentes
- Prefira **pathlib.Path** sobre `os.path` para manipulação de caminhos de arquivo

## Organização de Código

- Separe código em **módulos e pacotes** — cada arquivo deve ter uma responsabilidade clara
- Use **virtual environments** (venv ou uv) para isolar dependências de cada projeto
- Mantenha um **pyproject.toml** para declarar dependências e metadados do projeto
- Escreva **docstrings** em todas as funções públicas explicando o que fazem, parâmetros e retorno

## Tratamento de Erros e Testes

- Trate erros com **exceções específicas**: `except ValueError` em vez de `except Exception` genérico
- Escreva **testes unitários** com pytest — cada função deve ter pelo menos um teste
- Use **logging** em vez de `print()` para mensagens de diagnóstico em produção
- Aplique o princípio **EAFP** (Easier to Ask Forgiveness than Permission): tente executar e trate exceções em vez de verificar condições antes

## Performance e Boas Práticas

- Use **generators** (`yield`) para processar grandes volumes de dados sem carregar tudo na memória
- Prefira **dataclasses** ou **Pydantic** para representar dados estruturados em vez de dicts aninhados
- Evite **variáveis globais** — passe dependências explicitamente como parâmetros

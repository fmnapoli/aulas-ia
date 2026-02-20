"""Guardrails customizados para validação de entrada do agente.

Demonstra como criar guardrails estendendo BaseGuardrail:
- TopicGuardrail: bloqueia inputs que mencionam tópicos proibidos
- MaxLengthGuardrail: bloqueia inputs que excedem um tamanho máximo

Os guardrails são executados ANTES do agente processar o input (pre_hooks).
Se a validação falhar, uma InputCheckError é lançada e o agente não executa.
"""

from agno.exceptions import CheckTrigger, InputCheckError
from agno.guardrails import BaseGuardrail
from agno.run.agent import RunInput


class TopicGuardrail(BaseGuardrail):
    """Bloqueia inputs que mencionam tópicos proibidos.

    Verifica se o texto do input contém palavras-chave de tópicos
    banidos (ex: violência, armas, drogas). A verificação é case-insensitive.
    """

    def __init__(self, banned_topics: list[str] | None = None):
        self.banned_topics = banned_topics or ["violence", "weapons", "drugs"]

    def check(self, run_input: RunInput) -> None:
        """Verifica se o input contém tópicos proibidos."""
        if isinstance(run_input.input_content, str):
            content_lower = run_input.input_content.lower()
            for topic in self.banned_topics:
                if topic.lower() in content_lower:
                    raise InputCheckError(
                        f"Input blocked: topic '{topic}' is not allowed.",
                        check_trigger=CheckTrigger.INPUT_NOT_ALLOWED,
                    )

    async def async_check(self, run_input: RunInput) -> None:
        """Versão assíncrona da verificação (delega para check síncrono)."""
        self.check(run_input)


class MaxLengthGuardrail(BaseGuardrail):
    """Bloqueia inputs que excedem um tamanho máximo de caracteres.

    Útil para prevenir abusos com inputs excessivamente longos
    que podem consumir muitos tokens e recursos.
    """

    def __init__(self, max_length: int = 500):
        self.max_length = max_length

    def check(self, run_input: RunInput) -> None:
        """Verifica se o input excede o tamanho máximo permitido."""
        if isinstance(run_input.input_content, str):
            if len(run_input.input_content) > self.max_length:
                raise InputCheckError(
                    f"Input too long: {len(run_input.input_content)} chars (max: {self.max_length}).",
                    check_trigger=CheckTrigger.INPUT_NOT_ALLOWED,
                )

    async def async_check(self, run_input: RunInput) -> None:
        """Versão assíncrona da verificação (delega para check síncrono)."""
        self.check(run_input)

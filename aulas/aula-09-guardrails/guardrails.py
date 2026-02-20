import re

from agno.exceptions import CheckTrigger, InputCheckError
from agno.guardrails import BaseGuardrail
from agno.run.agent import RunInput


class TopicGuardrail(BaseGuardrail):
    """Block inputs that mention banned topics."""

    def __init__(self, banned_topics: list[str] | None = None):
        self.banned_topics = banned_topics or ["violence", "weapons", "drugs"]

    def check(self, run_input: RunInput) -> None:
        if isinstance(run_input.input_content, str):
            content_lower = run_input.input_content.lower()
            for topic in self.banned_topics:
                if topic.lower() in content_lower:
                    raise InputCheckError(
                        f"Input blocked: topic '{topic}' is not allowed.",
                        check_trigger=CheckTrigger.INPUT_NOT_ALLOWED,
                    )

    async def async_check(self, run_input: RunInput) -> None:
        self.check(run_input)


class MaxLengthGuardrail(BaseGuardrail):
    """Block inputs that exceed a maximum character length."""

    def __init__(self, max_length: int = 500):
        self.max_length = max_length

    def check(self, run_input: RunInput) -> None:
        if isinstance(run_input.input_content, str):
            if len(run_input.input_content) > self.max_length:
                raise InputCheckError(
                    f"Input too long: {len(run_input.input_content)} chars (max: {self.max_length}).",
                    check_trigger=CheckTrigger.INPUT_NOT_ALLOWED,
                )

    async def async_check(self, run_input: RunInput) -> None:
        self.check(run_input)

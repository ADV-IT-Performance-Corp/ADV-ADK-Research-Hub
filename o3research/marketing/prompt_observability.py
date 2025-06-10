import os

from ..core.telemetry import log_prompt


def record_prompt(prompt_id: str, agent_name: str, prompt_text: str) -> None:
    """Log *prompt_text* if observability is enabled."""
    if os.environ.get("PROMPT_OBSERVABILITY") == "1":
        tokens = len(prompt_text.split())
        log_prompt(prompt_id, agent_name, tokens)

class PromptManager:
    """Manage message history for prompts with optional summarization."""

    def __init__(self, history_limit: int = 10) -> None:
        self.history_limit = history_limit

    def summarize_history(self, history: list[str]) -> list[str]:
        """Return summarized history if it exceeds the limit.

        The implementation collapses the oldest messages into a single summary
        placeholder when the number of messages exceeds ``history_limit``.
        """
        if len(history) <= self.history_limit:
            return history

        summary_count = len(history) - (self.history_limit - 1)
        summary = f"[{summary_count} messages summarized]"
        # fmt: off
        return [summary] + history[-(self.history_limit - 1):]
        # fmt: on

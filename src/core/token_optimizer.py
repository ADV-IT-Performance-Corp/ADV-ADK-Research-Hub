class TokenOptimizer:
    """Utility to trim text if it exceeds a limit."""

    def __init__(self, limit: int = 2000) -> None:
        self.limit = limit

    def trim(self, text: str) -> str:
        if len(text) > self.limit:
            return text[: self.limit]
        return text

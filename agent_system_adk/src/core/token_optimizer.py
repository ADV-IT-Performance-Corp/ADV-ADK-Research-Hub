class TokenOptimizer:
    """Utility for trimming or compressing prompt tokens."""

    def optimize(self, text: str) -> str:
        return text.strip()

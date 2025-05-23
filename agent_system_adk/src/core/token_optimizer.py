class TokenOptimizer:
    """Utility to trim prompts and keep token counts low."""
    def optimize(self, text: str) -> str:
        return " ".join(text.split())

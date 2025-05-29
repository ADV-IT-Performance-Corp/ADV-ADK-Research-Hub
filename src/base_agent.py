class BaseAgent:
    """Minimal base class for agents used in examples."""

    def __init__(self, name: str) -> None:
        self.name = name

    def run(self, message: str) -> str:
        """Default implementation simply echoes the message."""
        return f"{self.name}: {message}"

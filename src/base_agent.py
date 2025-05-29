class BaseAgent:
    """Minimal base class for demonstration."""

    def __init__(self, name: str) -> None:
        self.name = name

    def run(self, message: str) -> str:
        """Process a message and return a response."""
        raise NotImplementedError("Agents must implement run()")

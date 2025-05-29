class BaseAgent:
    """Base class for simple agents."""

    def __init__(self, name: str = "BaseAgent") -> None:
        self.name = name

    def run(self, message: str) -> str:
        """Process a message and return a response."""
        raise NotImplementedError("Subclasses must implement run()")

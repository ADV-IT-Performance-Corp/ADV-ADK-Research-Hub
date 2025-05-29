class BaseAgent:
    """Base class for simple agents used in examples."""

    def __init__(self, name: str) -> None:
        self.name = name

    def run(self, message: str) -> str:
        """Return a response. Subclasses should override this."""
        raise NotImplementedError

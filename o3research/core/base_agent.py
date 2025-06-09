from typing import Any


class BaseAgent:
    """Base class for simple agents used in examples.

    Subclasses must implement :py:meth:`run`.
    """

    def __init__(self, name: str) -> None:
        self.name = name

    def run(self, message: Any) -> str:
        """Return a textual response.

        Subclasses should override this.
        """
        raise NotImplementedError

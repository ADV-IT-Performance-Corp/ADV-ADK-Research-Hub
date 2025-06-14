from typing import Any


class Agent:
    """Minimal stub Agent base class."""

    model_config: Any = {}

    def __init__(self, name: str | None = None) -> None:
        self.name = name or self.__class__.__name__

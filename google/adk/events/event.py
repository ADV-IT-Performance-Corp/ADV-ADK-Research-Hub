from dataclasses import dataclass
from typing import Any


@dataclass
class Event:
    invocation_id: str
    author: str
    content: Any

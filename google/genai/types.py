from dataclasses import dataclass
from typing import List, Optional


@dataclass
class Part:
    text: Optional[str] = None

    @classmethod
    def from_text(cls, text: str) -> "Part":
        return cls(text=text)


@dataclass
class Content:
    parts: List[Part]
    role: str

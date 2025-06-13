from dataclasses import dataclass
from pydantic import BaseModel


@dataclass
class A2AMessage:
    """Dataclass representing a simple agent-to-agent message."""

    sender: str
    recipient: str
    content: str


class A2AMessageModel(BaseModel):
    """Pydantic model for agent-to-agent message validation."""

    sender: str
    recipient: str
    content: str

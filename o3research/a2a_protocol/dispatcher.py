"""Simple message dispatcher for agent-to-agent communication."""

from collections.abc import Callable
from typing import Any, Dict

from .a2a_message import A2AMessage, A2AMessageModel

_HANDLERS: Dict[str, Callable[[A2AMessage], Any]] = {}


def register_agent(name: str, handler: Callable[[A2AMessage], Any]) -> None:
    """Register a handler for a recipient agent."""
    if name in _HANDLERS:
        raise KeyError(f"Handler already registered for {name}")
    _HANDLERS[name] = handler


def dispatch_message(message: A2AMessage | A2AMessageModel) -> Any:
    """Forward message to the registered recipient handler."""
    if isinstance(message, A2AMessageModel):
        msg = A2AMessage(**message.model_dump())
    else:
        msg = message

    handler = _HANDLERS.get(msg.recipient)
    if not handler:
        return f"No handler for {msg.recipient}"
    return handler(msg)


def remove_agent(name: str) -> None:
    """Remove a previously registered agent handler."""
    _HANDLERS.pop(name, None)


def clear_agents() -> None:
    """Remove all registered handlers (primarily for tests)."""
    _HANDLERS.clear()

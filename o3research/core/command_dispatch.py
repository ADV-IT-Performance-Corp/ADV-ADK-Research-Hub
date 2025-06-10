"""Minimal command dispatch registry."""

from typing import Any, Callable, Dict

_HANDLERS: Dict[str, Callable[..., Any]] = {}


def register_handler(command: str, handler: Callable[..., Any]) -> None:
    """Register a callable handler for a command."""
    if command in _HANDLERS:
        raise KeyError(f"Handler already registered for {command}")
    _HANDLERS[command] = handler


def dispatch(command: str, *args: Any, **kwargs: Any) -> Any:
    """Dispatch a command to its registered handler."""
    handler = _HANDLERS.get(command)
    if not handler:
        return f"Unknown command: {command}"
    return handler(*args, **kwargs)


def remove_handler(command: str) -> None:
    """Remove a registered handler if present."""
    _HANDLERS.pop(command, None)


def clear_handlers() -> None:
    """Remove all registered handlers (primarily for tests)."""
    _HANDLERS.clear()

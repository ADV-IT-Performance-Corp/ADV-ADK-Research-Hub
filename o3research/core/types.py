from dataclasses import dataclass
from typing import Any, Callable, Awaitable

Callback = Callable[[str], None]
AsyncCallback = Callable[[str], Awaitable[None]]


@dataclass
class TaskResult:
    """Return value from :class:`Executor` tasks."""

    task: Callable[..., Any]
    success: bool
    result: Any | None = None
    error: str | None = None

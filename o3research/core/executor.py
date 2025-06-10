import asyncio
from typing import Any, Awaitable, Callable, Iterable

from .logger import get_logger
from .types import TaskResult


class Executor:
    """Simple async task executor that logs errors."""

    def __init__(self) -> None:
        self.logger = get_logger(self.__class__.__name__)

    async def _run_task(self, task: Callable[[], Awaitable[Any] | Any]) -> TaskResult:
        try:
            if asyncio.iscoroutinefunction(task):
                result = await task()
            else:
                result = task()
            return TaskResult(task=task, success=True, result=result)
        except Exception as exc:
            self.logger.error(
                "Task %s failed: %s", getattr(task, "__name__", str(task)), exc
            )
            return TaskResult(task=task, success=False, error=str(exc))

    async def run_tasks(
        self, tasks: Iterable[Callable[[], Awaitable[Any] | Any]]
    ) -> list[TaskResult]:
        """Execute tasks sequentially and return their results."""
        results: list[TaskResult] = []
        for task in tasks:
            results.append(await self._run_task(task))
        return results

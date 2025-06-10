import asyncio
from pathlib import Path
from typing import Callable, List, Any


class TaskFlow:
    """Minimal sequential task runner."""

    def __init__(self, queue_size: int, work_dir: str) -> None:
        self.queue_size = queue_size
        self.work_dir = Path(work_dir)
        self._queue: asyncio.Queue[Callable[[], Any]] = asyncio.Queue(
            maxsize=queue_size
        )
        self._running = False

    def feed(self, tasks: List[Callable[[], Any]]) -> None:
        if not tasks:
            raise ValueError("tasks list cannot be empty")
        for task in tasks:
            self._queue.put_nowait(task)

    async def _process(self) -> None:
        while not self._queue.empty() and self._running:
            task = await self._queue.get()
            try:
                task()
            finally:
                self._queue.task_done()

    def run(self) -> None:
        self._running = True
        asyncio.run(self._process())
        self._running = False

    def stop(self) -> None:
        self._running = False
        while not self._queue.empty():
            self._queue.get_nowait()
            self._queue.task_done()

    def pending(self) -> int:
        return self._queue.qsize()

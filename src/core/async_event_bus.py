import asyncio
from collections import defaultdict
from typing import Awaitable, Callable

class AsyncEventBus:
    """Simple asyncio-based publish/subscribe bus."""

    def __init__(self) -> None:
        self.subscribers: dict[str, list[Callable[[str], Awaitable[None]]]] = defaultdict(list)

    def subscribe(self, topic: str, callback: Callable[[str], Awaitable[None]]) -> None:
        self.subscribers[topic].append(callback)

    async def publish(self, topic: str, message: str) -> None:
        tasks = [callback(message) for callback in self.subscribers.get(topic, [])]
        if tasks:
            await asyncio.gather(*tasks)

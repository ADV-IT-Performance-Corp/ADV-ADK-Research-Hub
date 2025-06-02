import asyncio
from collections import defaultdict
from typing import Awaitable, Callable

# Callback type alias for async subscribers
AsyncSubscriber = Callable[[str], Awaitable[None]]

class AsyncEventBus:
    """Simple asyncio-based publish/subscribe bus."""

    def __init__(self) -> None:
        self.subscribers: dict[str, list[AsyncSubscriber]] = defaultdict(list)

    def subscribe(self, topic: str, callback: AsyncSubscriber) -> None:
        self.subscribers[topic].append(callback)

    async def publish(self, topic: str, message: str) -> None:
        tasks = [callback(message) for callback in self.subscribers.get(topic, [])]
        if tasks:
            await asyncio.gather(*tasks)

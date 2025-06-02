import asyncio
from collections import defaultdict
from typing import Awaitable, Callable, Dict, List

AsyncEventCallback = Callable[[str], Awaitable[None]]

class AsyncEventBus:
    """Simple asyncio-based publish/subscribe bus."""

    def __init__(self) -> None:
        self.subscribers: Dict[str, List[AsyncEventCallback]] = defaultdict(list)

    def subscribe(self, topic: str, callback: AsyncEventCallback) -> None:
        self.subscribers[topic].append(callback)

    async def publish(self, topic: str, message: str) -> None:
        tasks = [callback(message) for callback in self.subscribers.get(topic, [])]
        if tasks:
            await asyncio.gather(*tasks)

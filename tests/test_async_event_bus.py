import asyncio
from src.core.event_bus import AsyncEventBus

async def main():
    bus = AsyncEventBus()
    messages = []

    async def handler(msg: str) -> None:
        messages.append(msg)

    bus.subscribe("demo", handler)
    await bus.publish("demo", "hello")
    assert messages == ["hello"]

if __name__ == "__main__":
    asyncio.run(main())

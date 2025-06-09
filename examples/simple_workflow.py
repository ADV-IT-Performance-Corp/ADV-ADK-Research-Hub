"""Run a basic workflow using AsyncEventBus and sample agents."""

import asyncio
from o3research.mcp_server import MCPServer
from o3research.core import AsyncEventBus, get_logger


event_bus = AsyncEventBus()
logger = get_logger("Workflow")
server = MCPServer()


async def handle_research(msg: str) -> None:
    logger.info(server.route("research", msg))
    await asyncio.sleep(0.1)
    logger.info(server.route("content", msg))


async def handle_optimize(msg: str) -> None:
    logger.info(server.route("optimize", msg))
    logger.info(server.route("analytics", msg))


event_bus.subscribe("start_research", handle_research)
event_bus.subscribe("start_optimize", handle_optimize)


async def main() -> None:
    await asyncio.gather(
        event_bus.publish("start_research", "email marketing trends"),
        event_bus.publish("start_optimize", "budget allocation"),
    )


if __name__ == "__main__":
    asyncio.run(main())

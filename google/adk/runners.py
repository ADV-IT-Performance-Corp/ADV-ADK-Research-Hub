from __future__ import annotations

import asyncio
from types import SimpleNamespace
from typing import Any, List

from .events.event import Event


class InMemoryRunner:
    """Very small stub runner executing an agent locally."""

    def __init__(
        self,
        agent: Any | None = None,
        flow: str | None = None,
        app_name: str = "stub_app",
    ) -> None:
        self.agent = agent
        self.flow = flow
        self.app_name = app_name

        class SessionService:
            def create_session_sync(self, *args: Any, **kwargs: Any) -> None:
                pass

        self.session_service = SessionService()

    def run(
        self,
        user_id: str | None = None,
        session_id: str | None = None,
        new_message: Any | None = None,
    ) -> List[Event]:
        if not self.agent or not hasattr(self.agent, "_run_async_impl"):
            return []
        ctx = SimpleNamespace(invocation_id="0", user_content=new_message)

        async def gather() -> List[Event]:
            events: List[Event] = []
            async for ev in self.agent._run_async_impl(ctx):  # type: ignore[attr-defined,union-attr]
                events.append(ev)
            return events

        return asyncio.run(gather())


class VertexAIRunner:
    """Placeholder for Vertex AI runner."""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        self.args = args
        self.kwargs = kwargs

    def run(self, *args: Any, **kwargs: Any) -> None:
        pass

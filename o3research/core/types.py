from typing import Callable, Awaitable

Callback = Callable[[str], None]
AsyncCallback = Callable[[str], Awaitable[None]]

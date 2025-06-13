import unittest
import sys
from types import ModuleType

# Stub heavy google packages so importing o3research works without deps
modules = {
    "google": ModuleType("google"),
    "google.ads": ModuleType("google.ads"),
    "google.ads.googleads": ModuleType("google.ads.googleads"),
    "google.ads.googleads.client": ModuleType("google.ads.googleads.client"),
    "google.ads.googleads.errors": ModuleType("google.ads.googleads.errors"),
}
for name, mod in modules.items():
    sys.modules.setdefault(name, mod)
client_mod = modules["google.ads.googleads.client"]
client_mod.GoogleAdsClient = object  # type: ignore[attr-defined]
error_mod = modules["google.ads.googleads.errors"]
error_mod.GoogleAdsException = Exception  # type: ignore[attr-defined]

from o3research.a2a_protocol.a2a_message import (  # noqa: E402
    A2AMessage,
    A2AMessageModel,
)  # noqa: E402
from o3research.a2a_protocol.dispatcher import (  # noqa: E402
    register_agent,
    dispatch_message,
    clear_agents,
)


class TestA2AMessage(unittest.TestCase):
    def test_dataclass_creation(self) -> None:
        msg = A2AMessage(sender="a", recipient="b", content="hi")
        self.assertEqual(msg.sender, "a")
        self.assertEqual(msg.recipient, "b")
        self.assertEqual(msg.content, "hi")

    def test_model_validation(self) -> None:
        model = A2AMessageModel(sender="x", recipient="y", content="hey")
        self.assertEqual(model.sender, "x")
        self.assertEqual(model.recipient, "y")
        self.assertEqual(model.content, "hey")


class TestDispatcher(unittest.TestCase):
    def setUp(self) -> None:
        clear_agents()

    def test_dispatch_registered_agent(self) -> None:
        def handler(msg: A2AMessage) -> str:
            return f"echo:{msg.content}"

        register_agent("bob", handler)
        msg = A2AMessage(sender="alice", recipient="bob", content="hi")
        result = dispatch_message(msg)
        self.assertEqual(result, "echo:hi")

    def test_dispatch_model(self) -> None:
        def handler(msg: A2AMessage) -> str:
            return msg.content.upper()

        register_agent("carol", handler)
        model = A2AMessageModel(sender="dave", recipient="carol", content="ok")
        result = dispatch_message(model)
        self.assertEqual(result, "OK")

    def test_unknown_recipient(self) -> None:
        msg = A2AMessage(sender="a", recipient="missing", content="test")
        result = dispatch_message(msg)
        self.assertEqual(result, "No handler for missing")


if __name__ == "__main__":  # pragma: no cover
    unittest.main()

import unittest
from o3research.core.command_dispatch import (
    register_handler,
    dispatch,
    remove_handler,
    clear_handlers,
)


class TestCommandDispatch(unittest.TestCase):
    def setUp(self) -> None:
        clear_handlers()

    def test_known_command_invokes_handler(self) -> None:
        calls = []

        def handler(arg: str) -> str:
            calls.append(arg)
            return "handled"

        register_handler("ping", handler)
        result = dispatch("ping", "data")
        self.assertEqual(result, "handled")
        self.assertEqual(calls, ["data"])

    def test_unknown_command(self) -> None:
        result = dispatch("missing")
        self.assertEqual(result, "Unknown command: missing")

    def test_remove_handler(self) -> None:
        register_handler("ping", lambda: "ok")
        remove_handler("ping")
        result = dispatch("ping")
        self.assertEqual(result, "Unknown command: ping")


if __name__ == "__main__":
    unittest.main()

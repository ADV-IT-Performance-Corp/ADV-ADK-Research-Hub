import unittest

from o3research.agents.agent_registry import register_agent, get_agent, clear_registry


class DummyAgent:
    pass


class TestAgentRegistry(unittest.TestCase):
    def setUp(self) -> None:
        clear_registry()

    def test_register_and_fetch(self) -> None:
        register_agent("dummy", DummyAgent)
        self.assertIs(get_agent("dummy"), DummyAgent)

    def test_duplicate_registration_error(self) -> None:
        register_agent("dummy", DummyAgent)
        with self.assertRaises(KeyError):
            register_agent("dummy", DummyAgent)

    def test_fetch_unknown_error(self) -> None:
        with self.assertRaises(KeyError):
            get_agent("missing")


if __name__ == "__main__":  # pragma: no cover
    unittest.main()

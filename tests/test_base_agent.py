import unittest
from google.adk import Agent


class DummyAgent(Agent):
    """Trivial subclass without overriding run."""

    pass


class TestBaseAgent(unittest.TestCase):
    def test_run_not_implemented(self):
        agent = DummyAgent(name="dummy")
        with self.assertRaises(AttributeError):
            agent.run("msg")


if __name__ == "__main__":  # pragma: no cover
    unittest.main()

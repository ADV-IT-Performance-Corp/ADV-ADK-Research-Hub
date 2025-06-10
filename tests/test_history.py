import unittest
from tempfile import TemporaryDirectory
from pathlib import Path

from o3research.core.history import History


class TestHistory(unittest.TestCase):
    def test_load_missing_returns_empty(self) -> None:
        with TemporaryDirectory() as tmpdir:
            path = Path(tmpdir) / "hist.json"
            history = History.load(path)
            self.assertEqual(history.entries, [])

    def test_save_and_reload(self) -> None:
        with TemporaryDirectory() as tmpdir:
            path = Path(tmpdir) / "hist.json"
            history = History.load(path)
            history.add("hello")
            history.add("world")
            history.save()

            loaded = History.load(path)
            self.assertEqual(loaded.entries, ["hello", "world"])


if __name__ == "__main__":
    unittest.main()

import unittest
from pathlib import Path
from unittest.mock import patch

from o3research.core.prompt_gen import get_prompt, DEFAULT_PROMPT


class TestPromptGen(unittest.TestCase):
    def test_default_prompt_when_missing(self):
        with patch.object(Path, "exists", return_value=False):
            result = get_prompt(Path("missing.txt"))
        self.assertEqual(result, DEFAULT_PROMPT)

    def test_custom_prompt_from_file(self):
        with (
            patch.object(Path, "exists", return_value=True),
            patch.object(Path, "read_text", return_value="custom") as read_mock,
        ):
            result = get_prompt(Path("file.txt"))
            read_mock.assert_called_once_with(encoding="utf-8")
        self.assertEqual(result, "custom")


if __name__ == "__main__":  # pragma: no cover
    unittest.main()

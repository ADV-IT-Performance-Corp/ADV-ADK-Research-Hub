import runpy
from pathlib import Path
from unittest.mock import patch


def test_test_version_executes_main():
    called = {"value": False}

    def dummy():
        called["value"] = True

    test_file = Path(__file__).with_name("test_version.py")
    with patch("unittest.main", dummy):
        runpy.run_path(str(test_file), run_name="__main__")

    assert called["value"], "unittest.main should have been called"

import runpy
from pathlib import Path
from types import ModuleType
from unittest.mock import patch
import sys


def test_test_version_executes_main():
    called = {"value": False}

    # Provide stub google modules so imports work without dependencies
    stubs = {
        "google": ModuleType("google"),
        "google.ads": ModuleType("google.ads"),
        "google.ads.googleads": ModuleType("google.ads.googleads"),
        "google.ads.googleads.client": ModuleType("google.ads.googleads.client"),
        "google.ads.googleads.errors": ModuleType("google.ads.googleads.errors"),
    }
    stubs["google.ads.googleads.client"].GoogleAdsClient = object
    stubs["google.ads.googleads.errors"].GoogleAdsException = Exception
    for name, mod in stubs.items():
        sys.modules.setdefault(name, mod)

    def dummy():
        called["value"] = True

    test_file = Path(__file__).with_name("test_version.py")
    with patch("unittest.main", dummy):
        runpy.run_path(str(test_file), run_name="__main__")

    assert called["value"], "unittest.main should have been called"


def test_test_evaluation_executes_main():
    called = {"value": False}

    def dummy():
        called["value"] = True

    test_file = Path(__file__).with_name("test_evaluation.py")
    with patch("unittest.main", dummy):
        runpy.run_path(str(test_file), run_name="__main__")

    assert called["value"], "unittest.main should have been called"


def test_test_meta_json_executes_main():
    called = {"value": False}

    def dummy():
        called["value"] = True

    test_file = Path(__file__).with_name("test_meta_json.py")
    with patch("unittest.main", dummy):
        runpy.run_path(str(test_file), run_name="__main__")

    assert called["value"], "unittest.main should have been called"


def test_test_reporting_executes_main():
    called = {"value": False}

    def dummy():
        called["value"] = True

    test_file = Path(__file__).with_name("test_reporting.py")
    with patch("unittest.main", dummy):
        runpy.run_path(str(test_file), run_name="__main__")

    assert called["value"], "unittest.main should have been called"


def test_test_mcp_server_executes_main():
    called = {"value": False}

    def dummy():
        called["value"] = True

    test_file = Path(__file__).with_name("test_mcp_server.py")
    with patch("unittest.main", dummy):
        runpy.run_path(str(test_file), run_name="__main__")

    assert called["value"], "unittest.main should have been called"

import importlib
import runpy
import types
from pathlib import Path
from unittest.mock import patch


def test_async_queue_overflow_with_dummy_yaml():
    dummy_yaml = types.ModuleType("yaml")
    dummy_yaml.safe_load = lambda _: {"max_queue_size": 1}
    with patch.dict("sys.modules", {"yaml": dummy_yaml}):
        import tests.test_core as tc

        importlib.reload(tc)
        with patch.object(tc, "YAML_AVAILABLE", True):
            case = tc.TestQueueLimits("test_async_queue_overflow")
            case.test_async_queue_overflow()
    importlib.reload(tc)


def test_core_main_via_runpy():
    called = {"value": False}

    def dummy():
        called["value"] = True

    test_file = Path(__file__).with_name("test_core.py")
    with patch("unittest.main", dummy):
        runpy.run_path(str(test_file), run_name="__main__")
    assert called["value"], "unittest.main should have been called"

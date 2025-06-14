import importlib
import sys
from types import ModuleType

from typing import TYPE_CHECKING

if TYPE_CHECKING:  # pragma: no cover - type checking only
    import pytest
else:  # pragma: no cover - runtime import for fixture
    import pytest  # type: ignore


@pytest.fixture(autouse=True)
def _google_stubs():
    """Ensure Google packages are available for tests."""
    packages = {
        "google.adk": ModuleType("google.adk"),
        "google.genai": ModuleType("google.genai"),
    }
    for name, mod in packages.items():
        try:
            importlib.import_module(name)
        except ModuleNotFoundError:
            sys.modules.setdefault(name, mod)

    # Ensure the real o3research package is loaded if a stub was left behind
    o3 = sys.modules.get("o3research")
    if isinstance(o3, ModuleType) and not getattr(o3, "__file__", None):
        sys.modules.pop("o3research")
        importlib.import_module("o3research")

    modules = {
        "google": ModuleType("google"),
        "google.ads": ModuleType("google.ads"),
        "google.ads.googleads": ModuleType("google.ads.googleads"),
        "google.ads.googleads.client": ModuleType("google.ads.googleads.client"),
        "google.ads.googleads.errors": ModuleType("google.ads.googleads.errors"),
    }
    modules["google.ads.googleads.client"].GoogleAdsClient = object
    modules["google.ads.googleads.errors"].GoogleAdsException = Exception
    for name, mod in modules.items():
        sys.modules.setdefault(name, mod)
    yield

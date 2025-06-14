"""Test package initialization for ADV-ADK-Research-Hub."""

# This file ensures the tests package is discoverable when using pytest
# and also inserts lightweight stubs for optional Google packages so tests
# don't require the real dependencies.

from __future__ import annotations

import importlib
import sys
from types import ModuleType

for pkg in ("google.adk", "google.genai"):
    try:
        importlib.import_module(pkg)
    except ModuleNotFoundError:  # pragma: no cover - optional path
        sys.modules.setdefault(pkg, ModuleType(pkg))

# Provide simple stubs for the Google Ads client so imports succeed
modules = {
    "google": ModuleType("google"),
    "google.ads": ModuleType("google.ads"),
    "google.ads.googleads": ModuleType("google.ads.googleads"),
    "google.ads.googleads.client": ModuleType("google.ads.googleads.client"),
    "google.ads.googleads.errors": ModuleType("google.ads.googleads.errors"),
}
for name, mod in modules.items():
    sys.modules.setdefault(name, mod)
modules["google.ads.googleads.client"].GoogleAdsClient = object  # type: ignore[attr-defined]
modules["google.ads.googleads.errors"].GoogleAdsException = Exception  # type: ignore[attr-defined]

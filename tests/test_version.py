import unittest
import sys
from types import ModuleType
from unittest.mock import MagicMock
from o3research import __version__


class TestVersion(unittest.TestCase):
    def test_version_matches_file(self):
        with open("VERSION") as vf:
            file_version = vf.read().strip()
        self.assertEqual(__version__, file_version)

    def test_agent_versions_match_file(self):
        import importlib
        import pkgutil

        # Provide stub google modules so imports work without dependencies
        modules = {
            "google": ModuleType("google"),
            "google.adk": ModuleType("google.adk"),
            "google.oauth2": ModuleType("google.oauth2"),
            "google.oauth2.credentials": ModuleType("google.oauth2.credentials"),
            "google.oauth2.service_account": ModuleType("google.oauth2.service_account"),
            "google_auth_oauthlib": ModuleType("google_auth_oauthlib"),
            "google_auth_oauthlib.flow": ModuleType("google_auth_oauthlib.flow"),
            "google.auth": ModuleType("google.auth"),
            "google.auth.transport": ModuleType("google.auth.transport"),
            "google.auth.transport.requests": ModuleType("google.auth.transport.requests"),
            "googleapiclient": ModuleType("googleapiclient"),
            "googleapiclient.discovery": ModuleType("googleapiclient.discovery"),
        }
        modules["google.adk"].Agent = object
        modules["google.oauth2.credentials"].Credentials = MagicMock()
        modules["google.oauth2.service_account"].Credentials = MagicMock()
        modules["google_auth_oauthlib.flow"].InstalledAppFlow = MagicMock()
        modules["google.auth.transport.requests"].Request = MagicMock()
        modules["googleapiclient.discovery"].build = MagicMock()
        for name, mod in modules.items():
            sys.modules.setdefault(name, mod)

        with open("VERSION") as vf:
            file_version = vf.read().strip()

        packages = [
            "o3research.agents",
            "o3research.agents.marketing_assistant",
            "marketing_assistant",
        ]
        for pkg_name in packages:
            pkg = importlib.import_module(pkg_name)
            if hasattr(pkg, "__version__"):
                self.assertEqual(pkg.__version__, file_version)
            if hasattr(pkg, "__path__"):
                for _, name, _ in pkgutil.iter_modules(pkg.__path__):
                    mod = importlib.import_module(f"{pkg_name}.{name}")
                    if hasattr(mod, "__version__"):
                        self.assertEqual(mod.__version__, file_version)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()

import sys
from types import ModuleType
import unittest
from unittest.mock import MagicMock, patch

# Provide stub google modules so imports work without dependencies
modules = {
    "google": ModuleType("google"),
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
for name, mod in modules.items():
    sys.modules.setdefault(name, mod)

sys.modules["google.oauth2.credentials"].Credentials = MagicMock()
sys.modules["google.oauth2.service_account"].Credentials = MagicMock()
sys.modules["google_auth_oauthlib.flow"].InstalledAppFlow = MagicMock()
sys.modules["google.auth.transport.requests"].Request = MagicMock()
sys.modules["googleapiclient.discovery"].build = MagicMock()

import marketing_assistant.google_ads_client  # noqa: E402
import marketing_assistant.ga_client  # noqa: E402
from marketing_assistant.google_ads_client import GoogleAdsClient
from marketing_assistant.ga_client import GAClient


class TestGoogleAdsClient(unittest.TestCase):
    @patch("marketing_assistant.google_ads_client.build")
    def test_list_campaigns_build_request(self, mock_build):
        service = MagicMock()
        customers = service.customers.return_value
        google_ads = customers.googleAds.return_value
        search = google_ads.search.return_value
        search.execute.return_value = {"results": [{"id": "1"}]}
        mock_build.return_value = service

        with patch.object(
            GoogleAdsClient, "_load_credentials", lambda self: None
        ), patch.object(GoogleAdsClient, "refresh_token") as mock_refresh:
            client = GoogleAdsClient("cred.json", "token.json")
            result = client.list_campaigns("123", page_size=10)
            mock_refresh.assert_called_once()

        expected_query = (
            "SELECT campaign.id, campaign.name FROM campaign ORDER BY "
            "campaign.id LIMIT 10"
        )
        google_ads.search.assert_called_once_with(
            customerId="123", body={"query": expected_query}
        )
        search.execute.assert_called_once()
        self.assertEqual(result, [{"id": "1"}])

    @patch(
        "marketing_assistant.google_ads_client.service_account.Credentials.from_service_account_file"
    )
    def test_load_service_account_credentials(self, mock_from_file):
        cred = MagicMock()
        mock_from_file.return_value = cred
        client = GoogleAdsClient(
            "cred.json", "token.json", service_account_file="sa.json"
        )
        self.assertIs(client.creds, cred)
        mock_from_file.assert_called_once_with(
            "sa.json", scopes=marketing_assistant.google_ads_client.SCOPES
        )

    @patch("marketing_assistant.google_ads_client.Path.write_text")
    def test_refresh_token_saves_credentials(self, mock_write):
        with patch.object(GoogleAdsClient, "_load_credentials", lambda self: None):
            client = GoogleAdsClient("cred.json", "token.json")
        creds = MagicMock(expired=True, refresh_token="tok")
        creds.to_json.return_value = "data"
        client.creds = creds
        client.refresh_token()
        creds.refresh.assert_called_once()
        mock_write.assert_called_once_with("data")

    @patch("marketing_assistant.google_ads_client.Path.write_text")
    def test_service_account_refresh_no_save(self, mock_write):
        with patch.object(GoogleAdsClient, "_load_credentials", lambda self: None):
            client = GoogleAdsClient(
                "cred.json", "token.json", service_account_file="sa.json"
            )
        creds = MagicMock(expired=True)
        creds.refresh_token = None
        client.creds = creds
        client.refresh_token()
        creds.refresh.assert_called_once()
        mock_write.assert_not_called()


class TestGAClient(unittest.TestCase):
    @patch("marketing_assistant.ga_client.build")
    def test_fetch_traffic(self, mock_build):
        service = MagicMock()
        props = service.properties.return_value
        run = props.runReport.return_value
        run.execute.return_value = {"rows": [{"metric": "value"}]}
        mock_build.return_value = service

        with patch.object(
            GAClient, "_load_credentials", lambda self: None
        ), patch.object(GAClient, "refresh_token") as mock_refresh:
            client = GAClient("cred.json", "token.json", "999")
            result = client.fetch_traffic("2023-01-01", "2023-01-02")
            mock_refresh.assert_called_once()

        expected_body = {
            "dateRanges": [{"startDate": "2023-01-01", "endDate": "2023-01-02"}],
            "metrics": [{"name": "sessions"}],
            "dimensions": [{"name": "date"}],
        }
        props.runReport.assert_called_once_with(
            property="properties/999", body=expected_body
        )
        run.execute.assert_called_once()
        self.assertEqual(result, [{"metric": "value"}])

    @patch(
        "marketing_assistant.ga_client.service_account.Credentials.from_service_account_file"
    )
    def test_load_service_account_credentials(self, mock_from_file):
        cred = MagicMock()
        mock_from_file.return_value = cred
        client = GAClient(
            "cred.json", "token.json", "999", service_account_file="sa.json"
        )
        self.assertIs(client.creds, cred)
        mock_from_file.assert_called_once_with(
            "sa.json", scopes=marketing_assistant.ga_client.SCOPES
        )

    @patch("marketing_assistant.ga_client.build")
    def test_fetch_conversions(self, mock_build):
        service = MagicMock()
        props = service.properties.return_value
        run = props.runReport.return_value
        run.execute.return_value = {"rows": [{"conv": "val"}]}
        mock_build.return_value = service

        with patch.object(
            GAClient, "_load_credentials", lambda self: None
        ), patch.object(GAClient, "refresh_token") as mock_refresh:
            client = GAClient("cred.json", "token.json", "888")
            result = client.fetch_conversions("2023-02-01", "2023-02-02")
            mock_refresh.assert_called_once()

        expected_body = {
            "dateRanges": [{"startDate": "2023-02-01", "endDate": "2023-02-02"}],
            "metrics": [{"name": "conversions"}],
            "dimensions": [{"name": "date"}],
        }
        props.runReport.assert_called_once_with(
            property="properties/888", body=expected_body
        )
        run.execute.assert_called_once()
        self.assertEqual(result, [{"conv": "val"}])

    @patch("marketing_assistant.ga_client.Path.write_text")
    def test_refresh_token_saves_credentials(self, mock_write):
        with patch.object(GAClient, "_load_credentials", lambda self: None):
            client = GAClient("cred.json", "token.json", "123")
        creds = MagicMock(expired=True, refresh_token="tok")
        creds.to_json.return_value = "data"
        client.creds = creds
        client.refresh_token()
        creds.refresh.assert_called_once()
        mock_write.assert_called_once_with("data")

    @patch("marketing_assistant.ga_client.Path.write_text")
    def test_service_account_refresh_no_save(self, mock_write):
        with patch.object(GAClient, "_load_credentials", lambda self: None):
            client = GAClient(
                "cred.json", "token.json", "123", service_account_file="sa.json"
            )
        creds = MagicMock(expired=True)
        creds.refresh_token = None
        client.creds = creds
        client.refresh_token()
        creds.refresh.assert_called_once()
        mock_write.assert_not_called()


if __name__ == "__main__":  # pragma: no cover
    unittest.main()

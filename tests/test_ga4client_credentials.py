import unittest
from unittest.mock import MagicMock, patch, PropertyMock
from o3research.analytics import GA4Client, BigQueryMetricsSink

class TestGA4ClientCredentials(unittest.TestCase):
    @patch('o3research.analytics.Path.write_text')
    @patch('o3research.analytics.Credentials.from_authorized_user_file')
    @patch('o3research.analytics.Path.exists', return_value=True)
    def test_refresh_existing_token(self, mock_exists, mock_from_file, mock_write):
        creds = MagicMock(valid=False, expired=True, refresh_token='tok')
        mock_from_file.return_value = creds
        with patch('o3research.analytics.Request') as mock_request:
            GA4Client('prop', credentials_file='cred.json', token_file='token.json')
            creds.refresh.assert_called_once()
            mock_write.assert_called_once()

    @patch('o3research.analytics.Path.write_text')
    @patch('o3research.analytics.InstalledAppFlow.from_client_secrets_file')
    @patch('o3research.analytics.Credentials.from_authorized_user_file')
    @patch('o3research.analytics.Path.exists', return_value=False)
    def test_run_local_server_new_token(self, mock_exists, mock_from_file, mock_flow, mock_write):
        flow = MagicMock()
        creds = MagicMock(valid=True)
        flow.run_local_server.return_value = creds
        mock_flow.return_value = flow
        GA4Client('prop', credentials_file='cred.json', token_file='token.json')
        from o3research import analytics
        mock_flow.assert_called_once_with('cred.json', analytics.SCOPES)
        mock_write.assert_called_once()

class TestGA4ClientFetchMetrics(unittest.TestCase):
    @patch.object(GA4Client, '_load_credentials', lambda self: None)
    def test_no_rows_returns_empty(self):
        client = GA4Client('prop')
        fake_request = MagicMock()
        fake_request.execute.return_value = {}
        service = MagicMock()
        service.properties.return_value.runReport.return_value = fake_request
        with patch.object(GA4Client, 'service', new_callable=PropertyMock) as mock_service:
            mock_service.return_value = service
            result = client.fetch_metrics('2023-01-01', '2023-01-31')
        self.assertEqual(result, {})

    @patch.object(GA4Client, '_load_credentials', lambda self: None)
    def test_with_rows_parses_values(self):
        client = GA4Client('prop')
        fake_request = MagicMock()
        fake_request.execute.return_value = {
            'rows': [{'metricValues': [{'value': '1'}, {'value': '2'}, {'value': '3'}, {'value': '4'}, {'value': '5'}, {'value': '6'}]}]
        }
        service = MagicMock()
        service.properties.return_value.runReport.return_value = fake_request
        with patch.object(GA4Client, 'service', new_callable=PropertyMock) as mock_service:
            mock_service.return_value = service
            result = client.fetch_metrics('2023-01-01', '2023-01-31')
        self.assertEqual(result['impressions'], 1.0)
        self.assertEqual(result['returning_customers'], 6.0)

    @patch.object(GA4Client, '_load_credentials', lambda self: None)
    @patch('o3research.analytics.build')
    def test_service_lazy_build(self, mock_build):
        client = GA4Client('prop')
        svc = object()
        mock_build.return_value = svc
        self.assertIs(client.service, svc)
        mock_build.assert_called_once()

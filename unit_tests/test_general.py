import unittest
import mock
from transactions_api.main import app


class TestGeneral(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_health(self):
        self.assertEqual((self.app.get('/health')).status_code, 200)

    @mock.patch('transactions_api.calls.TRANSACTIONS_ADAPTER.get_health_service_check')
    def test_health_service_check(self, mock_health):
        mock_health.return_value = 'hello'
        rv = self.app.get('/health/service-check', headers={'Content-Type': 'application/json'})
        self.assertEqual(rv.status_code, 200)
        self.assertEqual(rv.data.decode('utf-8'), 'hello')

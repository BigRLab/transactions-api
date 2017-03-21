import json
import mock
import unittest
import requests

from transactions_api.main import app

class TestTransactions(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    @mock.patch('transactions_api.calls.TRANSACTIONS_ADAPTER.insert_transaction')
    def test_insert_transaction(self, mock_insert):
        self.app.post('insert-transaction', data=json.dumps({"a": "b"}))
        mock_insert.assert_called_with(b'{"a": "b"}')

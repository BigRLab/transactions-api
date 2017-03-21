import json
import mock
import unittest

from transactions_api.main import app


class TestLogging(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    @mock.patch('transactions_api.calls.TRANSACTIONS_ADAPTER.insert_transaction')
    def test_error_logged(self, mock_insert):
        mock_insert.side_effect = self.transaction_find_exception
        with self.assertLogs(level='ERROR') as logging_context:
            self.app.post('insert-transaction', data=json.dumps({"a": "b"}),
                          headers={'Content-Type': 'application/json', 'Accept': 'application/json'})
        self.assertTrue("Transaction Find BOOM!" in str(logging_context.output))

    def transaction_find_exception(self, *args, **kwargs):
        raise Exception("Transaction Find BOOM!")

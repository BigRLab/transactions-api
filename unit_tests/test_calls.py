import json
import mock
import requests
import unittest

from transactions_api import calls
from transactions_api.main import app


class FakeResponse(requests.Response):

    def __init__(self, content='', status_code=200):
        super(FakeResponse, self).__init__()
        self._content = content
        self._content_consumed = True
        self.status_code = status_code


class TestCalls(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    @mock.patch('transactions_api.calls.TRANSACTIONS_ADAPTER.insert_transaction')
    def test_error_logged(self, mock_insert):
        self.app.post('insert-transaction', data=json.dumps({"a": "b"}),
                      headers={'Content-Type': 'application/json', 'Accept': 'application/json'})
        mock_insert.assert_called_with(b'{"a": "b"}')

    @mock.patch('transactions_api.calls.requests.post')
    def test_post_json(self, mock_requests):
        mock_requests.return_value = FakeResponse(str.encode('{"foo" : "bar"}'))
        api = calls._APIBase()
        api.base = "http://127.0.0.1:5000"
        ret_val = api._post_json("http://127.0.0.1:5000/",
                                 data={'test': '1'})
        self.assertEqual({'foo': 'bar'}, json.loads(ret_val))

    # TODO consider unit test for service check.

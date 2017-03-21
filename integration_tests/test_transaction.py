import json
import os
import unittest

from transactions_api.main import app


class TestTransaction(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_insert_transaction(self):
        title_number = os.environ['TEST_TITLE']
        application_referenece = os.environ['TEST_APPLICATION']
        data = {"appn_trans_code": "C", "appn_trans_value": 123,
                "fee_categ_code": "2", "lr_appn_ref": application_referenece, "title_no": title_number,
                "trans_proc_curr": "Y"}
        post_response = self.app.post('/insert-transaction', data=json.dumps(data),
                                      headers={'Content-Type': 'application/json', 'Accept': 'application/json'})
        self.assertEqual(post_response.status_code, 200)

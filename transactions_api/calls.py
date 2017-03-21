import os
import json
from urllib.parse import urljoin
from flask import jsonify
from transactions_api.app import app

import requests


class _APIBase:

    """
    The Base Class a collaborating service call API
    """

    base = ''

    def _post_json(self, url, data=None, headers=None):
        if data is None:
            data = {}

        url = urljoin(self.base, url)
        app.logger.debug('Posting %s:%s...', url, data)
        response = requests.post(url, data=data, headers=headers)
        response.raise_for_status()
        app.logger.debug(response.text)

        return response.text

try:
    TRANSACTION_URI_BASE = os.getenv('TRANSACTION_ADAPTER_URI')
except KeyError:
    TRANSACTION_URI_BASE = ''


class _TransactionsAdapter(_APIBase):

    base = TRANSACTION_URI_BASE

    def insert_transaction(self, data=None):

        return self._post_json('insert-transaction', data)

    @staticmethod
    def get_health_service_check():

        # Attempt to establish a connection with all linked services
        service_list = {
            'services':
                [
                    # empty for now - default, but required
                ]
        }

        try:
            # Attempt to connect to transactions adapter
            service_response = requests.get(TRANSACTION_URI_BASE + '/health/service-check')
            trans_service_dict = json.loads(service_response.text)
            service_response_refined = trans_service_dict['trans-adapter-services']

            # If we get to this point then we can assume that no exceptions have occurred
            # so we can add the service response to the list above
            [service_list['services'].append(response_value) for response_value in service_response_refined]

        except Exception as e:
            # The most common scenario here is that a RequestException occurs; when the attempted connection
            # is not completed successfully for a number of different reasons
            app.logger.error('A exception has occured in the service check route: %s', (e,), exc_info=True)
            service_list['services'].append(_get_service_check_json(500, 'Transactions API', 'Transactions Adapter',
                                            'Error: could not connect'))

        return jsonify(service_list)


def _get_service_check_json(status_code, service_from, service_to, service_message):

    service_dict = {
        'status_code': status_code,
        'service_from': service_from,
        'service_to': service_to,
        'service_message': service_message
    }

    return service_dict


TRANSACTIONS_ADAPTER = _TransactionsAdapter()

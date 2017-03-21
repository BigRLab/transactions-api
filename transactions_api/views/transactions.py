from flask import Blueprint, request
from transactions_api import calls

# This is the blueprint object that gets registered into the app in blueprints.py.
transaction = Blueprint('transaction', __name__)


@transaction.route('/insert-transaction', methods=['POST'])
def transactions():
    return calls.TRANSACTIONS_ADAPTER.insert_transaction(request.data)

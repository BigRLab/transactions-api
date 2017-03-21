# Import every blueprint file
from transactions_api.views import general, transactions


def register_blueprints(app):
    """
    Adds all blueprint objects into the app.
    """
    app.register_blueprint(general.general)
    app.register_blueprint(transactions.transaction)

    # All done!
    app.logger.info("Blueprints registered")

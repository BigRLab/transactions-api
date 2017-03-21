from flask_script import Manager
from transactions_api.main import app
import os

# Init manager
manager = Manager(app)


@manager.command
def runserver(port=5014):
    """Run the app using flask server"""

    os.environ["PYTHONUNBUFFERED"] = "yes"
    os.environ["LOG_LEVEL"] = "DEBUG"
    os.environ["COMMIT"] = "LOCAL"

    app.run(debug=True, port=int(port))


if __name__ == "__main__":
    manager.run()

# Tests the endpoints and controller for the User

from tests import TestAssertion
from flask import Flask
from routes.user_routes import user_blueprint
from routes.auth_routes import auth_blueprint


test_app = Flask("__main__")
test_app.register_blueprint(user_blueprint)
test_app.register_blueprint(auth_blueprint)
test_app.run(host="localhost", port="8080")






# Tests the endpoints and controller for the User

from flask import Flask
from routes.exercise_routes import exercise_blueprint
from routes.auth_routes import auth_blueprint


test_app = Flask("__main__")
test_app.register_blueprint(exercise_blueprint)
test_app.register_blueprint(auth_blueprint)
test_app.run(host="localhost", port="8080")

# Check against endpoints from user_routes.py in Postman

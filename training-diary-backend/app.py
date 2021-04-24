from flask import Flask
from routes.auth_routes import auth_blueprint
from routes.body_routes import body_blueprint
from routes.diet_routes import diet_blueprint
from routes.exercise_routes import exercise_blueprint
from routes.user_routes import user_blueprint

# driver code
app = Flask(__name__)
if __name__ == "__main__":
    app.register_blueprint(auth_blueprint)
    app.register_blueprint(body_blueprint)
    app.register_blueprint(diet_blueprint)
    app.register_blueprint(exercise_blueprint)
    app.register_blueprint(user_blueprint)
    app.run()

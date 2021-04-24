from flask import Blueprint, request
from controllers import ApiAuthController, ExerciseController


exercise_blueprint = Blueprint("exercise_blueprint", __name__)
auth = ApiAuthController.ApiAuthController()
exercise_controller = ExerciseController.ExerciseController()


@exercise_blueprint.route("/api/exercise/getExercises", methods=["GET"])
def get_exercises():
    token = request.headers.get("token")
    user_id = request.headers.get("user_id")
    if auth.is_valid_token(token, user_id):
        return exercise_controller.get_exercises(user_id)
    return auth.generate_unauthorized_response()


@exercise_blueprint.route("/api/exercise/getEntries", methods=["GET"])
def get_entries():
    token = request.headers.get("token")
    user_id = request.headers.get("user_id")
    if auth.is_valid_token(token, user_id):
        return exercise_controller.get_entries_by_user(user_id)
    return auth.generate_unauthorized_response()


@exercise_blueprint.route("/api/exercise/postExercises", methods=["POST"])
def post_exercises():
    token = request.headers.get("token")
    user_id = request.headers.get("user_id")
    data = request.get_json().get("data")
    if auth.is_valid_token(token, user_id) and auth.is_valid_payload(user_id, data):
        return exercise_controller.create_exercises(data)
    return auth.generate_unauthorized_response()


@exercise_blueprint.route("/api/exercise/postEntries", methods=["POST"])
def post_entries():
    token = request.headers.get("token")
    user_id = request.headers.get("user_id")
    data = request.get_json().get("data")
    if auth.is_valid_token(token, user_id) and auth.is_valid_payload(user_id, data):
        return exercise_controller.create_entries(data)
    return auth.generate_unauthorized_response()


@exercise_blueprint.route("/api/exercise/putExercise", methods=["POST", "PUT"])
def put_exercise():
    token = request.headers.get("token")
    user_id = request.headers.get("user_id")
    data = request.get_json().get("data")
    if auth.is_valid_token(token, user_id) and auth.is_valid_payload(user_id, data):
        return exercise_controller.update_exercise(data)
    return auth.generate_unauthorized_response()


@exercise_blueprint.route("/api/exercise/putEntry", methods=["POST", "PUT"])
def put_entry():
    token = request.headers.get("token")
    user_id = request.headers.get("user_id")
    data = request.get_json().get("data")
    if auth.is_valid_token(token, user_id) and auth.is_valid_payload(user_id, data):
        return exercise_controller.update_entry(data)
    return auth.generate_unauthorized_response()


@exercise_blueprint.route("/api/exercise/deleteExercise/<exercise_id>", methods=["POST", "DELETE"])
def delete_exercise(exercise_id):
    token = request.headers.get("token")
    user_id = request.headers.get("user_id")
    if auth.is_valid_token(token, user_id):
        return exercise_controller.delete_exercise(exercise_id)
    return auth.generate_unauthorized_response()


@exercise_blueprint.route("/api/exercise/deleteEntry/<exercise_entry_id>", methods=["POST", "DELETE"])
def delete_entry(exercise_entry_id):
    token = request.headers.get("token")
    user_id = request.headers.get("user_id")
    if auth.is_valid_token(token, user_id):
        return exercise_controller.delete_entry(exercise_entry_id)
    return auth.generate_unauthorized_response()


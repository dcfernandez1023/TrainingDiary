from flask import Blueprint, request
from controllers import ApiAuthController, DietController


diet_blueprint = Blueprint("diet_blueprint", __name__)
auth = ApiAuthController.ApiAuthController()
diet_controller = DietController.DietController()


@diet_blueprint.route("/api/diet/getEntries", methods=["GET"])
def get_entries():
    token = request.headers.get("token")
    user_id = request.headers.get("user_id")
    if auth.is_valid_token(token, user_id):
        return diet_controller.get_entries(user_id)
    return auth.generate_unauthorized_response()


@diet_blueprint.route("/api/diet/postEntry", methods=["POST"])
def post_entry():
    token = request.headers.get("token")
    user_id = request.headers.get("user_id")
    data = request.get_json().get("data")
    if auth.is_valid_token(token, user_id):
        return diet_controller.create_entry(data)
    return auth.generate_unauthorized_response()


@diet_blueprint.route("/api/diet/putEntry", methods=["POST", "PUT"])
def put_entry():
    token = request.headers.get("token")
    user_id = request.headers.get("user_id")
    data = request.get_json().get("data")
    if auth.is_valid_token(token, user_id):
        return diet_controller.update_entry(data)
    return auth.generate_unauthorized_response()


@diet_blueprint.route("/api/diet/deleteEntry/<day>/<month>/<year>", methods=["POST", "DELETE"])
def delete_entry(day, month, year):
    token = request.headers.get("token")
    user_id = request.headers.get("user_id")
    if auth.is_valid_token(token, user_id):
        return diet_controller.delete_entry(user_id, day, month, year)
    return auth.generate_unauthorized_response()

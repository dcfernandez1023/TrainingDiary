from flask import Blueprint, request
from controllers import ApiAuthController, UserController


user_blueprint = Blueprint("user_blueprint", __name__)
auth = ApiAuthController.ApiAuthController()
user_controller = UserController.UserController()


@user_blueprint.route("/api/user/getUser", methods=["GET"])
def get_user():
    token = request.headers.get("token")
    user_id = request.headers.get("user_id")
    if auth.is_valid_token(token, user_id):
        return user_controller.get(user_id)
    return auth.generate_unauthorized_response()


@user_blueprint.route("/api/user/postUser", methods=["POST"])
def post_user():
    # TODO: USE FIREBASE TO CREATE NEW USER
    data = request.get_json().get("data")
    return user_controller.create(data)


@user_blueprint.route("/api/user/putUser", methods=["POST"])
def put_user():
    token = request.headers.get("token")
    user_id = request.headers.get("user_id")
    data = request.get_json().get("data")
    if auth.is_valid_token(token, user_id):
        return user_controller.update(data)
    return auth.generate_unauthorized_response()


@user_blueprint.route("/api/user/deleteUser", methods=["DELETE"])
def delete_user():
    token = request.headers.get("token")
    user_id = request.headers.get("user_id")
    if auth.is_valid_token(token, user_id):
        return user_controller.delete(user_id)
    return auth.generate_unauthorized_response()

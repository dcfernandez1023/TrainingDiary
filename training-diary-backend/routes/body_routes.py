from flask import Blueprint, request
from controllers import ApiAuthController, BodyController


body_blueprint = Blueprint("body_blueprint", __name__)
auth = ApiAuthController.ApiAuthController()
body_controller = BodyController.BodyController()


@body_blueprint.route("/api/body/getAll", methods=["GET"])
def get_all():
    token = request.headers.get("token")
    user_id = request.headers.get("user_id")
    if auth.is_valid_token(token, user_id):
        return body_controller.get_all(user_id)
    return auth.generate_unauthorized_response()


@body_blueprint.route("/api/body/postBwEntry", methods=["POST"])
def post_bw_entry():
    token = request.headers.get("token")
    user_id = request.headers.get("user_id")
    data = request.get_json().get("data")
    if auth.is_valid_token(token, user_id) and auth.is_valid_payload(user_id, data):
        return body_controller.create_bw_entry(data)
    return auth.generate_unauthorized_response()


@body_blueprint.route("/api/body/postBfEntry", methods=["POST"])
def post_bf_entry():
    token = request.headers.get("token")
    user_id = request.headers.get("user_id")
    data = request.get_json().get("data")
    if auth.is_valid_token(token, user_id) and auth.is_valid_payload(user_id, data):
        return body_controller.create_bf_entry(data)
    return auth.generate_unauthorized_response()


@body_blueprint.route("/api/body/putBwEntry", methods=["POST", "PUT"])
def put_bw_entry():
    token = request.headers.get("token")
    user_id = request.headers.get("user_id")
    data = request.get_json().get("data")
    if auth.is_valid_token(token, user_id) and auth.is_valid_payload(user_id, data):
        return body_controller.update_bw_entry(data)
    return auth.generate_unauthorized_response()


@body_blueprint.route("/api/body/putBfEntry", methods=["POST", "PUT"])
def put_bf_entry():
    token = request.headers.get("token")
    user_id = request.headers.get("user_id")
    data = request.get_json().get("data")
    if auth.is_valid_token(token, user_id) and auth.is_valid_payload(user_id, data):
        return body_controller.update_bf_entry(data)
    return auth.generate_unauthorized_response()


@body_blueprint.route("/api/body/deleteBwEntry/<bw_id>", methods=["POST", "DELETE"])
def delete_bw_entry(bw_id):
    token = request.headers.get("token")
    user_id = request.headers.get("user_id")
    if auth.is_valid_token(token, user_id):
        return body_controller.delete_bw_entry(bw_id)
    return auth.generate_unauthorized_response()


@body_blueprint.route("/api/body/deleteBfEntry/<bf_id>", methods=["POST", "DELETE"])
def delete_bf_entry(bf_id):
    token = request.headers.get("token")
    user_id = request.headers.get("user_id")
    if auth.is_valid_token(token, user_id):
        return body_controller.delete_bf_entry(bf_id)
    return auth.generate_unauthorized_response()

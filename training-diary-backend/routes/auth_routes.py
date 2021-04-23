from flask import Blueprint, request
from controllers import ApiAuthController
from models import User, DbAccess


auth_blueprint = Blueprint("auth_blueprint", __name__)


@auth_blueprint.route("/api/auth/getApiToken", methods=["GET"])
def get_api_token():
    auth = ApiAuthController.ApiAuthController()
    user = User.User(DbAccess.DbAccess())
    user_id = request.headers.get("user_id")
    if user.get_user_info(user_id) is not None:
        return {"token": auth.encode_token(user_id)}
    return auth.generate_unauthorized_response()

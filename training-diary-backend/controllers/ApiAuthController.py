# Controller for api authentication

import jwt
import datetime
import os
from utilities import error_logger
from flask import make_response


class ApiAuthController:
    def __init__(self):
        self.__secret_key = os.getenv("TD_API_AUTH")

    def tokenize_response_header(self, res, user_id):
        res.headers["token"] = self.encode_token(user_id)
        return res

    def encode_token(self, user_id):
        try:
            payload = {
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=10),
                'iat': datetime.datetime.utcnow(),
                'sub': user_id
            }
            return jwt.encode(
                payload,
                self.__secret_key,
                algorithm="HS256"
            )
        except Exception:
            error_logger.log_error()
            return None

    def is_valid_token(self, token, user_id):
        decode = self.__decode_token(token)
        if decode is not None and decode == user_id:
            return True
        return False

    def generate_unauthorized_response(self):
        return make_response({"message": "Not authorized"}, 401)

    # Checks the data being sent in to ensure that the data truly belongs to the user sending the request.
    # Since all objects/schemas of this application have a user_id, this checks against the user_id from
    # the request and the user_id from the request's payload to ensure they match
    def is_valid_payload(self, user_id, data):
        payload_user_id = ""
        if isinstance(data, dict):
            payload_user_id = data.get("user_id")
        elif isinstance(data, str):
            payload_user_id = data
        elif isinstance(data, list):
            for obj in data:
                payload_user_id = obj.get("user_id")
                if payload_user_id is None or user_id is None:
                    return False
                if payload_user_id != user_id:
                    return False
            return True
        if payload_user_id is None or user_id is None:
            return False
        if payload_user_id == user_id:
            return True
        return False

    def __decode_token(self, token):
        try:
            payload = jwt.decode(token, self.__secret_key, algorithms="HS256")
            return payload["sub"]
        except Exception as e:
            return None

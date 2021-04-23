# Controller for api authentication

import jwt
import datetime
import os
from utilities import error_logger
from flask import make_response


class ApiAuthController:
    def __init__(self):
        self.__secret_key = os.getenv("TD_API_AUTH")

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
        return make_response({}, 401)

    def __decode_token(self, token):
        try:
            payload = jwt.decode(token, self.__secret_key, algorithms="HS256")
            return payload["sub"]
        except Exception as e:
            return None

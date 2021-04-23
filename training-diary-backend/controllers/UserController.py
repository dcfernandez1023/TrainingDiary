# Controller class for the User model

from models import DbAccess, User
from flask import make_response
from utilities import error_logger


class UserController:
    # Constructor - initializes a User model object and a DbAccess model object
    def __init__(self):
        self.__db = DbAccess.DbAccess()
        self.__user = User.User(self.__db)

    # Gets user info
    # @param user_id - unique identifier of the user
    def get(self, user_id):
        try:
            data = self.__user.get_user_info(user_id)
            # if data is None, return 204 (no content)
            if data is None:
                return make_response({}, 204)
            return make_response(data, 200)
        except Exception:
            error_logger.log_error()
            return make_response({}, 500)
        finally:
            self.__db.close_connection()

    # Creates a new user
    # @param data - json/dictionary coming from endpoint containing user data
    def create(self, data):
        try:
            user_id = data.get("user_id")
            email = data.get("email")
            name = data.get("name")
            # if insufficient data was provided to create a user, return 400 (bad request)
            if user_id is None or email is None or name is None:
                return make_response({}, 400)
            self.__user.create_new_user(user_id, email, name)
            return make_response({}, 200)
        except Exception:
            error_logger.log_error()
            return make_response({}, 500)
        finally:
            self.__db.close_connection()

    # Updates a user
    # @param user_id - unique identifier of the user
    # @param data - json/dictionary coming from endpoint containing user data to be updated
    def update(self, data):
        try:
            user_id = data.get("user_id")
            if user_id is None:
                return make_response({}, 400)
            self.__user.update_user_info(user_id, data)
            return make_response({}, 200)
        except Exception:
            error_logger.log_error()
            return make_response({}, 500)
        finally:
            self.__db.close_connection()

    # Deletes a user
    # @param user_id - unique identifier of the user
    def delete(self, user_id):
        try:
            self.__user.delete_user(user_id)
            self.__db.close_connection()
            return make_response({}, 200)
        except Exception:
            self.__db.close_connection()
            error_logger.log_error()
            return make_response({}, 500)
        finally:
            self.__db.close_connection()

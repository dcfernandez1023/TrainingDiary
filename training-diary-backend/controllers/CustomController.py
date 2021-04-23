# Controller class for Exercise model

from models import Custom
from db import DbAccess
from flask import make_response
from utilities import error_logger
import uuid


class CustomController:
    def __init__(self):
        self.__db = DbAccess.DbAccess()
        self.__custom = Custom.Custom(self.__db)

    def get_types(self, user_id):
        try:
            data = self.__custom.get_user_custom_types(user_id)
            return make_response({"data": data}, 200)
        except Exception:
            error_logger.log_error()
            return make_response({}, 500)
        finally:
            self.__db.close_connection()

    def get_entries(self, user_id):
        try:
            data = self.__custom.get_user_custom_entries(user_id)
            return make_response({"data": data}, 200)
        except Exception:
            error_logger.log_error()
            return make_response({}, 500)
        finally:
            self.__db.close_connection()

    def create_type(self, data):
        try:
            custom_id = "custom" + str(uuid.uuid1())
            user_id = data.get("user_id")
            custom_schema = data.get("custom_schema")
            if custom_id is None or user_id is None or custom_schema is None:
                return make_response({}, 400)
            self.__custom.create_new_custom_type(custom_id, user_id, custom_schema)
            return make_response({"custom_id": custom_id}, 200)
        except Exception:
            error_logger.log_error()
            return make_response({}, 500)
        finally:
            self.__db.close_connection()

    def create_entry(self, data):
        try:
            custom_entry_id = "custom_entry" + str(uuid.uuid1())
            custom_id = data.get("custom_id")
            user_id = data.get("user_id")
            custom_entry = data.get("custom_entry")
            timestamp = data.get("timestamp")
            day = data.get("day")
            month = data.get("month")
            year = data.get("year")
            notes = data.get("notes")
            if custom_entry_id is None or custom_id is None or user_id is None or custom_entry is None \
            or timestamp is None or day is None or month is None or year is None or notes is None:
                return make_response({}, 400)
        except Exception:
            error_logger.log_error()
            return make_response({}, 500)
        finally:
            self.__db.close_connection()

    def update_type(self, data):
        try:
            custom_id = data.get("custom_id")
            if custom_id is None:
                return make_response({}, 400)
            self.__custom.update_custom_type(custom_id, data)
            return make_response({}, 200)
        except Exception:
            error_logger.log_error()
            return make_response({}, 500)
        finally:
            self.__db.close_connection()

    def update_entry(self, data):
        try:
            custom_entry_id = data.get("custom_entry_id")
            if custom_entry_id is None:
                return make_response({}, 400)
            self.__custom.update_custom_entry(custom_entry_id, data)
            return make_response({}, 200)
        except Exception:
            error_logger.log_error()
            return make_response({}, 500)
        finally:
            self.__db.close_connection()

    def delete_type(self, custom_id):
        try:
            self.__custom.delete_custom_type(custom_id)
            return make_response({}, 200)
        except Exception:
            error_logger.log_error()
            return make_response({}, 500)
        finally:
            self.__db.close_connection()

    def delete_entry(self, custom_entry_id):
        try:
            self.__custom.delete_custom_entry(custom_entry_id)
            return make_response({}, 200)
        except Exception:
            error_logger.log_error()
            return make_response({}, 500)
        finally:
            self.__db.close_connection()

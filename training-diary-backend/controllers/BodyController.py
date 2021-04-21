# Controller class for Body model

from models import DbAccess, Body
from flask import make_response
from utilities import error_logger
import uuid


# TODO: implement API authentication and return API tokens on success
class BodyController:
    def __init__(self):
        self.__db = DbAccess.DbAccess()
        self.__body = Body.Body(self.__db)

    # Gets all user body entries - both body weight and body fat
    # @param user_id - unique identifier of the user
    def get_all(self, user_id):
        try:
            data = self.__body.get_user_body_entries(user_id)
            self.__db.close_connection()
            return make_response(data, 200)
        except Exception:
            self.__db.close_connection()
            error_logger.log_error()
            return make_response({}, 500)

    # Gets a body weight entry by id
    # @param bw_id - unique identifier of the body weight entry
    def get_bw_entry(self, bw_id):
        try:
            data = self.__body.get_body_weight_entry_by_id(bw_id)
            self.__db.close_connection()
            return make_response(data, 200)
        except Exception:
            self.__db.close_connection()
            error_logger.log_error()
            return make_response({}, 500)

    # Gets a body fat entry by id
    # @param bf_id - unique identifier of the body fat entry
    def get_bf_entry(self, bf_id):
        try:
            data = self.__body.get_body_fat_entry_by_id(bf_id)
            self.__db.close_connection()
            return make_response(data, 200)
        except Exception:
            self.__db.close_connection()
            error_logger.log_error()
            return make_response({}, 500)

    # Creates a body weight entry with the given json/dictionary data
    # @param data - json/dictionary data coming from http request
    def create_bw_entry(self, data):
        try:
            for attribute in Body.Body.BODY_WEIGHT_SCHEMA:
                if data.get(attribute) is None:
                    self.__db.close_connection()
                    return make_response({}, 400)
            bw_id = str(uuid.uuid1())
            user_id = data.get("user_id")
            weight = data.get("weight")
            units = data.get("units")
            timestamp = data.get("timestamp")
            day = data.get("day")
            month = data.get("month")
            year = data.get("year")
            notes = data.get("notes")
            self.__body.create_new_body_weight_entry(bw_id, user_id, weight, units, timestamp, day, month, year, notes)
            self.__db.close_connection()
            return make_response({}, 200)
        except Exception:
            self.__db.close_connection()
            error_logger.log_error()
            return make_response({}, 500)



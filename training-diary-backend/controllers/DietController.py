# Controller class for Diet model

from models import Diet
from db import DbAccess
from flask import make_response
from utilities import error_logger


class DietController:
    def __init__(self):
        self.__db = DbAccess.DbAccess()
        self.__diet = Diet.Diet(self.__db)

    def get_entry(self, user_id, day, month, year):
        try:
            data = self.__diet.get_user_diet_entry(user_id, day, month, year)
            if data is None:
                return make_response({}, 204)
            return make_response(data, 200)
        except Exception:
            error_logger.log_error()
            return make_response({}, 500)
        finally:
            self.__db.close_connection()

    def get_entries(self, user_id):
        try:
            data = self.__diet.get_user_diet_entries(user_id)
            return make_response({"data": data}, 200)
        except Exception:
            error_logger.log_error()
            return make_response({}, 500)
        finally:
            self.__db.close_connection()

    def create_entry(self, data):
        try:
            user_id = data.get("user_id")
            day = int(data.get("day"))
            month = int(data.get("month"))
            year = int(data.get("year"))
            calories = data.get("calories")
            protein = data.get("protein")
            carbs = data.get("carbs")
            fat = data.get("fat")
            notes = data.get("notes")
            if user_id is None or day is None or month is None or year is None or calories is None or protein is None \
            or carbs is None or fat is None or notes is None:
                return make_response({}, 400)
            self.__diet.create_new_diet_entry(user_id, day, month, year, calories, protein, carbs, fat, notes)
            return make_response({}, 200)
        except Exception:
            error_logger.log_error()
            return make_response({}, 500)
        finally:
            self.__db.close_connection()

    def update_entry(self, data):
        try:
            user_id = data.get("user_id")
            day = int(data.get("day"))
            month = int(data.get("month"))
            year = int(data.get("year"))
            if user_id is None or day is None or month is None or year is None:
                return make_response({}, 400)
            self.__diet.update_diet_entry(user_id, day, month, year, data)
            return make_response({}, 200)
        except Exception:
            error_logger.log_error()
            return make_response({}, 500)
        finally:
            self.__db.close_connection()

    def delete_entry(self, user_id, day, month, year):
        try:
            day = int(day)
            month = int(month)
            year = int(year)
            self.__diet.delete_diet_entry(user_id, day, month, year)
            return make_response({}, 200)
        except Exception:
            error_logger.log_error()
            return make_response({}, 500)
        finally:
            self.__db.close_connection()

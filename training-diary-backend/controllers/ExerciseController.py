# Controller class for Exercise model

from models import Exercise
from db import DbAccess
from flask import make_response
from utilities import error_logger
import uuid


class ExerciseController:
    def __init__(self):
        self.__db = DbAccess.DbAccess()
        self.__exercise = Exercise.Exercise(self.__db)

    def get_exercises(self, user_id):
        try:
            data = self.__exercise.get_user_exercises(user_id)
            return make_response({"data": data}, 200)
        except Exception:
            error_logger.log_error()
            return make_response({}, 500)
        finally:
            self.__db.close_connection()

    def get_entries_by_exercise(self, exercise_id):
        try:
            data = self.__exercise.get_exercise_entries_by_exercise_id(exercise_id)
            return make_response({"data": data}, 200)
        except Exception:
            error_logger.log_error()
            return make_response({}, 500)
        finally:
            self.__db.close_connection()

    def get_entries_by_user(self, user_id):
        try:
            data = self.__exercise.get_user_exercise_entries(user_id)
            return make_response({"data": data}, 200)
        except Exception:
            error_logger.log_error()
            return make_response({}, 500)
        finally:
            self.__db.close_connection()

    def get_entries_by_year(self, user_id, year):
        try:
            data = self.__exercise.get_user_exercise_entries_by_year(user_id, year)
            return make_response({"data": data}, 200)
        except Exception:
            error_logger.log_error()
            return make_response({}, 500)
        finally:
            self.__db.close_connection()

    # Creates one or many exercises
    # @param data - a list of json/dictionaries containing the data for the exercises
    def create_exercises(self, data):
        try:
            exercises = []
            for exercise in data:
                fields = []
                exercise_id = "exercise_entry" + str(uuid.uuid1())
                exercise.update({"exercise_entry_id": exercise_id})
                for attribute in self.__exercise.EXERCISE_SCHEMA:
                    value = exercise.get(attribute)
                    if value is None:
                        return make_response({}, 400)
                    fields.append(value)
                exercises.append(fields)
            self.__exercise.create_new_exercises(exercises)
            return make_response({"data": exercises}, 200)
        except Exception:
            error_logger.log_error()
            return make_response({}, 500)
        finally:
            self.__db.close_connection()

    # Creates one or many exercise entries
    # @param data- a list of json/dictionaries containing the data for the exercise entries
    def create_entries(self, data):
        try:
            entries = []
            for entry in data:
                fields = []
                exercise_entry_id = "exercise_entry" + str(uuid.uuid1())
                entry.update({"exercise_entry_id": exercise_entry_id})
                for attribute in self.__exercise.EXERCISE_ENTRY_SCHEMA:
                    value = entry.get(attribute)
                    if value is None:
                        return make_response({}, 400)
                    fields.append(value)
                entries.append(fields)
            self.__exercise.create_new_exercise_entries(entries)
            return make_response({"data": entries}, 200)
        except Exception:
            error_logger.log_error()
            return make_response({}, 500)
        finally:
            self.__db.close_connection()

    def update_exercise(self, data):
        try:
            for key in data.keys():
                if key not in self.__exercise.EXERCISE_SCHEMA:
                    return make_response({}, 400)
            exercise_id = data.get("exercise_id")
            if exercise_id is None:
                return make_response({}, 400)
            self.__exercise.update_exercise(exercise_id, data)
            return make_response({}, 200)
        except Exception:
            error_logger.log_error()
            return make_response({}, 500)
        finally:
            self.__db.close_connection()

    def update_entry(self, data):
        try:
            for key in data.keys():
                if key not in self.__exercise.EXERCISE_ENTRY_SCHEMA:
                    return make_response({}, 400)
            exercise_entry_id = data.get("exercise_id")
            if exercise_entry_id is None:
                return make_response({}, 400)
            self.__exercise.update_exercise_entry(exercise_entry_id, data)
            return make_response({}, 200)
        except Exception:
            error_logger.log_error()
            return make_response({}, 500)
        finally:
            self.__db.close_connection()

    def delete_exercise(self, exercise_id):
        try:
            self.__exercise.delete_exercise(exercise_id)
            return make_response({}, 200)
        except Exception:
            error_logger.log_error()
            return make_response({}, 500)
        finally:
            self.__db.close_connection()

    def delete_entry(self, exercise_entry_id):
        try:
            self.__exercise.delete_exercise_entry_by_id(exercise_entry_id)
            return make_response({}, 200)
        except Exception:
            error_logger.log_error()
            return make_response({}, 500)
        finally:
            self.__db.close_connection()

# Exercise model object. Contains methods for CRUD operations on user's exercise data

import time
from models import DbAccess, QueryBuilder
from utilities import util


class Exercise:
    SCHEMA = ("exercise_id", "user_id", "name", "category", "sets", "reps", "amount", "units")
    TABLE = "Exercises"

    def __init__(self):
        self.__query_builder = QueryBuilder.QueryBuilder()

    def get_user_exercises(self, user_id):
        db = DbAccess.DbAccess()
        query = self.__query_builder.build_select_query([self.TABLE], [], {"user_id": ["user_id", "=", user_id]})
        data = db.get_data(query)
        db.close_connection()
        return util.to_jsons(self.SCHEMA, data)

    def get_exercise_by_id(self, exercise_id):
        db = DbAccess.DbAccess()
        query = self.__query_builder.build_select_query([self.TABLE], [],
                                                        {"exercise_id": ["exercise_id", "=", exercise_id]})
        data = db.get_data(query)
        if len(data) > 1:
            raise Exception("DuplicateExerciseIds")
        if len(data) == 0:
            return None
        db.close_connection()
        return util.to_json(self.SCHEMA, data[0])

    def create_new_exercise(self, user_id, name, category, sets, reps, amount, units):
        # TODO: generate id in controller
        exercise_id = "exercise_" + user_id + str(time.time())
        db = DbAccess.DbAccess()
        query = self.__query_builder.build_insert_query(self.TABLE, [
            (exercise_id, user_id, name, category, sets, reps, amount, units)])
        db.insert_data(query)
        db.close_connection()

    # Creates many new exercises
    # @param exercises - a list of lists where each inner list holds the data for an exercise
    def create_new_exercises(self, exercises):
        db = DbAccess.DbAccess()
        # TODO: generate ids in controller
        query = self.__query_builder.build_insert_query(self.TABLE, exercises)
        db.insert_data(query)
        db.close_connection()

    def update_exercise(self, exercise_id, data):
        db = DbAccess.DbAccess()
        query = self.__query_builder.build_update_query(self.TABLE, data,
                                                        {"exercise_id": ["exercise_id", "=", exercise_id]})
        db.update_data(query)
        db.close_connection()

    def delete_exercise(self, exercise_id):
        db = DbAccess.DbAccess()
        query = self.__query_builder.build_delete_query(self.TABLE, {"exercise_id": ["exercise_id", "=", exercise_id]})
        db.delete_data(query)
        db.close_connection()


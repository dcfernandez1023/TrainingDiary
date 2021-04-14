# Workout model object. Contains methods for CRUD operations on user's workout data and the exercise objects
# associated with the user's workout

import time
from models import DbAccess, QueryBuilder


class Workout:
    def __init__(self):
        self.__query_builder = QueryBuilder.QueryBuilder()

    def get_user_workouts(self, user_id):
        db = DbAccess.DbAccess()
        query = self.__query_builder.build_select_query(["Workouts"], [], {"user_id": ["user_id", "=", user_id]})
        data = db.get_data(query)
        db.close_connection()
        return data

    def get_workout_by_id(self, workout_id):
        db = DbAccess.DbAccess()
        query = self.__query_builder.build_select_query(["Workouts"], [], {"workout_id": ["workout_id", "=", workout_id]})
        data = db.get_data(query)
        if len(data) > 1:
            raise Exception("DuplicateWorkoutIds")
        if len(data) == 0:
            return None
        db.close_connection()
        return data[0]

    def get_public_workouts(self):
        db = DbAccess.DbAccess()
        query = self.__query_builder.build_select_query(["Workouts"], [], {"is_public": ["is_public", "=", 1]})
        data = db.get_data(query)
        db.close_connection()
        return data

    def create_new_workout(self, user_id, name, date_created, is_public, description):
        workout_id = "workout_" + user_id + str(time.time())
        db = DbAccess.DbAccess()
        query = self.__query_builder.build_insert_query("Workouts", [(workout_id, user_id, name, date_created, is_public, description)])
        db.insert_data(query)
        db.close_connection()
        return workout_id

    def update_workout(self, workout_id, data):
        db = DbAccess.DbAccess()
        query = self.__query_builder.build_update_query("Workouts", data, {"workout_id": ["workout_id", "=", workout_id]})
        db.update_data(query)
        db.close_connection()

    def delete_workout(self, workout_id):
        db = DbAccess.DbAccess()
        query = self.__query_builder.build_delete_query("Workouts", {"workout_id": ["workout_id", "=", workout_id]})
        db.delete_data(query)
        db.close_connection()

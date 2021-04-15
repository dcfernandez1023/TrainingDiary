# NOTE: THIS CLASS WILL NOT BE USED FOR NOW. DUE TO DESIGN CHANGES, WORKOUTS WILL NO LONGER BE USED AS CONTAINERS
# FOR EXERCISES.
# Workout model object. Contains methods for CRUD operations on user's workout data and the exercise objects
# associated with the user's workout

import time
from models import DbAccess, QueryBuilder, Exercise
from utilities import util


class Workout:
    SCHEMA = ("workout_id", "user_id", "name", "date_created", "is_public", "description")
    TABLE = "Workouts"

    def __init__(self):
        self.__query_builder = QueryBuilder.QueryBuilder()

    def get_user_workouts(self, user_id):
        db = DbAccess.DbAccess()
        query = self.__query_builder.build_select_query([self.TABLE], [], {"user_id": ["user_id", "=", user_id]})
        data = db.get_data(query)
        db.close_connection()
        return util.to_jsons(self.SCHEMA, data)

    def get_workout_by_id(self, workout_id):
        db = DbAccess.DbAccess()
        query = self.__query_builder.build_select_query([self.TABLE], [],
                                                        {"workout_id": ["workout_id", "=", workout_id]})
        data = db.get_data(query)
        if len(data) > 1:
            raise Exception("DuplicateWorkoutIds")
        if len(data) == 0:
            return None
        db.close_connection()
        return util.to_json(self.SCHEMA, data[0])

    def get_public_workouts(self):
        db = DbAccess.DbAccess()
        query = self.__query_builder.build_select_query([self.TABLE], [], {"is_public": ["is_public", "=", 1]})
        data = db.get_data(query)
        db.close_connection()
        return util.to_jsons(self.SCHEMA, data)

    def create_new_workout(self, user_id, name, date_created, is_public, description):
        # TODO: make this id generation more unique
        workout_id = "workout_" + user_id + str(time.time())
        db = DbAccess.DbAccess()
        query = self.__query_builder.build_insert_query(self.TABLE, [
            (workout_id, user_id, name, date_created, is_public, description)])
        db.insert_data(query)
        db.close_connection()
        return workout_id

    def update_workout(self, workout_id, data):
        db = DbAccess.DbAccess()
        query = self.__query_builder.build_update_query(self.TABLE, data,
                                                        {"workout_id": ["workout_id", "=", workout_id]})
        db.update_data(query)
        db.close_connection()

    def delete_workout(self, workout_id):
        db = DbAccess.DbAccess()
        query = self.__query_builder.build_delete_query(self.TABLE, {"workout_id": ["workout_id", "=", workout_id]})
        db.delete_data(query)
        db.close_connection()

    def get_user_workouts_with_exercises(self, user_id):
        db = DbAccess.DbAccess()
        workout_query = self.__query_builder.build_select_query([self.TABLE], [],
                                                                {"user_id": ["user_id", "=", user_id]})
        exercise_query = self.__query_builder.build_select_query(["Exercises"], [],
                                                                 {"user_id": ["user_id", "=", user_id]})
        workouts = db.get_data(workout_query)
        exercises = db.get_data(exercise_query)

        # merge workouts & exercises by converting workouts & exercises into dictionaries and matching their workout_ids
        workout_dict = util.tups_to_dict(workouts, self.SCHEMA)
        workouts_with_exercises = self.__merge_workouts_and_exercises(workout_dict, exercises)
        return workouts_with_exercises

    # merges workouts and exercises into one nested object
    # @param workout_dict - dictionary of workouts; key=unique workout_id, value=dictionary representation of workout
    # @param exercises - a list of tuples containing the exercise entities from the database
    def __merge_workouts_and_exercises(self, workout_dict, exercises):
        workouts_with_exercises = []
        for workout_id in workout_dict:
            workout = workout_dict.get(workout_id)
            exercises_with_workout = []
            for exercise in exercises:
                if exercise[1] == workout_id:
                    exercise_dict = dict(zip(Exercise.Exercise.SCHEMA, exercise))
                    exercises_with_workout.append(exercise_dict)
            workout.update({"exercises": exercises_with_workout})
            workouts_with_exercises.append(workout)
        return workouts_with_exercises



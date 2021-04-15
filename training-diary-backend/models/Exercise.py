# Workout model object. Contains methods for CRUD operations on user's workout data and the exercise objects
# associated with the user's workout

from models import DbAccess, QueryBuilder


class Exercise:
    schema = ("workout_id", "user_id", "name", "category", "sets", "reps", "amount", "units")

    def __init__(self):
        self.__query_builder = QueryBuilder.QueryBuilder()

    def get_exercises_by_user_id(self, user_id):
        db = DbAccess.DbAccess()
        query = "SELECT * " \
                "FROM Exercises" \
                "WHERE user_id = " + "'" + user_id + "'"
        data = db.get_data(query)
        db.close_connection()
        return data

    def get_exercises_by_workout_id(self, workout_id):
        db = DbAccess.DbAccess()
        query = "SELECT * " \
                "FROM Exercises" \
                "WHERE workout_id = " + "'" + workout_id + "'"
        data = db.get_data(query)
        db.close_connection()
        return data

# Workout model object. Contains methods for CRUD operations on user's workout data and the exercise objects
# associated with the user's workout

from models import DbAccess, QueryBuilder


class Exercise:
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

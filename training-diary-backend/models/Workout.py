# Workout model object. Contains methods for CRUD operations on user's workout data

from models import DbAccess


class Workout():
    def get_user_workouts(self, user_id):
        db = DbAccess.DbAccess("../db/data/training_diary_db")
        query = "SELECT * " \
                "FROM Workouts" \
                "WHERE user_id = " + "'" + user_id + "'"
        data = db.get_data(query)
        db.close_connection()
        return data

    def get_user_exercises(self, user_id):
        db = DbAccess.DbAccess("../db/data/training_diary_db")
        query = "SELECT * " \
                "FROM Exercises" \
                "WHERE user_id = " + "'" + user_id + "'"
        data = db.get_data(query)
        db.close_connection()
        return data

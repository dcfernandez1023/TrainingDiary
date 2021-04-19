# Exercise model object. Contains methods for CRUD operations on user's exercise data

from models import DbAccess, QueryBuilder
from utilities import util


class Exercise:
    EXERCISE_SCHEMA = ("exercise_id", "user_id", "name", "category", "sets", "reps", "amount", "units")
    EXERCISE_ENTRY_SCHEMA = ("exercise_entry_id", "exercise_id", "user_id", "timestamp", "day", "month", "year", "notes")
    EXERCISE_TABLE = "Exercises"
    EXERCISE_ENTRY_TABLE = "ExerciseEntries"

    def __init__(self):
        self.__query_builder = QueryBuilder.QueryBuilder()

    def get_user_exercises(self, user_id):
        db = DbAccess.DbAccess()
        query = self.__query_builder.build_select_query([self.EXERCISE_TABLE], [], {"user_id": ["user_id", "=", user_id]})
        data = db.get_data(query)
        db.close_connection()
        return util.to_jsons(self.EXERCISE_SCHEMA, data)

    def get_exercise_by_id(self, exercise_id):
        db = DbAccess.DbAccess()
        query = self.__query_builder.build_select_query([self.EXERCISE_TABLE], [],
                                                        {"exercise_id": ["exercise_id", "=", exercise_id]})
        data = db.get_data(query)
        if len(data) > 1:
            raise Exception("DuplicateExerciseIds")
        if len(data) == 0:
            return None
        db.close_connection()
        return util.to_json(self.EXERCISE_SCHEMA, data[0])

    def get_exercise_entries_by_exercise_id(self, exercise_id):
        db = DbAccess.DbAccess()
        query = self.__query_builder.build_select_query([self.EXERCISE_ENTRY_TABLE], [],
                                                        {"exercise_id":
                                                             ["exercise_id", "=", exercise_id]})
        data = db.get_data(query)
        db.close_connection()
        return util.to_jsons(self.EXERCISE_ENTRY_SCHEMA, data)

    def get_user_exercise_entries(self, user_id):
        db = DbAccess.DbAccess()
        query = self.__query_builder.build_select_query([self.EXERCISE_ENTRY_TABLE], [],
                                                        {"user_id": ["user_id", "=", user_id]})
        data = db.get_data(query)
        db.close_connection()
        return util.to_jsons(self.EXERCISE_ENTRY_SCHEMA, data)

    def get_user_exercise_entries_by_year(self, user_id, year):
        db = DbAccess.DbAccess()
        query = self.__query_builder.build_select_query([self.EXERCISE_ENTRY_TABLE], [],
                                                        {
                                                            "user_id": ["user_id", "=", user_id],
                                                            "year": ["year", "=", year]
                                                        })
        data = db.get_data(query)
        db.close_connection()
        return util.to_jsons(self.EXERCISE_ENTRY_SCHEMA, data)

    def create_new_exercise(self, exercise_id, user_id, name, category, sets, reps, amount, units):
        db = DbAccess.DbAccess()
        query = self.__query_builder.build_insert_query(self.EXERCISE_TABLE, [
            (exercise_id, user_id, name, category, sets, reps, amount, units)])
        db.insert_data(query)
        db.close_connection()

    # Creates many new exercises
    # @param exercises - a list of lists where each inner list holds the data for an exercise
    def create_new_exercises(self, exercises):
        db = DbAccess.DbAccess()
        # TODO: generate ids in controller
        query = self.__query_builder.build_insert_query(self.EXERCISE_TABLE, exercises)
        db.insert_data(query)
        db.close_connection()

    # Creates many new exercises entries
    # @param exercise_entries - a list of lists where each inner list holds the data for an exercise entry
    def create_new_exercise_entries(self, exercise_entries):
        db = DbAccess.DbAccess()
        query = self.__query_builder.build_insert_query(self.EXERCISE_ENTRY_TABLE, exercise_entries)
        db.insert_data(query)
        db.close_connection()

    def update_exercise(self, exercise_id, data):
        db = DbAccess.DbAccess()
        query = self.__query_builder.build_update_query(self.EXERCISE_TABLE, data,
                                                        {"exercise_id": ["exercise_id", "=", exercise_id]})
        db.update_data(query)
        db.close_connection()

    def update_exercise_entry(self, exercise_entry_id, data):
        db = DbAccess.DbAccess()
        query = self.__query_builder.build_update_query(self.EXERCISE_ENTRY_TABLE, data,
                                                        {"exercise_entry_id":
                                                            ["exercise_entry_id", "=", exercise_entry_id]})
        db.update_data(query)
        db.close_connection()

    def delete_exercise(self, exercise_id):
        db = DbAccess.DbAccess()
        delete_exercise_query = self.__query_builder.build_delete_query(self.EXERCISE_TABLE,
                                                                        {"exercise_id":
                                                                            ["exercise_id", "=", exercise_id]})
        delete_exercise_entries_query = self.__query_builder.build_delete_query(self.EXERCISE_ENTRY_TABLE,
                                                                                {"exercise_id":
                                                                                    ["exercise_id", "=", exercise_id]})
        db.delete_data(delete_exercise_query)
        db.delete_data(delete_exercise_entries_query)
        db.close_connection()

    def delete_exercise_entry_by_id(self, exercise_entry_id):
        db = DbAccess.DbAccess()
        delete_exercise_entries_query = self.__query_builder.build_delete_query(self.EXERCISE_ENTRY_TABLE,
                                                                                {"exercise_entry_id":
                                                                                    [
                                                                                        "exercise_entry_id",
                                                                                        "=",
                                                                                        exercise_entry_id
                                                                                    ]
                                                                                })
        db.delete_data(delete_exercise_entries_query)
        db.close_connection()

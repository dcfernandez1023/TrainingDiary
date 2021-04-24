# Exercise model object. Contains methods for CRUD operations on user's exercise data. This class provides access
# to two tables in the database: Exercises and ExerciseEntries. The Exercises table contains users' user-defined
# exercises, and the ExerciseEntries table contains all instances of when an exercise was logged by a user into
# the application.

from db import QueryBuilder
from utilities import util


class Exercise:
    EXERCISE_SCHEMA = ("exercise_id", "user_id", "name", "category", "sets", "reps", "amount", "units")
    EXERCISE_ENTRY_SCHEMA = (
        "exercise_entry_id", "exercise_id", "user_id", "timestamp", "day", "month", "year", "notes")
    EXERCISE_TABLE = "Exercises"
    EXERCISE_ENTRY_TABLE = "ExerciseEntries"

    # Constructor - initializes a QueryBuilder object to build dynamic SQL queries
    # @param db - DbAccess object that instantiations of this class use to access the database
    def __init__(self, db):
        self.__query_builder = QueryBuilder.QueryBuilder()
        self.__db = db

    # Gets user's defined exercises by user_id
    # @param user_id - the unique identifier of the user whose info to grab
    def get_user_exercises(self, user_id):
        query = self.__query_builder.build_select_query([self.EXERCISE_TABLE], [],
                                                        {"user_id": ["user_id", "=", user_id]})
        data = self.__db.get_data(query)

        return util.to_jsons(self.EXERCISE_SCHEMA, data)

    # Gets an exercise by exercise_id
    # @param exercise_id - the unique identifier of the exercise
    def get_exercise_by_id(self, exercise_id):
        query = self.__query_builder.build_select_query([self.EXERCISE_TABLE], [],
                                                        {"exercise_id": ["exercise_id", "=", exercise_id]})
        data = self.__db.get_data(query)
        if len(data) > 1:
            raise Exception("DuplicateExerciseIds")
        if len(data) == 0:
            return None

        return util.to_json(self.EXERCISE_SCHEMA, data[0])

    # Gets exercise entries by the exercise_id they are associated with
    # @param exercise_id - the unique identifier of the exercise
    def get_exercise_entries_by_exercise_id(self, exercise_id):
        query = self.__query_builder.build_select_query([self.EXERCISE_ENTRY_TABLE], [],
                                                        {"exercise_id":
                                                             ["exercise_id", "=", exercise_id]})
        data = self.__db.get_data(query)

        return util.to_jsons(self.EXERCISE_ENTRY_SCHEMA, data)

    # Gets all user exercise entries by user_id
    # @param user_id - the user_id associated with the exercise entries to grab
    def get_user_exercise_entries(self, user_id):
        query = self.__query_builder.build_select_query([self.EXERCISE_ENTRY_TABLE], [],
                                                        {"user_id": ["user_id", "=", user_id]})
        data = self.__db.get_data(query)

        return util.to_jsons(self.EXERCISE_ENTRY_SCHEMA, data)

    # Gets user exercise entries by the year they were logged
    # @param user_id - the user who owns these exercise entries
    # @param year - the year of the exercise entries to get
    def get_user_exercise_entries_by_year(self, user_id, year):
        query = self.__query_builder.build_select_query([self.EXERCISE_ENTRY_TABLE], [],
                                                        {
                                                            "user_id": ["user_id", "=", user_id],
                                                            "year": ["year", "=", year]
                                                        })
        data = self.__db.get_data(query)

        return util.to_jsons(self.EXERCISE_ENTRY_SCHEMA, data)

    # Creates a new exercise
    # @params - the data necessary for a new exercise; follows EXERCISE_SCHEMA above
    def create_new_exercise(self, exercise_id, user_id, name, category, sets, reps, amount, units):
        query = self.__query_builder.build_insert_query(self.EXERCISE_TABLE, [
            (exercise_id, user_id, name, category, sets, reps, amount, units)])
        self.__db.insert_data(query)

    # Creates many new exercises
    # @param exercises - a list of lists where each inner list holds the data for an exercise
    def create_new_exercises(self, exercises):
        # TODO: generate ids in controller
        query = self.__query_builder.build_insert_query(self.EXERCISE_TABLE, exercises)
        self.__db.insert_data(query)

    # Creates many new exercises entries
    # @param exercise_entries - a list of lists where each inner list holds the data for an exercise entry
    def create_new_exercise_entries(self, exercise_entries):
        for entry in exercise_entries:
            exercise_id = entry[1]
            check_query = self.__query_builder.build_select_query(["Exercises"],
                                                                  [],
                                                                  {"exercise_id": ["exercise_id", "=", exercise_id]})
            res = self.__db.get_data(check_query)
            if len(res) == 0:
                raise Exception("ExerciseDoesNotExist: Cannot create new exercise entry for a non-existent exercise")
        query = self.__query_builder.build_insert_query(self.EXERCISE_ENTRY_TABLE, exercise_entries)
        self.__db.insert_data(query)

    # Updates an exercise by id
    # @param data - the data to update; must contain keys from EXERCISE_SCHEMA or it will throw an Exception
    def update_exercise(self, exercise_id, data):
        query = self.__query_builder.build_update_query(self.EXERCISE_TABLE, data,
                                                        {"exercise_id": ["exercise_id", "=", exercise_id]})
        self.__db.update_data(query)

    # Updates an exercise entry by exercise_entry_id
    # @param exercise_entry_id - the unique identifier of the exercise entry to update
    # @param data - the data to update; must contain keys from EXERCISE_ENTRY_SCHEMA or it will throw an Exception
    def update_exercise_entry(self, exercise_entry_id, data):
        query = self.__query_builder.build_update_query(self.EXERCISE_ENTRY_TABLE, data,
                                                        {"exercise_entry_id":
                                                             ["exercise_entry_id", "=", exercise_entry_id]})
        self.__db.update_data(query)

    # Deletes an exercise by exercise_id
    # @param exercise_id - the id of the exercise to delete
    def delete_exercise(self, exercise_id):
        delete_exercise_query = self.__query_builder.build_delete_query(self.EXERCISE_TABLE,
                                                                        {"exercise_id":
                                                                             ["exercise_id", "=", exercise_id]})
        delete_exercise_entries_query = self.__query_builder.build_delete_query(self.EXERCISE_ENTRY_TABLE,
                                                                                {"exercise_id":
                                                                                     ["exercise_id", "=", exercise_id]})
        self.__db.delete_data(delete_exercise_query)
        self.__db.delete_data(delete_exercise_entries_query)

    # Deletes an exercise entry by exercise_entry_id
    # @param exercise_entry_id - the id of the exercise entry to delete
    def delete_exercise_entry_by_id(self, exercise_entry_id):
        delete_exercise_entries_query = self.__query_builder.build_delete_query(self.EXERCISE_ENTRY_TABLE,
                                                                                {"exercise_entry_id":
                                                                                    [
                                                                                        "exercise_entry_id",
                                                                                        "=",
                                                                                        exercise_entry_id
                                                                                    ]
                                                                                })
        self.__db.delete_data(delete_exercise_entries_query)

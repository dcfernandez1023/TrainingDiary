# User model object. Contains methods for CRUD operations on user's data. This class gives access to the User table
# in the database.

from models import QueryBuilder, Body, Custom, Diet, Exercise
from utilities import util


class User:
    # Database schema and table associated with this model object
    USER_SCHEMA = ("user_id", "email", "name")
    USER_TABLE = "Users"

    # Constructor - initializes a QueryBuilder object to build dynamic SQL queries
    # @param db - DbAccess object that instantiations of this class use to access the database
    def __init__(self, db):
        self.__query_builder = QueryBuilder.QueryBuilder()
        self.__db = db

    # Gets user info from the database
    # @param user_id - the unique identifier of the user whose info to grab
    def get_user_info(self, user_id):
        query = self.__query_builder.build_select_query([self.USER_TABLE], [], {"user_id": ["user_id", "=", user_id]})
        data = self.__db.get_data(query)
        if len(data) > 1:
            raise Exception("DuplicateUserIds")
        if len(data) == 0:
            return None
        return util.to_json(self.USER_SCHEMA, data[0])

    # Creates a new user
    # @param user_id - unique identifier for this user, generated in the UserController class
    # @param email - user's email
    # @param name - user's name
    def create_new_user(self, user_id, email, name):
        query = self.__query_builder.build_insert_query(self.USER_TABLE, [(user_id, email, name)])
        self.__db.insert_data(query)

    # Updates user info
    # @param user_id - unique identifier for this user, generated in the UserController
    # @param data - dictionary of data to update (if keys don't match USER_SCHEMA, an exception will be thrown)
    def update_user_info(self, user_id, data):
        query = self.__query_builder.build_update_query(self.USER_TABLE, data, {"user_id": ["user_id", "=", user_id]})
        self.__db.update_data(query)

    # Deletes a user and all rows in other tables associated with this user
    # @param user_id - the unique identifier of the user to delete
    def delete_user(self, user_id):
        conditions = {"user_id": ["user_id", "=", user_id]}
        user_query = self.__query_builder.build_delete_query(self.USER_TABLE, conditions)
        body_fat_query = self.__query_builder.build_delete_query(Body.Body.BODY_FAT_TABLE, conditions)
        body_weight_query = self.__query_builder.build_delete_query(Body.Body.BODY_WEIGHT_TABLE, conditions)
        custom_type_query = self.__query_builder.build_delete_query(Custom.Custom.CUSTOM_TYPE_TABLE, conditions)
        custom_entry_query = self.__query_builder.build_delete_query(Custom.Custom.CUSTOM_ENTRY_TABLE, conditions)
        diet_entry_query = self.__query_builder.build_delete_query(Diet.Diet.DIET_TABLE, conditions)
        exercise_schema_query = self.__query_builder.build_delete_query(Exercise.Exercise.EXERCISE_TABLE, conditions)
        exercise_entry_query = self.__query_builder.build_delete_query(Exercise.Exercise.EXERCISE_ENTRY_TABLE, conditions)
        self.__db.delete_data(user_query)
        self.__db.delete_data(body_fat_query)
        self.__db.delete_data(body_weight_query)
        self.__db.delete_data(custom_type_query)
        self.__db.delete_data(custom_entry_query)
        self.__db.delete_data(diet_entry_query)
        self.__db.delete_data(exercise_schema_query)
        self.__db.delete_data(exercise_entry_query)

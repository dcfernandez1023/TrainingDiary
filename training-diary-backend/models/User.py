# User model object. Contains methods for CRUD operations on user's data

from models import DbAccess, QueryBuilder


class User:
    def __init__(self):
        self.__query_builder = QueryBuilder.QueryBuilder()

    def get_user_info(self, user_id):
        db = DbAccess.DbAccess()
        query = self.__query_builder.build_select_query(["Users"], [], {"user_id": ["user_id", "=", user_id]})
        data = db.get_data(query)
        db.close_connection()
        if len(data) > 1:
            raise Exception("DuplicateUserIds")
        if len(data) == 0:
            return None
        return data

    def create_new_user(self, user_id, email, name):
        db = DbAccess.DbAccess()
        query = self.__query_builder.build_insert_query("Users", [(user_id, email, name)])
        db.insert_data(query)
        db.close_connection()

    def update_user_info(self, user_id, data):
        db = DbAccess.DbAccess()
        query = self.__query_builder.build_update_query("Users", data, {"user_id": ["user_id", "=", user_id]})
        db.update_data(query)
        db.close_connection()

    def delete_user(self, user_id):
        db = DbAccess.DbAccess()
        query = self.__query_builder.build_delete_query("Users", {"user_id": ["user_id", "=", user_id]})
        db.delete_data(query)
        db.close_connection()


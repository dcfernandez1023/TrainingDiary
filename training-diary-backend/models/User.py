# User model object. Contains methods for CRUD operations on user's data

from models import DbAccess


class User:
    def __init__(self, path_to_db_files):
        self.__db = path_to_db_files

    def get_user_info(self, user_id):
        db = DbAccess.DbAccess(self.__db)
        query = "SELECT * " \
                "FROM Users " \
                "WHERE user_id = " + "'" + user_id + "'"
        data = db.get_data(query)
        db.close_connection()
        if len(data) > 1:
            raise Exception("DuplicateUserIds")
        return data

    def create_new_user(self, user_id, email, name):
        db = DbAccess.DbAccess(self.__db)
        query = "INSERT INTO " \
                "Users " \
                "VALUES" \
                "(" + "'" + user_id + "'," + "'" + email + "'," + "'" + name + "'" + ")"
        db.insert_data(query)
        db.close_connection()

    def update_user_info(self, user_id, data):
        db = DbAccess.DbAccess(self.__db)
        query = "UPDATE Users " \
                "SET "
        keys = list(data.keys())
        for i in range(len(keys)):
            key = keys[i]
            if i == len(keys) - 1:
                query += key + "=" + "'" + data[key] + "'"
            else:
                query += key + "=" + "'" + data[key] + "', "
        query += "WHERE user_id = " + "'" + user_id + "'"
        db.update_data(query)
        db.close_connection()

    def delete_user(self, user_id):
        db = DbAccess.DbAccess(self.__db)
        query = "DELETE FROM Users " \
                "WHERE user_id = " + "'" + user_id + "'"
        db.delete_data(query)
        db.close_connection()


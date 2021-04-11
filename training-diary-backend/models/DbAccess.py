# This object provides access to the database. Intended to be instantiated
# and used by the model objects for this application.

import sqlite3
import os


class DbAccess:
    def __init__(self, database):
        self.__connection = sqlite3.connect(database)

    def close_connection(self):
        self.__connection.close()

    def get_data(self, sql_script):
        cursor = self.__connection.cursor()
        cursor.executescript(sql_script)
        return cursor.fetchall()

    def insert_data(self, sql_script):
        cursor = self.__connection.cursor()
        cursor.executescript(sql_script)

    def update_data(self, sql_script):
        cursor = self.__connection.cursor()
        cursor.executescript(sql_script)

    def delete_data(self, sql_script):
        cursor = self.__connection.cursor()
        cursor.executescript(sql_script)

    # Static method for initializing multiple databases.
    # @param path_to_db_files - path to where the db files are located
    # @param db_init_queries - dictionary of db names and their initialization queries
    # @return None
    @staticmethod
    def init_dbs(path_to_db_files, db_init_queries):
        # drop databases if needed
        for db in db_init_queries:
            db_path = path_to_db_files + "/" + db
            if os.path.exists(db_path):
                os.remove(db_path)
            # execute initialization script
            cursor = sqlite3.connect(db_path).cursor()
            cursor.executescript(db_init_queries[db])

    # static method to build a simple SELECT query string
    # @param table - string representing the table(s) to select from
    # @param columns - list of column(s) to select from
    # @param conditions - nested list of conditions to apply
    @staticmethod
    def build_simple_select_query(table, columns, conditions):
        query = "SELECT "
        if len(columns) == 0:
            query += "* "
        for i in range(len(columns)):
            if i == len(columns) - 1:
                query += columns[i] + " "
            else:
                query += columns[i] + ", "
        query += "FROM " + table + " WHERE "
        for n in range(len(conditions)):
            if n == len(conditions) - 1:
                for condition in conditions[n]:
                    query += condition + " "
            else:
                for condition in conditions[n]:
                    query += condition + " "
                query += "AND "
        return query

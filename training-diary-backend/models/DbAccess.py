# This object provides access to the database. Intended to be instantiated
# and used by the model objects for this application.

import psycopg2
import os


class DbAccess:
    def __init__(self, database=os.getenv("TRAINING_DIARY_DB"), user=os.getenv("POSTGRES_USERNAME"),
                 password=os.getenv("POSTGRES_PASSWORD"),
                 host=os.getenv("POSTGRES_HOST"),
                 port=os.getenv("POSTGRES_PORT")):
        self.__connection = psycopg2.connect(
            database=database,
            user=user,
            password=password,
            host=host,
            port=port
        )

    def open_connection(self, database=os.getenv("TRAINING_DIARY_DB"), user=os.getenv("POSTGRES_USERNAME"),
                        password=os.getenv("POSTGRES_PASSWORD"),
                        host=os.getenv("POSTGRES_HOST"),
                        port=os.getenv("POSTGRES_PORT")):
        self.__connection = psycopg2.connect(
            database=database,
            user=user,
            password=password,
            host=host,
            port=port
        )

    def close_connection(self):
        self.__connection.close()
        self.__connection = None

    def get_data(self, query):
        if self.__connection is None:
            self.open_connection()
        cursor = self.__connection.cursor()
        cursor.execute(query)
        self.__connection.commit()
        data = cursor.fetchall()
        cursor.close()
        return data

    def insert_data(self, query):
        if self.__connection is None:
            self.open_connection()
        cursor = self.__connection.cursor()
        cursor.execute(query)
        self.__connection.commit()
        cursor.close()

    def update_data(self, query):
        if self.__connection is None:
            self.open_connection()
        cursor = self.__connection.cursor()
        cursor.execute(query)
        self.__connection.commit()
        cursor.close()

    def delete_data(self, query):
        if self.__connection is None:
            self.open_connection()
        cursor = self.__connection.cursor()
        cursor.execute(query)
        self.__connection.commit()
        cursor.close()

    def init_database(self, query):
        if self.__connection is None:
            self.open_connection()
        cursor = self.__connection.cursor()
        cursor.execute(query)
        self.__connection.commit()
        cursor.close()

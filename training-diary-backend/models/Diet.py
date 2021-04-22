# Diet model object. Contains methods for CRUD operations on user's diet data. This class gives access to the
# Diet table in the database.

from db import QueryBuilder
from utilities import util


class Diet:
    DIET_SCHEMA = ("user_id", "day", "month", "year", "calories", "protein", "carbs", "fat", "notes")
    DIET_TABLE = "Diet"

    def __init__(self, db):
        self.__query_builder = QueryBuilder.QueryBuilder()
        self.__db = db
        
    def get_user_diet_entry(self, user_id, day, month, year):
        query = self.__query_builder.build_select_query([self.DIET_TABLE], [], {
            "user_id": ["user_id", "=", user_id],
            "day": ["day", "=", day],
            "month": ["month", "=", month],
            "year": ["year", "=", year]
        })
        data = self.__db.get_data(query)
        if len(data) > 1:
            raise Exception("DuplicateDietIds")
        if len(data) == 0:
            return None
        return util.to_json(self.DIET_SCHEMA, data[0])

    def get_user_diet_entries(self, user_id):
        query = self.__query_builder.build_select_query([self.DIET_TABLE], [], {"user_id": ["user_id", "=", user_id]})
        data = self.__db.get_data(query)
        return util.to_jsons(self.DIET_SCHEMA, data)

    def create_new_diet_entry(self, user_id, day, month, year, calories, protein, carbs, fat, notes):
        query = self.__query_builder.build_insert_query(self.DIET_TABLE, [
            (user_id, day, month, year, calories, protein, carbs, fat, notes)])
        self.__db.insert_data(query)

    def update_diet_entry(self, user_id, day, month, year, data):
        query = self.__query_builder.build_update_query(self.DIET_TABLE, data, {
            "user_id": ["user_id", "=", user_id],
            "day": ["day", "=", day],
            "month": ["month", "=", month],
            "year": ["year", "=", year]
        })
        self.__db.update_data(query)

    def delete_diet_entry(self, user_id, day, month, year):
        query = self.__query_builder.build_delete_query(self.DIET_TABLE, {
            "user_id": ["user_id", "=", user_id],
            "day": ["day", "=", day],
            "month": ["month", "=", month],
            "year": ["year", "=", year]
        })
        self.__db.delete_data(query)
        


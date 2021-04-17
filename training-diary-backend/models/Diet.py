# Diet model object. Contains methods for CRUD operations on user's diet data

from models import DbAccess, QueryBuilder
from utilities import util


class Diet:
    DIET_SCHEMA = ("user_id", "day", "month", "year", "calories", "protein", "carbs", "fat", "notes")
    DIET_TABLE = "Diet"

    def __init__(self):
        self.__query_builder = QueryBuilder.QueryBuilder()

    def get_user_diet_entry(self, user_id, day, month, year):
        db = DbAccess.DbAccess()
        query = self.__query_builder.build_select_query([self.DIET_TABLE], [], {
            "user_id": ["user_id", "=", user_id],
            "day": ["day", "=", day],
            "month": ["month", "=", month],
            "year": ["year", "=", year]
        })
        data = db.get_data(query)
        db.close_connection()
        if len(data) > 1:
            raise Exception("DuplicateDietIds")
        if len(data) == 0:
            return None
        return util.to_json(self.DIET_SCHEMA, data[0])

    def get_user_diet_entries(self, user_id):
        db = DbAccess.DbAccess()
        query = self.__query_builder.build_select_query([self.DIET_TABLE], [], {"user_id": ["user_id", "=", user_id]})
        data = db.get_data(query)
        return util.to_jsons(self.DIET_SCHEMA, data)

    def create_new_diet_entry(self, user_id, day, month, year, calories, protein, carbs, fat, notes):
        db = DbAccess.DbAccess()
        query = self.__query_builder.build_insert_query(self.DIET_TABLE, [
            (user_id, day, month, year, calories, protein, carbs, fat, notes)])
        db.insert_data(query)
        db.close_connection()

    def update_diet_entry(self, user_id, day, month, year, data):
        db = DbAccess.DbAccess()
        query = self.__query_builder.build_update_query(self.DIET_TABLE, data, {
            "user_id": ["user_id", "=", user_id],
            "day": ["day", "=", day],
            "month": ["month", "=", month],
            "year": ["year", "=", year]
        })
        db.update_data(query)
        db.close_connection()

    def delete_diet_entry(self, user_id, day, month, year):
        db = DbAccess.DbAccess()
        query = self.__query_builder.build_delete_query(self.DIET_TABLE, {
            "user_id": ["user_id", "=", user_id],
            "day": ["day", "=", day],
            "month": ["month", "=", month],
            "year": ["year", "=", year]
        })
        db.delete_data(query)
        db.close_connection()


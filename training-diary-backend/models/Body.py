# Body model object. Contains methods for CRUD operations on user's body data

from models import DbAccess, QueryBuilder
from utilities import util


class Body:
    SCHEMA = ("body_id", "user_id", "timestamp", "day", "month", "year", "body_weight", "units", "body_fat")
    TABLE = "Body"

    def __init__(self):
        self.__query_builder = QueryBuilder.QueryBuilder()

    def get_user_body_entries(self, user_id):
        db = DbAccess.DbAccess()
        query = self.__query_builder.build_select_query([self.TABLE], [], {"user_id": ["user_id", "=", user_id]})
        data = db.get_data(query)
        db.close_connection()
        return util.to_jsons(self.SCHEMA, data)

    def get_body_entry_by_id(self, body_id):
        db = DbAccess.DbAccess()
        query = self.__query_builder.build_select_query([self.TABLE], [], {"body_id": ["body_id", "=", body_id]})
        data = db.get_data(query)
        if len(data) > 1:
            raise Exception("DuplicateBodyIds")
        if len(data) == 0:
            return None
        db.close_connection()
        return util.to_json(self.SCHEMA, data[0])

    def create_new_body_entry(self, body_id, user_id, timestamp, day, month, year, body_weight, units, body_fat):
        db = DbAccess.DbAccess()
        query = self.__query_builder.build_insert_query(self.TABLE, [
            (body_id, user_id, timestamp, day, month, year, body_weight, units, body_fat)])
        db.insert_data(query)
        db.close_connection()

    def update_body_entry(self, body_id, data):
        db = DbAccess.DbAccess()
        query = self.__query_builder.build_update_query(self.TABLE, data, {"body_id": ["body_id", "=", body_id]})
        db.update_data(query)
        db.close_connection()

    def delete_body_entry(self, body_id):
        db = DbAccess.DbAccess()
        query = self.__query_builder.build_delete_query(self.TABLE, {"body_id": ["body_id", "=", body_id]})
        db.delete_data(query)
        db.close_connection()

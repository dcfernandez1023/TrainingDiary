# Activity model object. Contains methods for CRUD operations on user's activity data

from models import DbAccess, QueryBuilder
from utilities import util


class Activity:
    SCHEMA = ("activity_id", "user_id", "exercise_id", "timestamp", "day", "month", "year", "notes")
    TABLE = "Activities"

    def __init__(self):
        self.__query_builder = QueryBuilder.QueryBuilder()

    def get_user_activities(self, user_id):
        db = DbAccess.DbAccess()
        query = self.__query_builder.build_select_query([self.TABLE], [], {"user_id": ["user_id", "=", user_id]})
        data = db.get_data(query)
        db.close_connection()
        return util.to_jsons(self.SCHEMA, data)

    def get_activities_by_date(self, user_id, day, month, year):
        db = DbAccess.DbAccess()
        query = self.__query_builder.build_select_query(
            [self.TABLE],
            [],
            {"day": ["day", "=", day], "month": ["month", "=", month], "year": ["year", "=", year],
             "user_id": ["user_id", "=", user_id]}
        )
        data = db.get_data(query)
        db.close_connection()
        return util.to_jsons(self.SCHEMA, data)

    def get_activities_by_year(self, user_id, year):
        db = DbAccess.DbAccess()
        query = self.__query_builder.build_select_query([self.TABLE], [], {"year": ["year", "=", year],
                                                                           "user_id": ["user_id", "=", user_id]})
        data = db.get_data(query)
        db.close_connection()
        return util.to_jsons(self.SCHEMA, data)

    def get_activity_by_id(self, activity_id):
        db = DbAccess.DbAccess()
        query = self.__query_builder.build_select_query([self.TABLE], [],
                                                        {"activity_id": ["activity_id", "=", activity_id]})
        data = db.get_data(query)
        db.close_connection()
        if len(data) > 1:
            raise Exception("DuplicateActivityIds")
        if len(data) == 0:
            return None
        return util.to_json(self.SCHEMA, data[0])

    def create_new_activity(self, activity_id, user_id, exercise_id, time, day, month, year, notes):
        db = DbAccess.DbAccess()
        query = self.__query_builder.build_insert_query(self.TABLE, [
            (activity_id, user_id, exercise_id, time, day, month, year, notes)])
        db.insert_data(query)
        db.close_connection()

    def update_activity(self, activity_id, data):
        db = DbAccess.DbAccess()
        update_conditions = {"activity_id": ["activity_id", "=", activity_id]}
        query = self.__query_builder.build_update_query(self.TABLE, data, update_conditions)
        db.update_data(query)
        db.close_connection()

    def delete_activity(self, activity_id):
        db = DbAccess.DbAccess()
        delete_conditions = {"activity_id": ["activity_id", "=", activity_id]}
        query = self.__query_builder.build_delete_query(self.TABLE, delete_conditions)
        db.delete_data(query)
        db.close_connection()



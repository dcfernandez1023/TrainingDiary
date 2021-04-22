# Body model object. Contains methods for CRUD operations on user's body data

from db import QueryBuilder
from utilities import util


class Body:
    BODY_WEIGHT_SCHEMA = ("bw_id", "user_id", "weight", "units", "timestamp", "day", "month", "year", "notes")
    BODY_FAT_SCHEMA = ("bf_id", "user_id", "percentage", "timestamp", "day", "month", "year", "notes")
    BODY_WEIGHT_TABLE = "BodyWeight"
    BODY_FAT_TABLE = "BodyFat"

    def __init__(self, db):
        self.__query_builder = QueryBuilder.QueryBuilder()
        self.__db = db

    def get_user_body_entries(self, user_id):
        bw_query = self.__query_builder.build_select_query([self.BODY_WEIGHT_TABLE], [], {"user_id":
                                                                                              ["user_id", "=",
                                                                                               user_id]})
        bf_query = self.__query_builder.build_select_query([self.BODY_FAT_TABLE], [], {"user_id":
                                                                                           ["user_id", "=", user_id]})
        bw_data = util.to_jsons(self.BODY_WEIGHT_SCHEMA, self.__db.get_data(bw_query))
        bf_data = util.to_jsons(self.BODY_FAT_SCHEMA, self.__db.get_data(bf_query))
        return {"body_weight_entries": bw_data, "body_fat_entries": bf_data}

    def get_body_weight_entry_by_id(self, bw_id):
        query = self.__query_builder.build_select_query([self.BODY_WEIGHT_TABLE], [], {"bw_id": ["bw_id", "=", bw_id]})
        data = self.__db.get_data(query)
        if len(data) > 1:
            raise Exception("DuplicateBodyWeightIds")
        if len(data) == 0:
            return None
        return util.to_json(self.BODY_WEIGHT_SCHEMA, data[0])

    def get_body_fat_entry_by_id(self, bf_id):
        query = self.__query_builder.build_select_query([self.BODY_FAT_TABLE], [], {"bf_id": ["bf_id", "=", bf_id]})
        data = self.__db.get_data(query)
        if len(data) > 1:
            raise Exception("DuplicateBodyFatIds")
        if len(data) == 0:
            return None
        return util.to_json(self.BODY_FAT_SCHEMA, data[0])

    def create_new_body_weight_entry(self, bw_id, user_id, weight, units, timestamp, day, month, year, notes):
        query = self.__query_builder.build_insert_query(self.BODY_WEIGHT_TABLE, [
            (bw_id, user_id, weight, units, timestamp, day, month, year, notes)])
        self.__db.insert_data(query)

    def create_new_body_fat_entry(self, bf_id, user_id, percentage, timestamp, day, month, year, notes):
        query = self.__query_builder.build_insert_query(self.BODY_FAT_TABLE, [
            (bf_id, user_id, percentage, timestamp, day, month, year, notes)])
        self.__db.insert_data(query)

    def update_body_weight_entry(self, bw_id, data):
        query = self.__query_builder.build_update_query(self.BODY_WEIGHT_TABLE, data, {"bw_id": ["bw_id", "=", bw_id]})
        self.__db.update_data(query)

    def update_body_fat_entry(self, bf_id, data):
        query = self.__query_builder.build_update_query(self.BODY_FAT_TABLE, data, {"bf_id": ["bf_id", "=", bf_id]})
        self.__db.update_data(query)

    def delete_body_weight_entry(self, bw_id):
        query = self.__query_builder.build_delete_query(self.BODY_WEIGHT_TABLE, {"bw_id": ["bw_id", "=", bw_id]})
        self.__db.delete_data(query)

    def delete_body_fat_entry(self, bf_id):
        query = self.__query_builder.build_delete_query(self.BODY_FAT_TABLE, {"bf_id": ["bf_id", "=", bf_id]})
        self.__db.delete_data(query)

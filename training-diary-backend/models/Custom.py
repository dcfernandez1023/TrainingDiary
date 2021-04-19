# Custom model object. Contains methods for CRUD operations on user-defined custom fitness data

from models import DbAccess, QueryBuilder
from utilities import util
import json


class Custom:
    CUSTOM_TYPE_SCHEMA = ("custom_id", "user_id", "custom_schema")
    CUSTOM_ENTRY_SCHEMA = (
    "custom_entry_id", "custom_id", "user_id", "custom_entry", "timestamp", "day", "month", "year", "notes")
    CUSTOM_TYPE_TABLE = "CustomTypes"
    CUSTOM_ENTRY_TABLE = "CustomEntries"

    def __init__(self):
        self.__query_builder = QueryBuilder.QueryBuilder()

    def get_user_custom_types(self, user_id):
        db = DbAccess.DbAccess()
        query = self.__query_builder.build_select_query([self.CUSTOM_TYPE_TABLE],
                                                        [], {"user_id": ["user_id", "=", user_id]})
        data = db.get_data(query)
        db.close_connection()
        return util.to_jsons(self.CUSTOM_TYPE_SCHEMA, data)

    def get_user_custom_entries(self, user_id):
        db = DbAccess.DbAccess()
        query = self.__query_builder.build_select_query([self.CUSTOM_ENTRY_TABLE],
                                                        [], {"user_id": ["user_id", "=", user_id]})
        data = db.get_data(query)
        db.close_connection()
        return util.to_jsons(self.CUSTOM_ENTRY_SCHEMA, data)

    def get_custom_type_by_id(self, custom_id):
        db = DbAccess.DbAccess()
        query = self.__query_builder.build_select_query([self.CUSTOM_ENTRY_TABLE],
                                                        [], {"custom_id": ["custom_id", "=", custom_id]})
        data = db.get_data(query)
        if len(data) > 1:
            raise Exception("DuplicateCustomTypeIds")
        if len(data) == 0:
            return None
        db.close_connection()
        return util.to_json(self.CUSTOM_TYPE_SCHEMA, data[0])

    def get_user_custom_entries_by_custom_id(self, custom_id):
        db = DbAccess.DbAccess()
        query = self.__query_builder.build_select_query([self.CUSTOM_ENTRY_TABLE],
                                                        [], {"custom_id": ["custom_id", "=", custom_id]})
        data = db.get_data(query)
        db.close_connection()
        return util.to_jsons(self.CUSTOM_ENTRY_SCHEMA, data)

    def get_custom_entry_by_id(self, custom_entry_id):
        db = DbAccess.DbAccess()
        query = self.__query_builder.build_select_query([self.CUSTOM_ENTRY_TABLE],
                                                        [],
                                                        {"custom_entry_id": ["custom_entry_id", "=", custom_entry_id]})
        data = db.get_data(query)
        if len(data) > 1:
            raise Exception("DuplicateCustomEntryIds")
        if len(data) == 0:
            return None
        db.close_connection()
        return util.to_json(self.CUSTOM_ENTRY_SCHEMA, data[0])

    def create_new_custom_type(self, custom_id, user_id, custom_schema):
        db = DbAccess.DbAccess()
        custom_schema = json.dumps(custom_schema)
        query = self.__query_builder.build_insert_query(self.CUSTOM_TYPE_TABLE,
                                                        [(custom_id, user_id, custom_schema)])
        db.insert_data(query)
        db.close_connection()

    def create_new_custom_entry(self, custom_entry_id, custom_id, user_id, custom_entry, timestamp, day, month, year,
                                notes):
        db = DbAccess.DbAccess()
        if self.__validate_entry_schema(db, custom_id, custom_entry):
            custom_entry = json.dumps(custom_entry)
            query = self.__query_builder.build_insert_query(self.CUSTOM_ENTRY_TABLE,
                                                            [(custom_entry_id, custom_id, user_id, custom_entry,
                                                              timestamp,
                                                              day, month, year, notes)])
            db.insert_data(query)
        db.close_connection()

    def update_custom_type(self, custom_id, data):
        db = DbAccess.DbAccess()
        if "custom_schema" in data:
            custom_type = json.dumps(data.get("custom_schema")).replace("'", '"')
            print("PARSED: " + custom_type)
            data.update({"custom_schema": custom_type})
        query = self.__query_builder.build_update_query(self.CUSTOM_TYPE_TABLE, data,
                                                        {"custom_id": ["custom_id", "=", custom_id]})
        print(query)
        db.update_data(query)
        db.close_connection()

    def update_custom_entry(self, custom_entry_id, custom_id, data):
        db = DbAccess.DbAccess()
        if "custom_entry" in data:
            custom_entry = data.get("custom_entry")
            if self.__validate_entry_schema(db, custom_id, custom_entry):
                data.update({"custom_entry": json.dumps(data.get("custom_entry")).replace("'", '"')})
                query = self.__query_builder.build_update_query(self.CUSTOM_ENTRY_TABLE, data,
                                                                {"custom_entry_id": ["custom_entry_id", "=",
                                                                                     custom_entry_id]})
                db.update_data(query)
        db.close_connection()

    def delete_custom_type(self, custom_id):
        db = DbAccess.DbAccess()
        delete_custom_entries_query = self.__query_builder.build_delete_query(self.CUSTOM_ENTRY_TABLE, {
            "custom_id": ["custom_id", "=", custom_id]
        })
        delete_custom_type_query = self.__query_builder.build_delete_query(self.CUSTOM_TYPE_TABLE,
                                                                           {"custom_id": ["custom_id", "=", custom_id]})
        db.delete_data(delete_custom_type_query)
        db.delete_data(delete_custom_entries_query)
        db.close_connection()

    def delete_custom_entry(self, custom_entry_id):
        db = DbAccess.DbAccess()
        query = self.__query_builder.build_delete_query(self.CUSTOM_ENTRY_TABLE,
                                                        {"custom_entry_id": ["custom_entry_id", "=", custom_entry_id]})
        db.delete_data(query)
        db.close_connection()

    def __validate_entry_schema(self, db, custom_id, custom_entry):
        get_custom_type_query = self.__query_builder.build_select_query([self.CUSTOM_TYPE_TABLE], ["custom_schema"],
                                                                        {"custom_id": ["custom_id", "=", custom_id]})
        data = db.get_data(get_custom_type_query)
        if len(data) > 1:
            db.close_connection()
            raise Exception("DuplicateCustomTypeIds")
        if len(data) == 0:
            db.close_connection()
            raise Exception("NoCustomSchemaExists")
        custom_schema = json.loads(json.dumps(data[0][0]))
        print(str(custom_schema))
        print(str(custom_entry))
        if custom_schema.keys() != custom_entry.keys():
            db.close_connection()
            raise Exception("CustomSchemaDoesNotMatch")
        return True

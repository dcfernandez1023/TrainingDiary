# This object provides access to the database. Intended to be instantiated
# and used by the model objects for this application.

import sqlite3


class DbAccess:
    def __init__(self, database):
        self.__connection = sqlite3.connect(database)

    # DATABASE RETRIEVAL METHODS #

    # Gets and returns the first entity resulting from the query
    # Only for simple SELECT FROM WHERE queries
    # @param table - the table to query from
    # @param columns - list of columns of the table to select from
        # example: ["id", "name", "age"]
    # @param filters - dict of filters for the query, where each value
    #                  in the dict is an array of 3 values representing
    #                  the filter
        # example: { "age": ["age", "<", "60"],  "name": ["name", "=", "John"] }
    # @return dict - keys = columns, values = result values of query
    def get_one(self, table, columns, filters):
        query_string = self.__build_query_string(table, columns, filters)
        return query_string
    # helper function to build simple, dynamic query strings
    # @param table - the table to query from
    # @param columns - list of columns of the table to select from
    # @param filters - dict of filters for the query, where each value
    #                  in the dict is an array of 3 values representing
    #                  the filter
    # @return string - the constructed SQL query string
    def __build_query_string(self, table, columns, filters):
        query_string = "SELECT"
        # construct SELECT portion of the query
        curr_col = 0
        for col in columns:
            if curr_col == len(columns) - 1:
                query_string += " " + col + " "
            else:
                query_string += " " + col + ","
            curr_col += 1
        # construct FROM portion of the query
        query_string += "FROM " + table + " "
        # construct WHERE portion of the query
        curr_filter = 0
        for key in filters:
            if curr_filter == len(filters) - 1:
                query_string += filters[key][0] + " "
                query_string += filters[key][1] + " "
                query_string += filters[key][2]
            else:
                query_string += filters[key][0] + " "
                query_string += filters[key][1] + " "
                query_string += filters[key][2] + " AND "
        return query_string

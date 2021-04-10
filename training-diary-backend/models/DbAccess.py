# This object provides access to the database. Intended to be instantiated
# and used by the model objects for this application.

import sqlite3


class DbAccess:
    def __init__(self, database):
        self.__connection = sqlite3.connect(database)

    ## DATABASE RETRIEVAL METHODS ##
    # Gets and returns the first entity resulting from the query
    # @param table - the table to query from
    # @param columns - the columns of the table to select from
    # @param filters - constraints for the query
    # @return dict - keys = columns, values = result values of query
    def get_one(self, table, columns, filters):


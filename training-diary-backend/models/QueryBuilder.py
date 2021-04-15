# Helper class to build simple and dynamic SQL queries.


class QueryBuilder:
    # builds a simple SELECT FROM WHERE query
    # @param tables - list of tables to select from
    # @param columns - list of columns to select from
    # @param conditions - dictionary of conditions to apply in the WHERE clause
    # @return - the constructed query
    def build_select_query(self, tables, columns, conditions):
        # build select clause
        col_len = len(columns)
        table_len = len(tables)
        condition_keys = list(conditions.keys())
        if table_len == 0:
            raise Exception("InvalidFromClause")
        if col_len == 0:
            query = "SELECT * "
        else:
            query = "SELECT "
        for i in range(col_len):
            if i == col_len - 1:
                query += columns[i] + " "
            else:
                query += columns[i] + ", "
        # build from clause
        query += "FROM "
        for i in range(table_len):
            if i == table_len - 1:
                query += tables[i] + " "
            else:
                query += tables[i] + ", "
        # build where clause
        query += self.__construct_where_clause(conditions)
        return query

    # builds a simple insert query; does not support inserting into specific columns; must
    # provide data for all columns of the table's schema
    # @param table - the table to insert into
    # @param values - list of tuples representing the data to insert; tuples must match
    #                 the schema of the table
    # @return - the constructed query
    def build_insert_query(self, table, values):
        # build INSERT INTO clause
        query = "INSERT INTO " + table + " VALUES "
        for i in range(len(values)):
            tup = values[i]
            query += "("
            for n in range(len(tup)):
                ele = str(tup[n])
                if n == len(tup) - 1:
                    if ele.isdigit():
                        query += ele
                    else:
                        query += self.__wrap_in_single_quotes(ele)
                else:
                    if ele.isdigit():
                        query += ele + ","
                    else:
                        query += self.__wrap_in_single_quotes(ele) + ","
            if i == len(values) - 1:
                query += ")"
            else:
                query += "), "
        return query

    def build_update_query(self, table, cols_and_values, conditions):
        # build UPDATE clause
        query = "UPDATE " + table + " "
        # build SET clause
        query += "SET "
        cols = list(cols_and_values.keys())
        cols_len = len(cols)
        for i in range(cols_len):
            col = str(cols[i])
            value = str(cols_and_values[col])
            if value.isdigit():
                if i == cols_len - 1:
                    query += col + " = " + value + " "
                else:
                    query += col + " = " + value + ", "
            else:
                if i == cols_len - 1:
                    query += col + " = " + self.__wrap_in_single_quotes(value) + " "
                else:
                    query += col + " = " + self.__wrap_in_single_quotes(value) + ", "
        # build WHERE clause
        query += self.__construct_where_clause(conditions)
        return query

    def build_delete_query(self, table, conditions):
        # build DELETE clause
        query = "DELETE FROM " + table + " "
        query += self.__construct_where_clause(conditions)
        return query

    def __construct_where_clause(self, conditions):
        condition_keys = list(conditions.keys())
        conditions_len = len(condition_keys)
        query = "WHERE "
        for i in range(conditions_len):
            key = condition_keys[i]
            condition = conditions[key]
            c0 = str(condition[0])
            c1 = str(condition[1])
            c2 = str(condition[2])
            if len(condition) != 3:
                raise Exception("InvalidWhereClause: " + self.__wrap_in_single_quotes(str(condition)) +  " Needs 2 operands and 1 operator " )
            if i == conditions_len - 1:
                if c0.isdigit():
                    query += c0 + " " + c1 + " "
                else:
                    query += c0 + " " + c1 + " "
                if c2.isdigit():
                    query += c2
                else:
                    query += self.__wrap_in_single_quotes(c2)
            else:
                if c0.isdigit():
                    query += c0 + " " + c1 + " "
                else:
                    query += c0 + " " + c1 + " "
                if c2.isdigit():
                    query += c2
                else:
                    query += self.__wrap_in_single_quotes(c2)
                query += " AND "
        return query

    def __wrap_in_single_quotes(self, string):
        return "'" + string + "'"


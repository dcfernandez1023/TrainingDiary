# returns a dictionary of dictionaries given a list of tuples or lists
# assumes tups[i][0] is the key for the nested dictionary
# @param tups - list of tuples/lists to convert into a nested dictionary
# @param schema - a dictionary or list/tuple representing the schema that each tuple in tups should adhere to
def tups_to_dict(tups, schema):
    res_dict = {}
    for tup in tups:
        if isinstance(schema, dict):
            schema_keys = list(schema)
        else:
            schema_keys = schema
        # lengths must match, otherwise the schema of the data provided in tups may be invalid
        if len(tup) != len(schema_keys):
            return {}
        # this is assuming that the primary key/id is sitting at index 0 of the tuple (must be unique as well)
        key = tup[0]
        inner_dict = {}
        i = 0
        while i < len(tup):
            inner_dict.update({schema_keys[i]: tup[i]})
            i += 1
        res_dict.update({key: inner_dict})
    return res_dict


# converts a tuple from the database in to a json/dictionary representation
# the keys of the json/dictionary are from schema, and values are from the tuple
# @param schema - provides keys for the json/dictionary
# @param tuple - provides values for the json/dictionary
def to_json(schema, tuple):
    res = {}
    if len(schema) != len(tuple):
        return res
    for i in range(len(schema)):
        key = schema[i]
        value = tuple[i]
        res.update({key: value})
    return res


# Given a schema and a tuple of tuples/lists, this will convert each tuple into a dict/json representation
# @param schema - provides keys for the json/dictionary
# @param tuple - provides values for the json/dictionary
def to_jsons(schema, tuples):
    res = []
    for i in range(len(tuples)):
        if len(schema) != len(tuples[i]):
            return []
        res.append(to_json(schema, tuples[i]))
    return res

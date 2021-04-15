# Activity model object. Contains methods for CRUD operations on user's activity data

import time
from models import DbAccess, QueryBuilder
from utilities import util


class Activity:
    def __init__(self):
        self.__query_builder = QueryBuilder.QueryBuilder()


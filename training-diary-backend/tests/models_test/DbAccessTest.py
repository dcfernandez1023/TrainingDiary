# Simple unit tests for DbAccess class

import os
from tests import TestAssertion
from models import DbAccess

test = TestAssertion.TestAssertion()

# Test 1: instantiation
try:
    db = DbAccess.DbAccess("../../db/data/training_diary_db")
    db.close_connection()
    test.assert_test_success("Instantiation")
except Exception:
    test.assert_test_failure("Instantiation")

# Test 2: init dbs
try:
    file = open("../../db/queries/init_training_diary_db.sql", "r")
    db_inits = {"training_diary_db": file.read()}
    DbAccess.DbAccess.init_dbs("../../db/data", db_inits)
    file.close()
    test.assert_test_success("Initialize Database")
except Exception:
    test.assert_test_failure("Initialize Database")


test.assert_final_results()

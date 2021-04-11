# Simple unit tests for DbAccess class

import traceback
from tests import TestAssertion
from models import DbAccess

test = TestAssertion.TestAssertion()

# Test 1: instantiation
try:
    db = DbAccess.DbAccess("test_db")
    test.assert_test_success()
except Exception:
    tb = traceback.format_exc()
    test.assert_test_failure(tb)

# Test 2:
try:
    db = DbAccess.DbAccess("test_db")
    expected = "SELECT name, age FROM users WHERE user = 'Dom' AND age < 60"
    actual = db.get_one("users", ["name", "age"], {"name"})
    test.assert_test_success()
except Exception:
    tb = traceback.format_exc()
    test.assert_test_failure(tb)

test.assert_final_results()

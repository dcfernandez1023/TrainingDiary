# Simple unit tests for Diet class

from tests import TestAssertion
from models import Diet
from db import DbAccess

db = DbAccess.DbAccess()
test = TestAssertion.TestAssertion()
test.print_test_name("Diet Object Tests")

# Test 1: instantiation
try:
    diet = Diet.Diet(db)
    test.assert_test_success("Instantiation")
except Exception:
    test.assert_test_failure("Instantiation")

# Test 2: get diet info
try:
    diet = Diet.Diet(db)
    info = diet.get_user_diet_entry("u001", 16, 4, 2021)
    if info is None:
        raise Exception("No Diet Data Returned")
    print(str(info))
    test.assert_test_success("Get Diet Entry")
except Exception:
    test.assert_test_failure("Get Diet Entry")

# Test 3: get user diet entries
try:
    diet = Diet.Diet(db)
    info = diet.get_user_diet_entries("u001")
    print(str(info))
    test.assert_test_success("Get Diet Entries")
except Exception:
    test.assert_test_failure("Get Diet Entries")

# Test 4: create new diet entry
try:
    diet = Diet.Diet(db)
    diet.create_new_diet_entry('u001', 13, 4, 2021, 2700, 180, 230, 82, 'NEW DIET ENTRY')
    new_diet = diet.get_user_diet_entry("u001", 13, 4, 2021)
    if new_diet is None:
        raise Exception("Create User Failed")
    print("New Diet: " + str(new_diet))
    test.assert_test_success("Create New Diet Entry")
except Exception:
    test.assert_test_failure("Create New Diet Entry")

# Test 5: update diet entry
try:
    diet = Diet.Diet(db)
    new_data = {"notes": "UPDATE DIET ENTRY", "calories": 3000, "protein": 220, "carbs": 300, "fat": 90}
    diet.update_diet_entry('u001', 13, 4, 2021, new_data)
    print("Update: " + str(diet.get_user_diet_entry("u001", 13, 4, 2021)))
    test.assert_test_success("Update Diet Entry")
except Exception:
    test.assert_test_failure("Update Diet Entry")

# Test 6: delete diet entry
try:
    diet = Diet.Diet(db)
    diet.delete_diet_entry('u001', 13, 4, 2021)
    test.assert_test_success("Delete Diet Entry")
except Exception:
    test.assert_test_failure("Delete Entry")

test.assert_final_results()
db.close_connection()

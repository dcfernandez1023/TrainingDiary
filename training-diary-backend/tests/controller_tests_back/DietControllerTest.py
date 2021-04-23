# Simple unit tests for DietController class

from tests import TestAssertion
from controllers import DietController
from flask import app, Flask


test = TestAssertion.TestAssertion()
test.print_test_name("Diet Controller Tests")

diet_controller = DietController.DietController()
test_app = Flask("__main__")
app_context = app.AppContext(test_app)

# Test 1: Get Entry
with app_context:
    res = diet_controller.get_entry('u001', 16, 4, 2021)
    try:
        status = res.status_code
        data = res.get_json()
        if status != 200:
            raise Exception("BadResponse")
        print(data)
        test.assert_test_success("Get Entry")
    except Exception:
        test.assert_test_failure("Get Entry")

# Test 2: Get entries
with app_context:
    res = diet_controller.get_entries('u001')
    try:
        status = res.status_code
        data = res.get_json()
        if status != 200:
            raise Exception("BadResponse")
        print(data)
        test.assert_test_success("Get Entry")
    except Exception:
        test.assert_test_failure("Get Entry")

# Test 3: Create entry
with app_context:
    data = {
        "user_id": "u001",
        "day": 22,
        "month": 4,
        "year": 2021,
        "calories": 2300,
        "protein": 175,
        "carbs": 220,
        "fat": 79,
        "notes": "testing creating a new entry"
    }
    res = diet_controller.create_entry(data)
    print("Created entry: " + str(data))
    try:
        status = res.status_code
        print(status)
        if status != 200:
            raise Exception("BadResponse")
        test.assert_test_success("Create Entry")
    except Exception:
        test.assert_test_failure("Create Entry")

# Test 4: Update entry
with app_context:
    data = {
        "user_id": "u001",
        "day": 22,
        "month": 4,
        "year": 2021,
        "calories": 3000,
        "notes": "updating notes section"
    }
    res = diet_controller.update_entry(data)
    updated = diet_controller.get_entry("u001", 22, 4, 2021)
    print("Updated Entry: " + str(updated.get_json()))
    try:
        status = res.status_code
        print(status)
        if status != 200:
            raise Exception("BadResponse")
        test.assert_test_success("Update Entry")
    except Exception:
        test.assert_test_failure("Update Entry")

# Test 5: Delete entry
with app_context:
    res = diet_controller.delete_entry("u001", 22, 4, 2021)
    try:
        status = res.status_code
        print(status)
        if status != 200:
            raise Exception("BadResponse")
        test.assert_test_success("Delete Entry")
    except Exception:
        test.assert_test_failure("Delete Entry")


test.assert_final_results()

# Simple unit tests for CustomController class

from tests import TestAssertion
from controllers import CustomController
from flask import app, Flask


test = TestAssertion.TestAssertion()
test.print_test_name("User Controller Tests")

custom_controller = CustomController.CustomController()
test_app = Flask("__main__")
app_context = app.AppContext(test_app)

# Test 1: Get types and entries
with app_context:
    types = custom_controller.get_types("u001")
    entries = custom_controller.get_entries("u001")
    try:
        type_status = types.status_code
        entry_status = entries.status_code
        type_data = types.get_json()
        entry_data = entries.get_json()
        print(type_data)
        print(entry_data)
        if type_status != 200 or entry_status != 200:
            raise Exception("BadResponse")
        test.assert_test_success("Get Types and Entries")
    except Exception:
        test.assert_test_failure("Get Types and Entries")

# Test 2: Create Type and Entry
with app_context:
    try:
        type_data = {"user_id": "u001", "custom_schema": {"test": "", "name": "Test"}}
        type_res = custom_controller.create_type(type_data)
        custom_id = type_res.get_json().get("custom_id")
        entry_data = {
            "custom_id": custom_id,
            "user_id": "u001",
            "custom_entry": {"test": "yooo", "name": "Test"},
            "timestamp": 1619129330584,
            "day": 22,
            "month": 4,
            "year": 2021,
            "notes": "AYOOO"
        }
        entry_res = custom_controller.create_entry(entry_data)
        if entry_res.status_code != 200 or type_res.status_code != 200:
            raise Exception("BadResponse")
        test.assert_test_success("Create Type and Entry")
    except Exception:
        test.assert_test_failure("Create Type and Entry")

# Test 3: Update Type and Entry


test.assert_final_results()

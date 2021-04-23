# Simple unit tests for UserController class

from tests import TestAssertion
from controllers import UserController
from flask import app, Flask


test = TestAssertion.TestAssertion()
test.print_test_name("User Controller Tests")

user_controller = UserController.UserController()
test_app = Flask("__main__")
app_context = app.AppContext(test_app)

# Test 1: Get user info
with app_context:
    res = user_controller.get("u001")
    try:
        status = res.status_code
        data = res.get_json()
        if status != 200:
            raise Exception("BadResponse")
        print(data)
        test.assert_test_success("Get User")
    except Exception:
        test.assert_test_failure("Get User")

# Test 2: Create user
with app_context:
    data = {"user_id": "u020", "email": "dom22c@gmail.com", "name": "Big Dom"}
    res = user_controller.create(data)
    try:
        status = res.status_code
        if status != 200:
            raise Exception("BadResponse")
        print("New User: " + str(data))
        test.assert_test_success("Create User")
    except Exception:
        test.assert_test_failure("Create User")

# Test 3: Update user
with app_context:
    data = {"user_id": "u020", "name": "YOOOO"}
    res = user_controller.update(data)
    try:
        status = res.status_code
        print(status)
        if status != 200:
            raise Exception("BadResponse")
        print("Updated User: " + str(user_controller.get("u020").get_json()))
        test.assert_test_success("Update User")
    except Exception:
        test.assert_test_failure("Update User")

# Test 4: Delete user
with app_context:
    res = user_controller.delete("u020")
    try:
        status = res.status_code
        if status != 200:
            raise Exception("BadResponse")
        test.assert_test_success("Delete User")
    except Exception:
        test.assert_test_failure("Delete User")


test.assert_final_results()

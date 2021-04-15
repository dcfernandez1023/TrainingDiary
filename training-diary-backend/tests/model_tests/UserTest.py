# Simple unit tests for User class

from tests import TestAssertion
from models import User

test = TestAssertion.TestAssertion()
test.print_test_name("User Object Tests")

# Test 1: instantiation
try:
    user = User.User()
    test.assert_test_success("Instantiation")
except Exception:
    test.assert_test_failure("Instantiation")

# Test 2: get user info
try:
    user = User.User()
    info = user.get_user_info("u001")
    if info is None:
        raise Exception("No User Data Returned")
    print(str(info))
    test.assert_test_success("Get User Info")
except Exception:
    test.assert_test_failure("Get User Info")

# Test 3: create new user
try:
    user = User.User()
    user.create_new_user("u008", "test@mail.com", "test_name")
    if len(user.get_user_info("u008")) == 0:
        raise Exception("Create User Failed")
    test.assert_test_success("Create New User")
except Exception:
    test.assert_test_failure("Create New User")

# Test 4: update user
try:
    user = User.User()
    new_data = {"email": "dom22c@gmail.com", "name": "Dominic Fernandez"}
    user.update_user_info("u008", new_data)
    print("Update: " + str(user.get_user_info("u008")))
    test.assert_test_success("Update User")
except Exception:
    test.assert_test_failure("Update User")

# Test 5: delete user
try:
    user = User.User()
    user.delete_user("u008")
    test.assert_test_success("Delete User")
except Exception:
    test.assert_test_failure("Delete User")

test.assert_final_results()

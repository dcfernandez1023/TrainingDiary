# Simple unit tests for Body class

from tests import TestAssertion
from models import Body
from pprint import pprint

test = TestAssertion.TestAssertion()
test.print_test_name("Body Object Tests")

# Test 1: instantiation
try:
    body = Body.Body()
    test.assert_test_success("Instantiation")
except Exception:
    test.assert_test_failure("Instantiation")

# Test 2: get user body entries
try:
    body = Body.Body()
    info = body.get_user_body_entries('u001')
    pprint(str(info))
    test.assert_test_success("Get User Body Entries")
except Exception:
    test.assert_test_failure("Get User Body Entries")

# Test 3: get body entry by id
try:
    body = Body.Body()
    info = body.get_body_entry_by_id('b001')
    if info is None:
        raise Exception("Invalid Body Entry")
    pprint(str(info))
    test.assert_test_success("Get Body Entry by Id")
except Exception:
    test.assert_test_failure("Get Body Entry by Id")

# Test 4: create body entry
try:
    body = Body.Body()
    body.create_new_body_entry('b004', 'u001', 1618529709557, 15, 4, 2021, 420, "lbs", 420)
    new_body = body.get_body_entry_by_id('b004')
    if new_body is None:
        raise Exception("Create New Body Entry Failed")
    print("Created Body Entry: " + str(new_body))
    test.assert_test_success("Create New Body Entry")
except Exception:
    test.assert_test_failure("Create New Body Entry")

# Test 4: update user
try:
    body = Body.Body()
    new_data = {"timestamp": 420, "body_weight": 165, "units": "kgs", "body_fat": 10}
    body.update_body_entry('b004', new_data)
    print("Updated Body Entry: " + str(body.get_body_entry_by_id('b004')))
    test.assert_test_success("Update Body Entry")
except Exception:
    test.assert_test_failure("Update Body Entry")

# Test 5: delete body entry
try:
    body = Body.Body()
    body.delete_body_entry('b004')
    test.assert_test_success("Delete Body Entry")
except Exception:
    test.assert_test_failure("Delete Body Entry")

test.assert_final_results()

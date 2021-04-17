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

# Test 3: get body weight entry by id
try:
    body = Body.Body()
    info = body.get_body_weight_entry_by_id('bw001')
    if info is None:
        raise Exception("Invalid Body Weight Entry")
    pprint(str(info))
    test.assert_test_success("Get Body Weight Entry by Id")
except Exception:
    test.assert_test_failure("Get Body Weight Entry by Id")

# Test 3: get body fat entry by id
try:
    body = Body.Body()
    info = body.get_body_fat_entry_by_id('bf001')
    if info is None:
        raise Exception("Invalid Body Fat Entry")
    pprint(str(info))
    test.assert_test_success("Get Body Fat Entry by Id")
except Exception:
    test.assert_test_failure("Get Body Fat Entry by Id")

# Test 4: create body weight entry
try:
    body = Body.Body()
    body.create_new_body_weight_entry('bw003', 'u001', 420, 'lbs', 1618637490472, 16, 4, 2021, 'yoo')
    new_body = body.get_body_weight_entry_by_id('bw003')
    if new_body is None:
        raise Exception("Create New Body Weight Entry Failed")
    print("Created Body Entry: " + str(new_body))
    test.assert_test_success("Create New Body Weight Entry")
except Exception:
    test.assert_test_failure("Create New Body Weight Entry")

# Test 4: create body fat entry
try:
    body = Body.Body()
    body.create_new_body_fat_entry('bf003', 'u001', 420, 1618637490472, 16, 4, 2021, 'CREATE NEW')
    new_body = body.get_body_fat_entry_by_id('bf003')
    if new_body is None:
        raise Exception("Create New Body Fat Entry Failed")
    print("Created Body Entry: " + str(new_body))
    test.assert_test_success("Create New Body Fat Entry")
except Exception:
    test.assert_test_failure("Create New Body Fat Entry")

# Test 4: update body weight entry
try:
    body = Body.Body()
    new_data = {"timestamp": 420, "weight": 165, "units": "kgs", "notes": "UPDATED BW YO"}
    body.update_body_weight_entry('bw003', new_data)
    print("Updated Body Weight Entry: " + str(body.get_body_weight_entry_by_id('bw003')))
    test.assert_test_success("Update Body Weight Entry")
except Exception:
    test.assert_test_failure("Update Body Weight Entry")

# Test 4: update body fat entry
try:
    body = Body.Body()
    new_data = {"timestamp": 420, "percentage": 10, "notes": "UPDATED BF YO"}
    body.update_body_fat_entry('bf003', new_data)
    print("Updated Body Fat Entry: " + str(body.get_body_fat_entry_by_id('bf003')))
    test.assert_test_success("Update Body Fat Entry")
except Exception:
    test.assert_test_failure("Update Body Fat Entry")

# Test 5: delete body weight entry
try:
    body = Body.Body()
    body.delete_body_weight_entry('bw003')
    test.assert_test_success("Delete Body Weight Entry")
except Exception:
    test.assert_test_failure("Delete Body Entry")

# Test 5: delete body entry
try:
    body = Body.Body()
    body.delete_body_fat_entry('bf003')
    test.assert_test_success("Delete Body Fat Entry")
except Exception:
    test.assert_test_failure("Delete Body Fat Entry")

test.assert_final_results()

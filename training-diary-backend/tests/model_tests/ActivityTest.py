# Simple unit tests for Activity class

from tests import TestAssertion
from models import Activity
from pprint import pprint

test = TestAssertion.TestAssertion()
test.print_test_name("Activity Object Tests")

# Test 1: instantiation
try:
    activity = Activity.Activity()
    test.assert_test_success("Instantiation")
except Exception:
    test.assert_test_failure("Instantiation")

# Test 3: get user activities
try:
    activity = Activity.Activity()
    pprint(str(activity.get_user_activities("u001")))
    test.assert_test_success("Get User Activities")
except Exception:
    test.assert_test_failure("Get User Activities")

# Test 3: get activities by date
try:
    activity = Activity.Activity()
    pprint(str(activity.get_activities_by_date('u001', 15, 4, 2021)))
    test.assert_test_success("Get Activities by Date")
except Exception:
    test.assert_test_failure("Get Activities by Date")

# Test 3: get activities by year
try:
    activity = Activity.Activity()
    pprint(str(activity.get_activities_by_year("u001", 2021)))
    test.assert_test_success("Get Activities by Year")
except Exception:
    test.assert_test_failure("Get Activities by Year")

# Test 4: get activity by id
try:
    activity = Activity.Activity()
    pprint(str(activity.get_activity_by_id('a001')))
    test.assert_test_success("Get Activity by Id")
except Exception:
    test.assert_test_failure("Get Activity by Id")

# Test 5: create new activity
try:
    activity = Activity.Activity()
    activity.create_new_activity('a002', 'u001', 'e001', 1447920000000, 19, 10, 2015, 'YOOOO')
    pprint("New Activity: " + str(activity.get_activity_by_id('a002')))
    test.assert_test_success("Create New Activity")
except Exception:
    test.assert_test_failure("Create New Activity")

# Test 6: update activity
try:
    activity = Activity.Activity()
    activity.update_activity('a002', {"notes": "UPDATED NOTES", "timestamp": 1618525464460})
    pprint("Updated Activity: " + str(activity.get_activity_by_id('a002')))
    test.assert_test_success("Update Activity")
except Exception:
    test.assert_test_failure("Update Activity")

# Test 7 delete activity
try:
    activity = Activity.Activity()
    activity.delete_activity('a002')
    test.assert_test_success("Delete Activity")
except Exception:
    test.assert_test_failure("Delete Activity")

test.assert_final_results()

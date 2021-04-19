# Simple unit tests for Custom class

from tests import TestAssertion
from models import Custom
from pprint import pprint

test = TestAssertion.TestAssertion()
test.print_test_name("Custom Object Tests")


# Test 1: instantiation
try:
    custom = Custom.Custom()
    test.assert_test_success("Instantiation")
except Exception:
    test.assert_test_failure("Instantiation")

# Test 2: get custom types and entries
try:
    custom = Custom.Custom()
    pprint("User Custom Types: " + str(custom.get_user_custom_types('u001')))
    pprint("User Custom Entries: " + str(custom.get_user_custom_entries('u001')))
    pprint("Custom Type by Id: " + str(custom.get_custom_type_by_id('c001')))
    pprint("Custom Entries by Custom Id: " + str(custom.get_user_custom_entries_by_custom_id('c001')))
    pprint("Custom Entry by Entry Id: " + str(custom.get_custom_entry_by_id('ce001')))
    test.assert_test_success("Get Custom Types and Entries")
except Exception:
    test.assert_test_failure("Get Custom Types and Entries")

# Test 3: create new custom type
try:
    custom = Custom.Custom()
    custom.create_new_custom_type('c002', 'u001', {"test": "test"})
    test.assert_test_success("Create New Custom Type")
except Exception:
    test.assert_test_failure("Create New Custom Type")

# Test 4: create new custom entry
try:
    custom = Custom.Custom()
    custom.create_new_custom_entry("ce002", "c002", "u001", {"test": "test"}, 23465463546654, 16, 4, 2021, "test create custom entry")
    test.assert_test_success("Create New Custom Entry")
except Exception:
    test.assert_test_failure("Create New Custom Entry")

# Test 5: update custom type
try:
    custom = Custom.Custom()
    pprint("Before update: " + str(custom.get_custom_type_by_id('c002')))
    custom.update_custom_type('c002', {"custom_schema": {"test": "test"}})
    pprint("After update: " + str(custom.get_custom_type_by_id('c002')))
    test.assert_test_success("Update Custom Type")
except Exception:
    test.assert_test_failure("Update Custom Type")


# Test: 6 update custom entry
try:
    custom = Custom.Custom()
    pprint("Before update: " + str(custom.get_custom_entry_by_id('ce002')))
    custom.update_custom_entry('ce002', 'c002', {"custom_entry": {"test": "123"}, "notes": "UPDATED NOTESSSS"})
    pprint("After update: " + str(custom.get_custom_entry_by_id('ce002')))
    test.assert_test_success("Update Custom Entry")
except Exception:
    test.assert_test_failure("Update Custom Entry")

# Test: 7 delete custom type and custom entry
try:
    custom = Custom.Custom()
    custom.delete_custom_type('c002')
    test.assert_test_success("Delete Custom Type & Custom Entry")
except Exception:
    test.assert_test_failure("Delete Custom Type & Custom Entry")

test.assert_final_results()

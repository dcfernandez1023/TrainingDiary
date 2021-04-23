# Simple unit tests for Exercise class

from tests import TestAssertion
from models import Exercise
from db import DbAccess
from pprint import pprint

db = DbAccess.DbAccess()
test = TestAssertion.TestAssertion()
test.print_test_name("Exercise Object Tests")


# Test 1: instantiation
try:
    exercise = Exercise.Exercise(db)
    test.assert_test_success("Instantiation")
except Exception:
    test.assert_test_failure("Instantiation")

# Test 2: get user exercises
try:
    exercise = Exercise.Exercise(db)
    info = exercise.get_user_exercises("u001")
    if info is None:
        raise Exception("No Workout Data Returned")
    pprint("User Exercises: " + str(info))
    pprint("User Exercise Entries: " + str(exercise.get_user_exercise_entries("u001")))
    pprint("User Exercise Entries by Year (2021): " + str(exercise.get_user_exercise_entries_by_year('u001', 2021)))
    test.assert_test_success("Get User Exercises and Entries")
except Exception:
    test.assert_test_failure("Get User Exercises and Entries")

# Test 3: get exercise by id
try:
    exercise = Exercise.Exercise(db)
    info = exercise.get_exercise_by_id("e001")
    if info is None:
        raise Exception("No Exercise Data Returned")
    print(str(info))
    test.assert_test_success("Get Exercise by Id")
except Exception:
    test.assert_test_failure("Get Exercise by Id")

# Test 4: create new exercise
try:
    exercise = Exercise.Exercise(db)
    exercise.create_new_exercise('e007', 'u001', 'Push-ups', 'Body-Weight', 4, 50, 0, 'lbs')
    test.assert_test_success("Create New Exercise")
except Exception:
    test.assert_test_failure("Create New Exercise")

# Test 5: create new exercises
try:
    exercise = Exercise.Exercise(db)
    exercise.create_new_exercises(
        [
            ['e008', 'u001', 'Test2', 'Body-Weight', 4, 50, 0, 'lbs'],
            ['e009', 'u001', 'Test3', 'Body-Weight', 4, 50, 0, 'lbs'],
            ['e010', 'u001', 'Test4', 'Body-Weight', 4, 50, 0, 'lbs']
        ]
    )
    test.assert_test_success("Create New Exercises")
except Exception:
    test.assert_test_failure("Create New Exercises")

# Test 6: Create new exercise entries
try:
    exercise = Exercise.Exercise(db)
    exercise.create_new_exercise_entries(
        [
            ('ee005', 'e008', 'u001', 1618637490472, 16, 4, 2021, 'new entry1'),
            ('ee006', 'e009', 'u001', 1447920000000, 19, 10, 2015, 'new entry2'),
            ('ee007', 'e010', 'u001', 1618637490472, 16, 4, 2021, 'new entry3'),
        ]
    )
    test.assert_test_success("Create New Exercises Entries")
except Exception:
    test.assert_test_failure("Create New Exercises Entries")


# Test 7: update exercise
try:
    exercise = Exercise.Exercise(db)
    new_data = {"name": "UPDATED EXERCISE", "category": "UPDATED CATEGORY", "sets": 420}
    exercise.update_exercise('e007', new_data)
    print(str(exercise.get_exercise_by_id('e007')))
    test.assert_test_success("Update Exercise")
except Exception:
    test.assert_test_failure("Update Exercise")

# Test 8: update exercise entry
try:
    exercise = Exercise.Exercise(db)
    new_data = {
        "exercise_entry_id": "ee005",
        "exercise_id": "e008",
        "user_id": "u001",
        "timestamp": 1618637490472,
        "day": 16,
        "month": 4,
        "year": 2021,
        "notes": "UPDATED NOTES OF THIS ENTRY YOOOO"
    }
    exercise.update_exercise_entry('ee005', new_data)
    print(str(exercise.get_exercise_entries_by_exercise_id('e001')))
    test.assert_test_success("Update Exercise Entry")
except Exception:
    test.assert_test_failure("Update Exercise")

# Test 9: delete exercise entry
try:
    exercise = Exercise.Exercise(db)
    exercise.delete_exercise_entry_by_id('ee005')
    test.assert_test_success("Delete Exercise Entry")
except Exception:
    test.assert_test_failure("Delete Exercise Entry")

# Test 10: delete exercise
try:
    exercise = Exercise.Exercise(db)
    exercise.delete_exercise('e007')
    exercise.delete_exercise('e008')
    exercise.delete_exercise('e009')
    exercise.delete_exercise('e010')
    test.assert_test_success("Delete Exercise")
except Exception:
    test.assert_test_failure("Delete Exercise")


test.assert_final_results()
db.close_connection()

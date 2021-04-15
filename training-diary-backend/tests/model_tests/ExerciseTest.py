# Simple unit tests for Exercise class

from tests import TestAssertion
from models import Exercise


test = TestAssertion.TestAssertion()
test.print_test_name("Exercise Object Tests")


# Test 1: instantiation
try:
    exercise = Exercise.Exercise()
    test.assert_test_success("Instantiation")
except Exception:
    test.assert_test_failure("Instantiation")

# Test 2: get user exercises
try:
    exercise = Exercise.Exercise()
    info = exercise.get_user_exercises("u001")
    if info is None:
        raise Exception("No Workout Data Returned")
    print(str(info))
    test.assert_test_success("Get User Exercises")
except Exception:
    test.assert_test_failure("Get User Exercises")

# Test 3: get workout by id
try:
    exercise = Exercise.Exercise()
    info = exercise.get_exercise_by_id("e001")
    if info is None:
        raise Exception("No Exercise Data Returned")
    print(str(info))
    test.assert_test_success("Get Exercise by Id")
except Exception:
    test.assert_test_failure("Get Exercise by Id")

# Test 4: create new exercise
try:
    exercise = Exercise.Exercise()
    exercise.create_new_exercise('u001', 'Push-ups', 'Body-Weight', 4, 50, 0, 'lbs')
    test.assert_test_success("Create New Exercise")
except Exception:
    test.assert_test_failure("Create New Exercise")

# Test 5: create new exercises
try:
    exercise = Exercise.Exercise()
    exercise.create_new_exercises(
        [
            ['e007', 'u001', 'Test1', 'Body-Weight', 4, 50, 0, 'lbs'],
            ['e008', 'u001', 'Test2', 'Body-Weight', 4, 50, 0, 'lbs'],
            ['e009', 'u001', 'Test3', 'Body-Weight', 4, 50, 0, 'lbs'],
            ['e010', 'u001', 'Test4', 'Body-Weight', 4, 50, 0, 'lbs']
        ]
    )
    test.assert_test_success("Create New Exercises")
except Exception:
    test.assert_test_failure("Create New Exercises")

# Test 6: update exercise
try:
    exercise = Exercise.Exercise()
    new_data = {"name": "UPDATED EXERCISE", "category": "UPDATED CATEGORY", "sets": 420}
    exercise.update_exercise('e007', new_data)
    print(str(exercise.get_exercise_by_id('e007')))
    test.assert_test_success("Update Exercise")
except Exception:
    test.assert_test_failure("Update Exercise")

# Test 7: delete exercise
try:
    exercise = Exercise.Exercise()
    exercise.delete_exercise('e007')
    exercise.delete_exercise('e008')
    exercise.delete_exercise('e009')
    exercise.delete_exercise('e010')
    test.assert_test_success("Delete Exercise")
except Exception:
    test.assert_test_failure("Delete Exercise")


test.assert_final_results()

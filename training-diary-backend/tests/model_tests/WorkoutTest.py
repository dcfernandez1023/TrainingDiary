# Simple unit tests for User class

from tests import TestAssertion
from models import Workout

test = TestAssertion.TestAssertion()
test.print_test_name("Workout Object Tests")

WORKOUT_ID = ""

# Test 1: instantiation
try:
    workout = Workout.Workout()
    test.assert_test_success("Instantiation")
except Exception:
    test.assert_test_failure("Instantiation")

# Test 2: get user workouts
try:
    workout = Workout.Workout()
    info = workout.get_user_workouts("u001")
    if info is None:
        raise Exception("No Workout Data Returned")
    print(str(info))
    test.assert_test_success("Get User Workouts")
except Exception:
    test.assert_test_failure("Get User Workouts")

# Test 3: get workout by id
try:
    workout = Workout.Workout()
    info = workout.get_workout_by_id("w1")
    if info is None:
        raise Exception("No Workout Data Returned")
    print(str(info))
    test.assert_test_success("Get Workout by Id")
except Exception:
    test.assert_test_failure("Get Workout by Id")

# Test 4: create new workout
try:
    workout = Workout.Workout()
    WORKOUT_ID = workout.create_new_workout("u008", "Test Workout", "4/13/21", 1, "Testing description")
    created_workout = workout.get_workout_by_id(WORKOUT_ID)
    if created_workout is None:
        raise Exception("Create Workout Failed")
    print(str(created_workout))
    test.assert_test_success("Create New Workout")
except Exception:
    test.assert_test_failure("Create New Workout")

# Test 5: update workout
try:
    workout = Workout.Workout()
    new_data = {"description": "New description!", "name": "New name!"}
    workout.update_workout(WORKOUT_ID, new_data)
    print("Update: " + str(workout.get_workout_by_id(WORKOUT_ID)))
    test.assert_test_success("Update Workout")
except Exception:
    test.assert_test_failure("Update Workout")

# Test 6: delete workout
try:
    workout = Workout.Workout()
    workout.delete_workout(WORKOUT_ID)
    test.assert_test_success("Delete Workout")
except Exception:
    test.assert_test_failure("Delete Workout")

# Test 7: get public workouts
try:
    workout = Workout.Workout()
    print(str(workout.get_public_workouts()))
    test.assert_test_success("Get Public Workouts")
except Exception:
    test.assert_test_failure("Get Public Workouts")

# Test 8: get user's workouts along with exercises associated with each workout
try:
    workout = Workout.Workout()
    print(str(workout.get_user_workouts_with_exercises("u001")))
    test.assert_test_success("Workouts with Exercises")
except Exception:
    test.assert_test_failure("Workouts with Exercises")

test.assert_final_results()

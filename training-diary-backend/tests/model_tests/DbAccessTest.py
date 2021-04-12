# Simple unit tests for DbAccess class

import os
from tests import TestAssertion
from models import DbAccess

test = TestAssertion.TestAssertion()
test.print_test_name("DbAccess Tests")

# Test 1: instantiation
try:
    db = DbAccess.DbAccess("../../db/data/training_diary_db")
    db.close_connection()
    test.assert_test_success("Instantiation")
except Exception:
    test.assert_test_failure("Instantiation")

# Test 2: init dbs
try:
    file = open("../../db/queries/init_training_diary_db.sql", "r")
    db_inits = {"training_diary_db": file.read()}
    DbAccess.DbAccess.init_dbs("../../db/data", db_inits)
    file.close()
    test.assert_test_success("Initialize Database")
except Exception:
    test.assert_test_failure("Initialize Database")

# Test 3: select entire tables
try:
    db = DbAccess.DbAccess("../../db/data/training_diary_db")
    users = db.get_data("SELECT * FROM Users")
    activities = db.get_data("SELECT * FROM Activities")
    workouts = db.get_data("SELECT * FROM Workouts")
    exercises = db.get_data("SELECT * FROM Exercises")
    body = db.get_data("SELECT * FROM Body")
    # print("-- Test 3 stdout --")
    # print("    " + str(users))
    # print("    " + str(activities))
    # print("    " + str(workouts))
    # print("    " + str(exercises))
    # print("    " + str(body))
    db.close_connection()
    test.assert_test_success("Select All")
except Exception:
    test.assert_test_failure("Select Data")

# Test 4: select on condition
try:
    db = DbAccess.DbAccess("../../db/data/training_diary_db")
    # testing real queries the application would use
    # print("-- Test 4 stdout --")
    # user = db.get_data("SELECT * FROM Users WHERE user_id = '001'")
    # print("    " + "User 001: " + str(user))
    # activities = db.get_data("SELECT * FROM Activities WHERE user_id = '001'")
    # print("    " + "User 001's activities: " + str(activities))
    # workouts = db.get_data("SELECT * FROM Workouts WHERE user_id = '001'")
    # print("    " + "User 001's workouts: " + str(workouts))
    # exercises = db.get_data("SELECT * FROM Exercises WHERE workout_id = 'w1'")
    # print("    " + "Workout w1's exercises: " + str(exercises))
    # body = db.get_data("SELECT * FROM Body WHERE user_id = '001'")
    # print("    " + "User 001's body entries: " + str(body))
    db.close_connection()
    test.assert_test_success("Select on Condition")
except Exception:
    test.assert_test_failure("Select on Condition")

# Test 5: insert data
try:
    db = DbAccess.DbAccess("../../db/data/training_diary_db")
    db.insert_data("INSERT INTO Users VALUES ('004', 'test4@gmail.com', 'test4')")
    db.close_connection()
    test.assert_test_success("Insert Data")
except Exception:
    test.assert_test_failure("Insert Data")

# Test 6: delete data
try:
    db = DbAccess.DbAccess("../../db/data/training_diary_db")
    db.delete_data("DELETE FROM Users WHERE user_id = '003'")
    db.close_connection()
    test.assert_test_success("Delete Data")
except Exception:
    test.assert_test_failure("Delete Data")

# Test 7: update data
try:
    db = DbAccess.DbAccess("../../db/data/training_diary_db")
    db.update_data("UPDATE Workouts SET name = 'Hypertrophy Chest Day' WHERE workout_id = 'w1'")
    db.close_connection()
    test.assert_test_success("Update Data")
except Exception:
    test.assert_test_failure("Update Data")

# Test 8: multiple requests
try:
    from threading import Thread
    def func1():
        db = DbAccess.DbAccess("../../db/data/training_diary_db")
        db.insert_data("INSERT INTO Users VALUES ('005', 'test5@gmail.com', 'test5')")
        db.close_connection()
    def func2():
        db = DbAccess.DbAccess("../../db/data/training_diary_db")
        db.insert_data("INSERT INTO Users VALUES ('006', 'test6@gmail.com', 'test6')")
        db.close_connection()
    Thread(target=func1).start()
    Thread(target=func2).start()
    db = DbAccess.DbAccess("../../db/data/training_diary_db")
    db.delete_data("DELETE FROM Users WHERE user_id = '005'")
    db.delete_data("DELETE FROM Users WHERE user_id = '006'")
    db.close_connection()
    test.assert_test_success("Multiple Requests")
except Exception:
    test.assert_test_failure("Multiple Requests")

test.assert_final_results()

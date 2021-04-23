# Simple unit tests for DbAccess class

from tests import TestAssertion
from db import DbAccess

test = TestAssertion.TestAssertion()
test.print_test_name("DbAccess Tests")

# Test 1: instantiation
try:
    db = DbAccess.DbAccess()
    db.close_connection()
    test.assert_test_success("Instantiation")
except Exception:
    test.assert_test_failure("Instantiation")

# Test 2: init dbs
try:
    file = open("../../db/queries/init_training_diary_db.sql", "r")
    query = file.read()
    db = DbAccess.DbAccess()
    db.init_database(query)
    file.close()
    test.assert_test_success("Initialize Database")
except Exception:
    test.assert_test_failure("Initialize Database")

# Test 3: select entire tables
try:
    db = DbAccess.DbAccess()
    db.get_data("SELECT * FROM Users")
    db.get_data("SELECT * FROM Exercises")
    db.get_data("SELECT * FROM ExerciseEntries")
    db.get_data("SELECT * FROM BodyWeight")
    db.get_data("SELECT * FROM BodyFat")
    db.get_data("SELECT * FROM Diet")
    db.get_data("SELECT * FROM CustomTypes")
    db.get_data("SELECT * FROM CustomEntries")
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
    db = DbAccess.DbAccess()
    #testing simple condition query
    user = db.get_data("SELECT * FROM Users WHERE user_id = 'u001'")
    db.close_connection()
    test.assert_test_success("Select on Condition")
except Exception:
    test.assert_test_failure("Select on Condition")

# Test 5: insert data
try:
    db = DbAccess.DbAccess()
    db.insert_data("INSERT INTO Users VALUES ('u004', 'test4@gmail.com', 'test4')")
    db.close_connection()
    test.assert_test_success("Insert Data")
except Exception:
    test.assert_test_failure("Insert Data")

# Test 6: delete data
try:
    db = DbAccess.DbAccess()
    db.delete_data("DELETE FROM Users WHERE user_id = 'u004'")
    db.close_connection()
    test.assert_test_success("Delete Data")
except Exception:
    test.assert_test_failure("Delete Data")

# Test 7: update data
try:
    db = DbAccess.DbAccess()
    db.update_data("UPDATE Exercises SET name = 'YOOO' WHERE exercise_id = 'e001'")
    db.close_connection()
    test.assert_test_success("Update Data")
except Exception:
    test.assert_test_failure("Update Data")

# Test 8: multiple requests
try:
    from threading import Thread
    def func1():
        db = DbAccess.DbAccess()
        db.insert_data("INSERT INTO Users VALUES ('u005', 'test5@gmail.com', 'test5')")
        db.close_connection()
    def func2():
        db = DbAccess.DbAccess()
        db.insert_data("INSERT INTO Users VALUES ('u006', 'test6@gmail.com', 'test6')")
        db.close_connection()
    Thread(target=func1).start()
    Thread(target=func2).start()
    db = DbAccess.DbAccess()
    db.delete_data("DELETE FROM Users WHERE user_id = 'u005'")
    db.delete_data("DELETE FROM Users WHERE user_id = 'u006'")
    db.close_connection()
    test.assert_test_success("Multiple Requests")
except Exception:
    test.assert_test_failure("Multiple Requests")

test.assert_final_results()

# Asserts test successes and failures and total number of tests failed/succeeded

import traceback


class TestAssertion:
    def __init__(self):
        self.__num_failed = 0
        self.__num_success = 0
        self.__total_tests = 1

    def print_test_name(self, name):
        print("\n------ " + name + " ------\n")

    def assert_test_failure(self, test_name):
        tb = traceback.format_exc()
        print("--> TEST " + str(self.__total_tests) + " " + test_name + " [FAILED]")
        print("--------------------------------")
        print(tb.strip("\n"))
        print("--------------------------------")
        self.__num_failed += 1
        self.__total_tests += 1

    def assert_test_success(self, test_name):
        print("--> TEST " + str(self.__total_tests) + " " + test_name + " [SUCCEEDED]")
        self.__num_success += 1
        self.__total_tests += 1

    def assert_actual_vs_expected(self, actual, expected):
        raise Exception("ActualVsExpected: " + str(actual) + " != " + str(expected))

    def assert_final_results(self):
        total = self.__num_failed + self.__num_success
        print("\n# " + str(self.__num_success) + "/" + str(total) + " TESTS PASSED")

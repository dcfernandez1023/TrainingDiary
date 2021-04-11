# Asserts test successes and failures and total number of tests failed/succeeded
class TestAssertion:
    def __init__(self):
        self.__num_failed = 0
        self.__num_success = 0
        self.__total_tests = 1

    def assert_test_failure(self, error_string):
        print("--> TEST " + str(self.__total_tests) + "FAILED")
        print("--------------------------------")
        print(error_string.strip("\n"))
        print("--------------------------------")
        self.__num_failed += 1
        self.__total_tests += 1

    def assert_test_success(self):
        print("--> TEST " + str(self.__total_tests) + " SUCCEEDED")
        self.__num_success += 1
        self.__total_tests += 1

    def assert_final_results(self):
        total = self.__num_failed + self.__num_success
        print("# " + str(self.__num_success) + "/" + str(total) + " TESTS PASSED")

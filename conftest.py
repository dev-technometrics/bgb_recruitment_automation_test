import pytest
TOTAL_TESTS = 0
COMPLETED_TESTS = 0
def pytest_runtest_teardown(item, nextitem):
    global COMPLETED_TESTS
    COMPLETED_TESTS += 1
def my_function():
    # Your function code here
    print("All tests have completed!")
    # Call your function here or perform any other actions you want after completing all tests
def pytest_unconfigure(config):
    if COMPLETED_TESTS == TOTAL_TESTS:
        my_function()

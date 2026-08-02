tests_run = 0
tests_failed = 0

def run_test(test):
    global tests_run
    global tests_failed
    if test():
        tests_run += 1
    else:
        tests_failed += 1

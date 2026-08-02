import time
def timer():
    last_time = time.time()

    def create_timer():
        nonlocal last_time
        current_time = time.time()
        elapsed = current_time - last_time
        last_time = current_time
        return elapsed

    return create_timer
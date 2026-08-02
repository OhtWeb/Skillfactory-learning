import time
def time_it(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = int((time.time() - start))
        print(f'Function "{func.__name__}" took {end} seconds to run')
        return result
    return wrapper

@time_it
def add(a, b):
    return a + b

summa = add(55, 84)
print(summa)
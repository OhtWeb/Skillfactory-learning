import random
def ensure_result_is_number(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if isinstance(result, int):
            return result
        else:
            return None
    return wrapper

@ensure_result_is_number
def increment_number(number):
    return number + 10
res = increment_number(10)
print(res)

@ensure_result_is_number
def add_two_numbers(a, b):
    return a + b
res = add_two_numbers(1, 2)
print(res)

@ensure_result_is_number
def kitten(cat):
    print(cat)

res = kitten("cat")
print(res)
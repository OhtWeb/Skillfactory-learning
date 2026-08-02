def handle_exceptions(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f'Function {func.__name__} raised an exception: "{e}"')
    return wrapper

@handle_exceptions
def test_function():
    raise ValueError("Some value error")

test_function()

def test_function(func, arg, expected_result):
    try:
        actual_result = func(arg)
        return actual_result == expected_result
    except Exception as e:
        print(f"Ошибка при выполнении функции {func}: {e}")
        return False
result = test_function(func, 2, 8)
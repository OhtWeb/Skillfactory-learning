def aggregate_data(*args, **kwargs):
    total_sum = 0
    string_count = 0
    for arg in args:
        if isinstance(arg, (int, float)):
            total_sum += arg
        elif isinstance(arg, str):
            string_count += 1
    for value in kwargs.values():
        if isinstance(value, (int, float)):
            total_sum += value
        elif isinstance(value, str):
            string_count += 1
    return total_sum, string_count

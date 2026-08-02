def retry_if_result_is_none(times=1):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
                if result is not None:
                    return result
                else:
                    return None
        return wrapper
    return decorator
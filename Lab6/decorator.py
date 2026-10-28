def add_prefix(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return "Результат: " + result
    return wrapper
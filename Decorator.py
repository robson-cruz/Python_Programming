def add_hello(func):
    def wrapper(*args, **kwargs):
        print(func.__doc__)
        return func(*args, **kwargs)
    return wrapper


@add_hello
def simple(a, b):
    """Adds two numbers"""
    print(a + b)


simple(2, 4)

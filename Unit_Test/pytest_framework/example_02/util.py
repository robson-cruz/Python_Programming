def is_even(number):
    if isinstance(number, int):
        return number % 2 == 0
    raise TypeError("Invalid input type, only integers allowed.")

def is_even(number):
    """
    Check if a number is even.

    Parameters:
    number (int): The number to check.

    Returns:
    bool: True if the number is even, False otherwise.

    Raises:
    TypeError: If the input is not an integer.

    Example:
    >>> is_even(4)
    True
    >>> is_even(3)
    False
    >>> is_even("abc")
    Traceback (most recent call last):
        ...
    TypeError: Invalid input type, only integers allowed.
    """
    if isinstance(number, int):
        return number % 2 == 0
    raise TypeError("Invalid input type, only integers allowed.")

def string_to_lower(string):
    if not isinstance(string, str):
        raise ValueError("Input must be a string")
    return string.lower()

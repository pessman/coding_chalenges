def first_recurring_character(string):
    if not isinstance(string, str):
        raise TypeError("string paramater must be of type string")

    chars = set()
    for char in string:
        if char in chars:
            return char
        chars.add(char)

    return None
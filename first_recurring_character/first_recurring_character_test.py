import pytest

from first_recurring_character import first_recurring_character


def test_invalid_string_type():
    """
    Test to confirm we raise a type error when an object not of type string is provided
    """

    with pytest.raises(TypeError):
        char = first_recurring_character(None)

def test_valid_string():
    """
    Test to confirm function returns a character that is repeated
    """

    assert first_recurring_character("ABCDEA") == "A"

def test_no_recurring_chars():
    """
    Test to confirm function returns None when no characters are repeated
    """

    assert first_recurring_character("ABCD") == None

def test_multiple_recurring_chars():
    """
    Test to confirm function returns the FIRST recurring character if their are multiple possibilities
    """

    assert first_recurring_character("ABCDAB") == "A"
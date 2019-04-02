import pytest

from first_non_recurring_char import first_non_recurring_char

def test_invalid_string_type():
    with pytest.raises(TypeError):
        char = first_non_recurring_char(None)

def test_empty_string():
    assert first_non_recurring_char("") == None

def test_all_repeated():
    assert first_non_recurring_char("AABBCC") == None

def test_one_non_repeated():
    assert first_non_recurring_char("AABBCCDEEFF") == "D"

def test_multi_non_repeated():
    assert first_non_recurring_char("ABBCCDDEFFGG") == "A"
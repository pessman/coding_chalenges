import pytest

from subsets_that_add_to_n import subsets_that_add_to_n_v2


def test_invalid_list_type():
    with pytest.raises(TypeError):
        subsets = subsets_that_add_to_n_v2(None, 20)


def test_invalid_list_item_type():
    with pytest.raises(TypeError):
        subsets = subsets_that_add_to_n_v2([1, 2, 3.3], 20)


def test_invalid_target_type():
    with pytest.raises(TypeError):
        subsets = subsets_that_add_to_n_v2([1, 2, 3], 3.3)


def test_empty_list():
    assert subsets_that_add_to_n_v2([], 20) == []


def test_no_subsets():
    assert subsets_that_add_to_n_v2([1, 2, 3], 100) == []


def test_subsets():
    assert subsets_that_add_to_n_v2([2, 4, 6, 10], 16) == [[2, 4, 10], [6, 10]]
    assert subsets_that_add_to_n_v2([1, 2, 3, 4, 5], 10) == [
        [1, 2, 3, 4], [1, 4, 5], [2, 3, 5]]
    assert subsets_that_add_to_n_v2([2, 3, 2], 5) == [[2, 3], [3, 2]]


def test_target_zero():
    assert subsets_that_add_to_n_v2([1, 2, 3], 0) == [[]]

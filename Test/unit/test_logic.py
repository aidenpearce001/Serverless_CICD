import pytest

def test_sum_correct(logic) -> None:
    assert logic.simple_sum(1, 2) == 3, "Failed"

def test_sum_correct(logic) -> None:
    assert logic.multiple(2, 2) == 4, "Failed"

def test_sum_correct(logic) -> None:
    assert logic.square_root(9) == 3, "Failed"
import pytest

def test_sum_correct(logic) -> None:
    assert logic.simple_sum(1, 2) == 3, "Failed"

def test_sum_fail(logic) -> None:
    assert logic.simple_sum(3, 2) == 5, "Failed"

import pytest

from mongodb_crud.utils.SimpleMath import *

def test_sum():
    assert sum(2, 2) == 4, "Wrong as fuk"
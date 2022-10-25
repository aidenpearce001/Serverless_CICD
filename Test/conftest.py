import pytest
from mongodb_crud.utils.SimpleMath import Basic
from mongodb_crud.utils.MarkManagement import MarkCalulator

@pytest.fixture()
def logic():
    """Create SimpleMath object"""
    logic = Basic()
    return logic

@pytest.fixture()
def Calulator():
    Calulator = MarkCalulator()
    return Calulator

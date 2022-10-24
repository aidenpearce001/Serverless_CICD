import pytest
from mongodb_crud.utils.SimpleMath import Basic

@pytest.fixture()
def logic():
    """Create SimpleMath object"""
    logic = Basic()
    return logic

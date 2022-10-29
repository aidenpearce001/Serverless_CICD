import pytest
from mongodb_crud.utils.SimpleMath import Basic
from mongodb_crud.utils.MarkManagement import MarkCalulator

@pytest.fixture()
def context():
    @dataclass
    class LambdaContext:
        function_name: str = "test"
        aws_request_id: str = "88888888-4444-4444-4444-121212121212"
        invoked_function_arn: str = "arn:aws:lambda:eu-west-1:123456789101:function:test"

    return LambdaContext()
    
@pytest.fixture()
def logic():
    """Create SimpleMath object"""
    logic = Basic()
    return logic

@pytest.fixture()
def Calulator():
    Calulator = MarkCalulator()
    return Calulator

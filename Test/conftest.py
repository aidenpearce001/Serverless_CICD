import pytest
from mongodb_crud.utils.SimpleMath import Basic
from mongodb_crud.utils.MarkManagement import MarkCalulator

@pytest.fixture()
def lambda_context():
    """ Generates AWS Lambda context"""

    data = """{
        "aws_request_id": "abcdef",
        "invoked_function_arn": "arn:aws:lambda:eu-west-1:123456789012:function:SampleFunctionName-ERERWEREWR",
        "log_group_name": "/aws/lambda/SampleFunctionName-ERERWEREWR",
        "function_name": "SampleFunctionName-ERERWEREWR",
        "function_version": "$LATEST"
    }"""

    context = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))

    return context
    
@pytest.fixture()
def logic():
    """Create SimpleMath object"""
    logic = Basic()
    return logic

@pytest.fixture()
def Calulator():
    Calulator = MarkCalulator()
    return Calulator

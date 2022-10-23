# import pytest

# def test_create_record(apigw_event, mocker):

#     ret = Create.app.lambda_handler(apigw_event, "")
#     data = json.loads(ret["body"])

#     assert ret["statusCode"] == 200
#     assert "message" in ret["body"]
#     assert data["message"] == "hello world"
#     assert "location" in data.dict_keys()

# def test_read_record():

#     ret = Create.app.lambda_handler(apigw_event, "")
#     data = json.loads(ret["body"])

#     assert ret["statusCode"] == 200
#     assert "message" in ret["body"]
#     assert data["message"] == "hello world"
#     assert "location" in data.dict_keys()
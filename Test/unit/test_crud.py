# import pytest
# import json

# import mongodb_crud.CRUD.Create.app
# import mongodb_crud.CRUD.Read.app
# import mongodb_crud.CRUD.Update.app
# import mongodb_crud.CRUD.Delete.app

# def test_create_record(apigw_event, mocker):

#     ret = Create.app.lambda_handler(apigw_event, "")
#     data = json.loads(ret["body"])

#     assert ret["statusCode"] == 200
#     assert "message" in ret["body"]
#     assert data["message"] == "hello world"
#     assert "location" in data.dict_keys()

# env = "Test"
# Database = "Test"

# def apigw_event():
#     """ Generates API GW Event"""

#     return {
#         "body": '{ "test": "body"}',
#     }

# def test_read_record():

#     ret = mongodb_crud.CRUD.Read.app.DbRead(apigw_event())
#     data = json.loads(ret["body"])

#     assert "test" in ret["body"]
#     assert data["test"] == "body"
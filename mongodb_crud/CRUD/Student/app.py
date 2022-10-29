import os, traceback, json, logging
from functools import wraps

logging.basicConfig(format="%(asctime)s %(name)s %(levelname)s %(message)s")
logger = logging.getLogger("Student")
logger.setLevel(os.environ.get("LOGGING", logging.DEBUG))

try:
    import boto3
    import pymongo
except ImportError as E:
    logger.error(E)

def cloudwatch_logs(function):
    @wraps(function)
    def wrapper(event, context):
        logger.info(f'{context.function_name} - entry.\nIncoming event: {event}')
        result = function(event, context)
        logger.info(f'{context.function_name} - exit.\nResult: {result}')
        return result

    return wrapper

class UnknownEventException(Exception):
    pass

def load_config(self, ssm_parameter_path):
        """
        Get Parameter from  SSM Parameter Store
        :param ssm_parameter_path: Path to app config in SSM Parameter Store
        :return: ConfigParser holding loaded config
        """
        
        try:
            # Get all parameters for this app
            param_details = self.ssm.get_parameter(
                Name=ssm_parameter_path,
                WithDecryption=True
            )

            configuration = param_details.get('Parameter', [])
            
        except:
            print("Encountered an error loading config from SSM.")
            traceback.print_exc()
        finally:
            return configuration["Value"]

class StudentCRUD:
    def __init__(self, region="ap-southeast-1"):
        self.logger = logging.getLogger(self.__class__.__name__)
        self.logger.setLevel(os.environ.get("LOGGING", logging.DEBUG))
        self.ssm = boto3.client("ssm")

        # Initial MongoDB Client
        # self.MongoConnector = pymongo.MongoClient(load_config("/" + os.environ["ENV"] + "/" + os.environ["Db"]))
        # self.Database  = self.MongoConnector[os.environ["DatabaseName"]]
        # self.Collection = self.Database[os.environ["CollectionName"]]

        self.MongoConnector = pymongo.MongoClient("mongodb+srv://usth:123123a@hack-extenstion.gylmd.mongodb.net/test")
        self.Database  = self.MongoConnector["SchoolManagement"]
        self.Collection = self.Database["Student"]

    def POST(self, event):

        self.Collection.insert(event["body"])
        logger.info(f'Insert Successfully Item {event["body"]["StudentID"]}')

    def UPDATE(self, event):

        filter = {
            "StudentID": event["requestContext"]["resourceId"]
        }

        mycol.update_one(filter, event["body"])
        self.Collection.update_one(event["body"], {})

        logger.info(f'Update Successfully Item {event["requestContext"]["resourceId"]}')

    def DELETE(self, event):

        self.Collection.delete_one(event["body"])
        logger.info(f'Delete Successfully Item {event["body"]["StudentID"]}')

    def GET(self, event):

        if "{id}" in event["resource"]:
            return self.Collection.find({"StudentName": event["requestContext"]["resourceId"]})

        else:
            return [_ for _ in self.Collection.find()]

@cloudwatch_logs
def handler(event, context):

    return getattr(globals()["StudentCRUD"](), event["httpMethod"])(event)

event = {
    "resource": "/",
    "path": "/",
    "httpMethod": "GET",
    "requestContext": {
        "resourcePath": "/",
        "httpMethod": "GET",
        "path": "/Prod/"
    },
    "headers": {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "accept-encoding": "gzip, deflate, br",
        "Host": "70ixmpl4fl.execute-api.us-east-2.amazonaws.com",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36",
        "X-Amzn-Trace-Id": "Root=1-5e66d96f-7491f09xmpl79d18acf3d050",
    },
    "multiValueHeaders": {
        "accept": [
            "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
        ],
        "accept-encoding": [
            "gzip, deflate, br"
        ]
    },
    "queryStringParameters": "",
    "multiValueQueryStringParameters": "",
    "pathParameters": "",
    "stageVariables": "",
    "body": "",
    "isBase64Encoded": False
}


from dataclasses import dataclass

def context():
    @dataclass
    class LambdaContext:
        function_name: str = "test"
        aws_request_id: str = "88888888-4444-4444-4444-121212121212"
        invoked_function_arn: str = "arn:aws:lambda:eu-west-1:123456789101:function:test"

    return LambdaContext()

handler(event, context())
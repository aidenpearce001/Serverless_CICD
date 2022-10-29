import os, traceback, json, logging
from functools import wraps

logging.basicConfig(format="%(asctime)s %(name)s %(levelname)s %(message)s")
logger = logging.getLogger("Student")
logger.setLevel(os.environ.get("LOGGING", logging.DEBUG))

try:
    import boto3
    # import pymongo
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
            # return [_ for _ in self.Collection.find()]

            return { 
                'statusCode': 200,
                'body': json.dumps("Last Version")
            }

@cloudwatch_logs
def lambda_handler(event, context):

    return getattr(globals()["StudentCRUD"](), event["httpMethod"])(event)


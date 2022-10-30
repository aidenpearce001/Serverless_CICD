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

def db_connection(self, ssm_parameter_path):
        """
        Get Parameter from SSM Parameter Store and connect
        to MongoDB 
        :param ssm_parameter_path: Path to app config in SSM Parameter Store
        :Collection: Initialize MongoDB connection
        """
        
        try:
            # Get all parameters for this app
            param_details = self.ssm.get_parameter(
                Name=ssm_parameter_path,
                WithDecryption=True
            )

            configuration = param_details.get('Parameter', [])

        except:
            logger.warning("Encountered an error loading config from SSM.")
            traceback.print_exc()

        finally:

            try:
                MongoConnector = pymongo.MongoClient(configuration["Value"])
                Database  = MongoConnector[os.environ["DatabaseName"]]
                Collection = Database[os.environ["CollectionName"]]

                return Collection

            except pymongo.errors.ConnectionFailure, e:
                logger.warning(f"Could not connect to server: {e}")

db = db_connection("/" + os.environ["ENV"] + "/" + os.environ["Db"])

class TeacherCRUD:
    def __init__(self, region="ap-southeast-1"):
        self.logger = logging.getLogger(self.__class__.__name__)
        self.logger.setLevel(os.environ.get("LOGGING", logging.DEBUG))
        self.ssm = boto3.client("ssm")

    def POST(self, event):

        db.insert(event["body"])
        logger.info(f'Insert Successfully Item {event["body"]["TeacherID"]}')

    def UPDATE(self, event):

        filter = {
            "StudentID": event["requestContext"]["resourceId"]
        }

        mycol.update_one(filter, event["body"])
        db.update_one(event["body"], {})

        logger.info(f'Update Successfully Item {event["requestContext"]["resourceId"]}')

    def DELETE(self, event):

        db.delete_one(event["body"])
        logger.info(f'Delete Successfully Item {event["body"]["TeacherID"]}')

    def GET(self, event):

        if "{id}" in event["resource"]:
            return db.find({"TeacherName": event["requestContext"]["resourceId"]})

        else:
            return [_ for _ in db.find()]

        
@cloudwatch_logs
def lambda_handler(event, context):

    return getattr(globals()["TeacherCRUD"](), event["httpMethod"])(event)


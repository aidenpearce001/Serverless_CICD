import json, logging, os

logging.basicConfig(format="%(asctime)s %(name)s %(levelname)s %(message)s")
logger = logging.getLogger("Homepage")
logger.setLevel(os.environ.get("LOGGING", logging.DEBUG))

def lambda_handler(event, context):

    return { 
        'statusCode': 200,
        'body': json.dumps(f"Current Eviroment {event['requestContext']['path'].split('/')[1]} 2.0")
    }


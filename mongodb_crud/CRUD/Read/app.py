import os, traceback, json
import boto3

env = os.environ["ENV"]
Database = os.environ["Db"]
client = boto3.client("ssm")

def load_config(ssm_parameter_path):
    """
    Get Parameter from  SSM Parameter Store
    :param ssm_parameter_path: Path to app config in SSM Parameter Store
    :return: ConfigParser holding loaded config
    """
    
    try:
        # Get all parameters for this app
        param_details = client.get_parameter(
            Name=ssm_parameter_path,
            WithDecryption=True
        )

        configuration = param_details.get('Parameter', [])
        
    except:
        print("Encountered an error loading config from SSM.")
        traceback.print_exc()
    finally:
        return configuration["Value"]

def lambda_handler(event, context):

    URI = "/" + env + "/" + Database
    # MongoConnector = MongoClient(uri)

    config = load_config(URI)
    return { 
        'statusCode': 200,
        'body': json.dumps("Stagging Stage")
    }
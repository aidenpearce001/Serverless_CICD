from pymongo import MongoClient
import boto3 

client = boto3.client('ssm')

def load_config(ssm_parameter_path):
    """
    Load configparser from config stored in SSM Parameter Store
    :param ssm_parameter_path: Path to app config in SSM Parameter Store
    :return: ConfigParser holding loaded config
    """
    configuration = configparser.ConfigParser()
    try:
        # Get all parameters for this app
        param_details = client.get_parameters_by_path(
            Path=ssm_parameter_path,
            Recursive=False,
            WithDecryption=True
        )

        # Loop through the returned parameters and populate the ConfigParser
        if 'Parameters' in param_details and len(param_details.get('Parameters')) > 0:
            for param in param_details.get('Parameters'):
                param_path_array = param.get('Name').split("/")
                section_position = len(param_path_array) - 1
                section_name = param_path_array[section_position]
                config_values = json.loads(param.get('Value'))
                config_dict = {section_name: config_values}
                print("Found configuration: " + str(config_dict))
                configuration.read_dict(config_dict)

    except:
        print("Encountered an error loading config from SSM.")
        traceback.print_exc()
    finally:
        return configuration

def lambda_handler(event, context):

    # uri = "mongodb://" + MongoDBusername + ":" + MongoDBpassword + "@" + MongoDBaddress + "/" + MongoDBname
    # MongoConnector = MongoClient(uri)

    # pass

    config = load_config(full_config_path)
    return "MyApp config is " + str(config)
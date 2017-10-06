"""Dynamo Stream Class
"""

import configparser
import pkg_resources
import boto3

def get_kls_config(ini_path=None):
    """Gets pkg_resources for Class instances (in abscence of user preference)

    Args:
        - ini_path (str, optional): path to configuration file, if not set the
                                    default from the pkg_resources is used.

    Returns:
        configparser object
    """

    if (ini_path is None):
        ini_path = pkg_resources.resource_string('DustyPyManager.resources.stream', 'DynamoConnection.ini')

    config = configparser.ConfigParser()
    config.read_string(ini_path.decode('ascii'))

    return config


def test():
    
    conf = get_kls_config()
    region_name = conf['default']['region']

    client = boto3.client('dynamodb', region_name=region_name)

if __name__ == '__main__':
    test()
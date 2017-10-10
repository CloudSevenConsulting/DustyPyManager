"""Dynamo Stream Class
"""

import pkg_resources
import boto3

from DustyPyManager import configure

def test():
    
    conf = configure.get_config_resource('stream', 'DynamoConnection.ini')
    region_name = conf['default']['region']

    db = boto3.resource('dynamodb')
    table = db.Table('Movies')
    print(table.creation_date_time)

if __name__ == '__main__':
    test()
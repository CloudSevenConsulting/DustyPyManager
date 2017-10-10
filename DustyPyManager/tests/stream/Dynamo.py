"""Unit test for NM Sub-System/Stream-Dynamo unit of work
"""

import unittest
import boto3

from DustyPyManager import configure

def main():
    """Run the test
    """

    unittest.main()

class TestStreamDynamo(unittest.TestCase):
    """Test Case for Dynamo Stream Object
    """

    def __init__(self, *args, **kwargs):
        super(TestStreamDynamo, self).__init__(*args, **kwargs)

        self.conn_conf = configure.get_config_resource('stream', 'DynamoConnection.ini')

    def test_TU_NM_StreamDynamo_ClientObj_Op(self):
        """Test client object creation

        Pre-development test
        """

        db = boto3.resource('dynamodb')
        try:
            table = db.Table('Movies')
            print(table.creation_date_time)
        except ResourceNotFoundException:
            self.assertTrue(False)#Failed

        self.assertTrue(True)

if __name__ == '__main__':
    main()

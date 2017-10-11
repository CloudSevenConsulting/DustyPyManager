from __future__ import print_function # Python 2/3 compatibility
import boto3
import json
import decimal

# Helper class to convert a DynamoDB item to JSON.
class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            if o % 1 > 0:
                return float(o)
            else:
                return int(o)
        return super(DecimalEncoder, self).default(o)

dynamodb = boto3.resource('dynamodb', region_name='ap-southeast-1')

table = dynamodb.Table('NetworkData')

MoteID = 4
MoteTimestamp = "2016-10-06 0:00:00"

response = table.put_item(
Item={
'MoteID': MoteID,
'MoteTimestamp': MoteTimestamp,
'StockData': {
'OpenPrice':decimal.Decimal('29')
}
}
)

print("PutItem succeeded:")
print(json.dumps(response, indent=4, cls=DecimalEncoder))

import boto3

def test():
    
    client = boto3.client('dynamodb', region_name='ap-southeast-1')

if __name__ == '__main__':
    test()
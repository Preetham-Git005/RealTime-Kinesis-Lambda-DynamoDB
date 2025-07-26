import json
import base64
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('UserActions')

def lambda_handler(event, context):
    for record in event['Records']:
        # Decode base64 Kinesis data
        payload = base64.b64decode(record['kinesis']['data']).decode('utf-8')
        data = json.loads(payload)

        print("Decoded Record:", data)

        # Put item in DynamoDB
        response = table.put_item(
            Item={
                'username': data['username'],
                'timestamp': data['timestamp'],
                'action': data['action']
            }
        )

        print("DynamoDB PutItem response:", response)

    return {
        'statusCode': 200,
        'body': 'Processed successfully!'
    }
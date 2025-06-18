import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('MyDevOpsTable')

def lambda_handler(event, context):
    body = json.loads(event['body'])
    name = body.get('name', 'default')
    
    table.put_item(Item={'id': name})
    
    return {
        'statusCode': 200,
        'body': json.dumps({'message': f'Item {name} saved!'})
    }

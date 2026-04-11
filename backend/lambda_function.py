import json
import boto3

def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('visitor-counter')
    # Gets the table and update the counter
    response = table.update_item(
        # Updates the item
        Key={'id': 'visitors'},
        # Adds one to the count
        UpdateExpression='ADD #count :increment',
        # Maps a placeholder for the real attribute name, count
        ExpressionAttributeNames={'#count': 'count'},
        ExpressionAttributeValues={':increment': 1},
        # Updates and gets the value of counter
        ReturnValues="UPDATED_NEW"
    )

    # Gets the count from the response
    count = int(response['Attributes']['count'])

    return {
        'statusCode': 200,
        # Sets headers to allow cross-origin resource sharing (CORS)
        'headers': {
            'Access-Control-Allow-Origin': '*',
            'Content-Type': 'application/json'
        },
        'body': json.dumps({'count': count})
    }
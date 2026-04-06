import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('visitor-counter')

def lambda_handler(event, context):
    # Gets the table and update the counter
    response = table.update_item(
        # Updates the item
        Key={
            'id': 'visitors'
        },
        # Adds one to the count
        UpdateExpression='ADD count :increament',
        ExpressionAttributeValues={
            ':increament': 1
        }
    )

    # Gets the item from the table and prints it
    item = table.get_item(
        Key={
            'id': 'visitors'
        }
    )

    print(item['Item'])

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }

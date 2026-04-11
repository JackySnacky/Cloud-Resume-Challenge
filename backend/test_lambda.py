import boto3
import pytest
import os
from moto import mock_aws

import lambda_function
import json

@pytest.fixture
def aws_credentials():
    # Mocked AWS Credentials for moto.
    os.environ["AWS_ACCESS_KEY_ID"] = "testing"
    os.environ["AWS_SECRET_ACCESS_KEY"] = "testing"
    os.environ["AWS_SECURITY_TOKEN"] = "testing"
    os.environ["AWS_SESSION_TOKEN"] = "testing"
    os.environ["AWS_DEFAULT_REGION"] = "ca-west-1"

@pytest.fixture
def dynamodb(aws_credentials):
    with mock_aws():
        # Mocking DynamoDB
        db = boto3.resource("dynamodb", region_name="ca-west-1")
        # Creating table
        table = db.create_table(
            TableName="visitor-counter",
            # Creating the partition key and value
            KeySchema=[{
                'AttributeName': 'id',
                'KeyType': 'HASH'
            }],
            AttributeDefinitions=[{
                'AttributeName': 'id',
                'AttributeType': 'S'
            }],
            # Using pay pre request because DynamoDB want to provision capacity
            BillingMode='PAY_PER_REQUEST'
        )
        # put initial item into table
        table.put_item(Item={'id': 'visitors', 'count': 0})
        # yield will cleanup (teardown) the table
        yield table

def test_visitor_counter(dynamodb):
    # Calls the lambda_function handler from different file
    response = lambda_function.lambda_handler({},{})
    # check the response statusCode
    assert response['statusCode'] == 200
    # check the count incremented
    body = json.loads(response['body'])
    assert body['count'] == 1
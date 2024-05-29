import json
import boto3
from datetime import datetime

# Initialize AWS clients
dynamodb = boto3.resource('dynamodb')
sns = boto3.client('sns')

# Your DynamoDB table name
TABLE_NAME = 'YOUR_DYNAMODB_TABLE_NAME'

# Your SNS topic ARN
SNS_TOPIC_ARN = 'YOUR_SNS_TOPIC_ARN'

def lambda_handler(event, context):
    # Parse the incoming event data
    formData = json.loads(event['body'])

    # Prepare the data item for DynamoDB
    item = {
        'id': str(datetime.now().timestamp()),
        'name': formData['name'],
        'email': formData['email'],
        'message': formData['message'],
        'timestamp': datetime.now().isoformat()
    }

    # Insert the data item into DynamoDB
    table = dynamodb.Table(TABLE_NAME)
    try:
        table.put_item(Item=item)
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': 'Failed to write to DynamoDB', 'message': str(e)})
        }

    # Prepare the SNS message
    sns_message = f"Name: {formData['name']}\nEmail: {formData['email']}\nMessage: {formData['message']}"

    # Publish the message to SNS
    try:
        sns.publish(
            TopicArn=SNS_TOPIC_ARN,
            Subject='New Form Submission',
            Message=sns_message
        )
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': 'Failed to send SNS message', 'message': str(e)})
        }

    # Return a success response
    return {
        'statusCode': 200,
        'body': json.dumps({'message': 'Form submitted successfully'})
    }
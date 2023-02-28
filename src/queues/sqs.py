import boto3, os, json

queue_url = os.environ.get('SQS_SUBMISSION')
access_key = os.environ.get('ACCESS_KEY')
secret_key = os.environ.get('SECRET_KEY')

sqs_client = boto3.client('sqs', 
    region_name="eu-west-1",
    aws_access_key_id=access_key,
    aws_secret_access_key=secret_key)

def send_to_queue(payload):
    try:
        message = json.dumps(payload)
        response = sqs_client.send_message(
            QueueUrl=queue_url,
            MessageBody=message
        )
        return response
    
    except Exception as e:
        return f"Error sending SQS\n{e}"
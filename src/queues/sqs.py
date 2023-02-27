import boto3, os

queue_url = os.environ.get('SQS_SUBMISSION')
sqs = boto3.resource('sqs')

def send_to_queue(payload):
    response = sqs.send_message(
        QueueUrl=queue_url,
        MessageBody=payload
    )

    print(response['MessageId'])

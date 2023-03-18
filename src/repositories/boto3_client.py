import boto3
import os

access_key = os.environ.get('ACCESS_KEY')
secret_key = os.environ.get('SECRET_KEY')

dynamo_client = boto3.resource(
    service_name = 'dynamodb',
    region_name = 'eu-west-1',
    aws_access_key_id = access_key,
    aws_secret_access_key = secret_key)

exercise_table = dynamo_client.Table('Exercises')
submission_table = dynamo_client.Table('Submissions')
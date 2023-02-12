import boto3
import os

access_key = os.environ.get('ACCESS-KEY-TEST')
secret_key = os.environ.get('SECRET-KEY-TEST')

dynamo_client  =  boto3.resource(service_name = 'dynamodb',region_name = 'eu-west-1',
              aws_access_key_id = access_key,
              aws_secret_access_key = secret_key)


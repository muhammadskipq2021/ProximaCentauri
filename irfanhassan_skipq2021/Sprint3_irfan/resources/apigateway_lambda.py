import boto3
import os

def lambda_handler(event,context):
    value = dict()
    tablename = os.getenv('table_name')
    print(events)
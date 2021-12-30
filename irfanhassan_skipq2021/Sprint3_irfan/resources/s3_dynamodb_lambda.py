import boto3
import os
from s3bucket_read import s3bucket_read as bucket

def lambda_handler(event,context):
    value = dict()
    client = boto3.client('dynamodb')
    list_url=bucket().bucket_as_list()
    tablename = os.getenv('table_name')#getting table name
    for url in list_url:
        client.put_item(TableName= tablename,Item={'URL':{'S' : url}}) #putting url from json file to dynamoDB
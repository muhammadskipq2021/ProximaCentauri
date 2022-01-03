import datetime
import pytest
import requests
from resources import constants as constants_
import boto3

def test_apigateway():
    client = boto3.client('dynamodb')
    table_data = client.scan(TableName=constants_.url_table,AttributesToGet=['URL'])
    url_list=table_data["Items"]
    api_test = requests.put('https://hwmcjcc01f.execute-api.us-east-2.amazonaws.com/prod/',data = 'www.google.com')
    url_list2=dbscan.read_table(constants_.url_table)
    assert len(url_list1)==len(url_list2)-1
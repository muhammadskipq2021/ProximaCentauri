import datetime
import pytest
import requests
from resources import constants as constants_
from resources.tablescan import tablescan 


def test_apigateway():
    dbscan=tablescan()
    url_list1=dbscan.read_table(constants_.url_table)
    api_test = requests.put('https://hwmcjcc01f.execute-api.us-east-2.amazonaws.com/prod/',data = 'www.google.com')
    url_list2=dbscan.read_table(constants_.url_table)
    assert len(url_list1)==len(url_list2)-1
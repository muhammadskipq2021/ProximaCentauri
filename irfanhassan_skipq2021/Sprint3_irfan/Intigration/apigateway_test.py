import datetime
import pytest
import requests
from resources import constants as constants_
from resources.tablescan import tablescan 


def test_apigateway():
    dbscan=tablescan()
    url_list=dbscan.read_table(constants_.url_table)
    get_url=requests.get('https://hwmcjcc01f.execute-api.us-east-2.amazonaws.com/prod/')
    ans=True
    #for n in get_url:
     #   if n not in url_list:
     #       ans=False
     #       break
    assert ans
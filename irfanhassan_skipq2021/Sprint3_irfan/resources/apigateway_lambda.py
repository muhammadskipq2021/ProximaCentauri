import boto3
import os
import json
from tablescan import tablescan 
def lambda_handler(event,context):
    value = dict()
    dbscan=tablescan()
    client = boto3.client('dynamodb')
    #print(event)
    tablename = os.getenv('table_name')
    operation=event["httpMethod"]
    #print(operation)
    #print(url)
    response=""
    #https://dynobase.dev/dynamodb-python-with-boto3/#:~:text=To%20get%20all%20items%20from,the%20results%20in%20a%20loop
    if operation=="PUT":
        url=event['body']
        client.put_item(TableName= tablename,Item={'URL':{'S' : url}})
        response="The item has been successfully putted into DynamoDB table."
    elif operation=="DELETE":
        url=event['body']
        client.delete_item(TableName= tablename,Key={'URL':{'S' : url}}) #https://stackoverflow.com/questions/64187825/how-to-delete-all-the-items-in-the-dynamodb-with-boto3
        response="The item has been successfully deleted from DynamoDB table."
    elif operation=="GET":
        url_list=dbscan.read_table(tablename)
        response=url_list
    else:
        response="invalid request."
    
    return {'statusCode':200,'body':json.dumps(response)}   
    
    
    

        
        
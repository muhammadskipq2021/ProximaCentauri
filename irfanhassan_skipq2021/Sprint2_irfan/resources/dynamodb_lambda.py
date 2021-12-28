import boto3
import os
import json
import constants as constant_

def lambda_handler(event, context):
    print(event)
    client = boto3.client('dynamodb')
    
######### getiing timssetamp && message details fromm even(alarm)  #########################
    message = event['Records'][0]['Sns']['Message']
    msg = json.loads(message)  
    #reason = msg['NewStateReason']
    timestamp=message['Timestamp']
####### getting name of table ##############################################################
    
    tablename = os.environ['table_name']#getting table name
    print("--------------------")
    print(timestamp)
    print(tablename)
    #print(reason)
########### puuting Item in dynamo DB ####################################################3
    #client.put_item(tablename,Item={'Timestamp':{'S' : timestamp}, 'Reason':{'S':reason} })
        



    
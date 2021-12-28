import boto3
import os
import json
import constants as constant_

def lambda_handler(event, context):
    #print(eveny)
    client = boto3.client('dynamodb')
    
######### getiing timssetamp && message details fromm even(alarm)  #########################
    message = event['Records'][0]['Sns']
    msg = json.loads(message['Message'])   
    timestamp=message['Timestamp']
####### getting name of table ##############################################################
    
    tablename = os.getenv('table_name')#getting table name
    
########### puuting Item in dynamo DB ####################################################3
    client.put_item(tablename,
    Item={
              'Timestamp':{'S' : message['Timestamp']},
               'Reason':{'S':msg['NewStateReason']}
        }
    )
        



    
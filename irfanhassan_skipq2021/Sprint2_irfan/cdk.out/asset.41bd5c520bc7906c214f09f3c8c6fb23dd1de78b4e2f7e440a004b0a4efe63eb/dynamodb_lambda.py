import boto3
import json
import constants as constant_
client = boto3.client('dynamodb')

def lambda_handler(event, context):
    client = boto3.client('dynamodb')
    message = event['Records'][0]['Sns']
    msg = json.loads(message['Message'])
    timestamp=message['Timestamp']
    alarm=message['AlarmName']
    if alarm[0]=='B':
        client.put_item(TableName = "Beta-infraStack-TableCD117FA1-10BTARD7DGVYY",
        Item={
             'Timestamp':{'S' : message['Timestamp']},
              'Reason':{'S':msg['NewStateReason']
              }})
    else:
        client.put_item(TableName = "ProdStage-irfanskipqstack-irfanhassantable9BB9EE06-HSG5CFZS1QY0",
        Item={
              'Timestamp':{'S' : message['Timestamp']},
               'Reason':{'S':msg['NewStateReason']
               }})
    
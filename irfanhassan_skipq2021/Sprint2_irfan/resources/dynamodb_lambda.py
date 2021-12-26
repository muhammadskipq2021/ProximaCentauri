import boto3
import json
import constants as constant_
client = boto3.client('dynamodb')

def lambda_handler(event, context):
    #print(eveny)
    client = boto3.client('dynamodb')
    message = event['Records'][0]['Sns']
    msg = json.loads(message['Message'])
    timestamp=message['Timestamp']
    
    beta_table="BetaStag-irfanskipqstack-irfanhassantable1168CD430-1NNQHL0P7K3BG"
    prod_tabel="ProdStage-irfanskipqstack-irfanhassantable1168CD430-7BYYC0V4LAAG"
    Item={
              'Timestamp':{'S' : message['Timestamp']},
               'Reason':{'S':msg['NewStateReason']}
        }
    if msg['AlarmName'][0] == 'P':
        client.put_item(prod_tabel,Item)
        
    elif msg['AlarmName'][0] == 'B':
        client.put_item(beta_table,Item)


    
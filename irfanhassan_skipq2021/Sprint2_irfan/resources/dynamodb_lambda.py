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
    
    
  #  if msg['AlarmName'][0] == 'P':
  #      client.put_item(TableName = "ProdStage-irfanskipqstack-irfanhassantable9BB9EE06-K7N6HU3VLIWO",
  #      Item={
  #            'Timestamp':{'S' : message['Timestamp']},
  #             'Reason':{'S':msg['NewStateReason']
  #             }})
  #  elif msg['AlarmName'][0] == 'B':
  #      client.put_item(TableName = "BetaStag-irfanskipqstack-irfanhassantable9BB9EE06-Q9YQR7BPL0DL",
  #      Item={
  #           'Timestamp':{'S' : message['Timestamp']},
  #            'Reason':{'S':msg['NewStateReason']
  #            }})


    
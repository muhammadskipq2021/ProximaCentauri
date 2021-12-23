import boto3
import constants as constant_



def lambda_handler(event, context):
    db=boto3.resources('dynamodb')    
    Msg = event['Records'][0]['Sns']['MessageId'] #getting Alarm ID 
    Time = event['Records'][0]['Sns']['Timestamp'] #getting Alarm generation time
    T_name=constant_.table_name
    db.put_item(TableName =T_name,
    Item={     #writing the alarm id and time in dynamodb
        'MessageID':{'S':Msg},
        'TimeStamp':{'S':Time}
        }
    )
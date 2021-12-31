import boto3

class tablescan:
    def read_table(self,table_name):
        client = boto3.client('dynamodb')
        table_data = client.scan(TableName=table_name,AttributesToGet=['URL'])
        return table_data
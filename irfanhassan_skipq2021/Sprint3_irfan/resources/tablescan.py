import boto3

class tablescan:
    def read_table(self,table_name):
        client = boto3.client('dynamodb')
        table_data = client.scan(TableName=table_name,AttributesToGet=['URL'])
        url_list=table_data["Items"]
        for n in range(len(url_list)):
            url_list[n]=url_list[n]['URL']['S']
        return url_list
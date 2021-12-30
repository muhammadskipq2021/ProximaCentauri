from aws_cdk import (
    core as cdk,
    aws_lambda as lambda_,
    aws_events as event_,
    aws_events_targets as targets_,
    aws_cloudwatch as cloudwatch_,
    aws_iam,
    aws_lambda_event_sources as sources,
    aws_s3 as s3,
    aws_sns as sns,
    aws_sns_subscriptions as subsribe,
    aws_cloudwatch_actions as cw_actions,
    aws_dynamodb as db,
    aws_codedeploy as codedeploy,
    aws_apigateway as apigateway_
)
#from aws_cdk import aws_cloudwatch_actions as actions_
from resources import constants as constant_
from resources.s3bucket_read import s3bucket_read as bucket 

class Sprint3IrfanStack(cdk.Stack):

    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

########## #creating lambda roll and lambda for webhealth  ##########################################################################

        lambda_role = self.create_lambda_role()
    
############ #creating dynamo table to store URL  ###################################################################################
        url_lambda = self.create_lambda('urllammbda',"./resources",'s3_dynamodb_lambda.lambda_handler',db_lambda_role)
        url_table=self.create_table(id='irfanurltable', key=db.Attribute(name="URL", type=db.AttributeType.STRING))
        url_table.grant_full_access(url_lambda)
        url_lambda.add_environment('table_name', url_table.table_name)
        
####    adding s3bucket event to trigger url_labda       ##########################################################################
        bucket = s3.Bucket(self, "urls3bucket")
        url_lambda.add_event_source(sources.S3EventSource(bucket,events=[s3.EventType.OBJECT_CREATED],filters=[s3.NotificationKeyFilter(suffix=".json")]))

####### Adding API GateWay ##########################################################################################################
        apigateway_lambda=self.create_lambda('ApiGateWayLambda', './resources','apigateway_lambda.lambda_handler' ,db_lambda_role)
        apigateway_lambda.add_environment('table_name', url_table.table_name)
        url_table.grant_full_access(apigateway_lambda)
        url_table.grant_full_access(webhealth_lambda)
        #https://docs.aws.amazon.com/cdk/api/v1/python/aws_cdk.aws_apigateway/README.html
        api = apigateway.LambdaRestApi(self, "myapi",handler=backend) #REST API
        items = api.root.add_resource("items")
        items.add_method("GET") # GET items
        items.add_method("PUT") # PUT items
        items.add_method("DELETE") # PUT items
        
        
    ###### Periodic web health lambda ###############################################################################################
        
   #    hi_lamda = self.create_lambda('heloHellammbda',"./resources",'lambda.lambda_handler',lambda_role)
        webhealth_lambda = self.create_lambda('FirstHellammbda',"./resources",'Monitor_webhealth.lambda_handler',lambda_role)
        lambda_schedule = event_.Schedule.rate(cdk.Duration.minutes(1))
        lambda_target = targets_.LambdaFunction(handler = webhealth_lambda)
        our_rule = event_.Rule(self, id = "MonitorwebHealth",enabled = True, schedule= lambda_schedule,targets =[lambda_target])
                
############ #creating dynamodb table to store alarm ################################################################################

        dynamo_table=self.create_table(id='irfanhassantable', key=db.Attribute(name="Timestamp", type=db.AttributeType.STRING))
        db_lambda_role = self.create_db_lambda_role()
        db_lamda = self.create_lambda('secondHellammbda',"./resources/",'Monitor_webhealth.lambda_handler',db_lambda_role)
        dynamo_table.grant_full_access(db_lamda)
        db_lamda.add_environment('table_name', dynamo_table.table_name)
        

        
############# #adding SNS topic and adding dynao db lambda and myself as subscribe to sns topic using my email address #############

#creating lambda role function to give all access to lambda
    def create_lambda_role(self):
        lambda_role = aws_iam.Role(self, "lambda-role", 
        assumed_by = aws_iam.ServicePrincipal('lambda.amazonaws.com'),
        managed_policies = [
            aws_iam.ManagedPolicy.from_aws_managed_policy_name('service-role/AWSlambdaBasicExecutionRole'),
            aws_iam.ManagedPolicy.from_aws_managed_policy_name('CloudWatchFullAccess')
            ]
        )
        return lambda_role
  
        
#creating lambda handler    
    def create_lambda(self,id, asset, handler,role):
        return lambda_.Function(self, id,
        code = lambda_.Code.from_asset(asset),
        handler=handler,
        runtime= lambda_.Runtime.PYTHON_3_6,
        role=role
        )
    #### adding policy for dynamo db lambda to give it fullaccess
    def create_db_lambda_role(self):
        lambdaRole = aws_iam.Role(self, "lambda-role-db",
                        assumed_by = aws_iam.ServicePrincipal('lambda.amazonaws.com'),
                        managed_policies=[
                            aws_iam.ManagedPolicy.from_aws_managed_policy_name('service-role/AWSLambdaBasicExecutionRole'),
                            aws_iam.ManagedPolicy.from_aws_managed_policy_name('AmazonDynamoDBFullAccess'),
                            aws_iam.ManagedPolicy.from_aws_managed_policy_name('AmazonSNSFullAccess'),
                            aws_iam.ManagedPolicy.from_aws_managed_policy_name('AmazonS3FullAccess')
                        ])
        return lambdaRole
#creating dynamo table 
    def create_table(self,id,key):
        return db.Table(self,id,
        partition_key=key)
        #finish
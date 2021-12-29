from aws_cdk import (
    core as cdk,
    aws_lambda as lambda_,
    aws_events as event_,
    aws_events_targets as targets_,
    aws_cloudwatch as cloudwatch_,
    aws_iam,
    aws_sns as sns,
    aws_sns_subscriptions as subsribe,
    aws_cloudwatch_actions as cw_actions,
    aws_dynamodb as db,
    aws_codedeploy as codedeploy
)
#from aws_cdk import aws_cloudwatch_actions as actions_
from resources import constants as constant_
from resources.s3bucket_to_dynamoDB import s3bucket_to_dynamoDB as S3_db

class Sprint3IrfanStack(cdk.Stack):

    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

########## #creating lambda roll and lambda for webhealth  ####################################################################

        lambda_role = self.create_lambda_role()
    #    hi_lamda = self.create_lambda('heloHellammbda',"./resources",'lambda.lambda_handler',lambda_role)
        webhealth_lambda = self.create_lambda('WebHealthlammbda',"./resources",'Monitor_webhealth.lambda_handler',lambda_role)
        lambda_schedule = event_.Schedule.rate(cdk.Duration.minutes(1))
        lambda_target = targets_.LambdaFunction(handler = webhealth_lambda)
        our_rule = event_.Rule(self, id = "MonitorwebHealth",enabled = True, schedule= lambda_schedule,targets =[lambda_target])
                
############ #creating dynamodb table  for storing alarm data#############################################################

        dynamo_table=self.create_table(id='irfanhassantable', key=db.Attribute(name="Timestamp", type=db.AttributeType.STRING))
        db_lambda_role = self.create_lambda_role()
        db_lambda = self.create_lambda('DynaoDBlammbda',"./resources/",'dynamodb_lambda.lambda_handler',db_lambda_role)
        dynamo_table.grant_full_access(db_lambda)

        db_lambda.add_environment('table_name', dynamo_table.table_name)
        
############ #creating dynamodb table to stor URLs of webpags#############################################################

        url_table=self.create_table(id='irfanhassantable', key=db.Attribute(name="Timestamp", type=db.AttributeType.STRING))
        S3_db().bucket_to_dynamoDB(url_table.table_name)
        
############# #adding SNS topic and adding dynao db lambda and myself as subscribe to sns topic using my email address #############
        
    #    sns_topic = sns.Topic(self, 'WebHealth')
    #    sns_topic.add_subscription(subsribe.LambdaSubscription(fn = db_lamda))
    #    sns_topic.add_subscription(subsribe.EmailSubscription("muhammad.irfan.hassan.s@skipq.org"))
        

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
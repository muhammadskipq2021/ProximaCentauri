# ProximaCentauri Sprint2
# Continuous integration and delivery (CI/CD) using CDK Pipelines

## Table of contents
* [Project Description](#Project-Description)
* [Technologies](#technologies)
* [Setup](#setup)


## Project Description
This aim of this project is to create multi-stage pipeline having Beta and Prod stage using CDK. pipeline will get webHealth monitor application'source code from github repository and will automate the process of building, testing and deploying application. If we add new stacks/stage or update anything in application, the pipeline automatically reconfigures itself to deploy those new stages and stacks. 

## Technologies 
Project is created with 
* Lambda
* CloudWatch
* DynamoDB
* SNS
* Cloud9
* S3
* CodePipeline
* Secret Manager
* CloudFormation

## SetUp
To run this project, follow these steps 
### Environment creation on AWS
First of all login in aws.amazon and create a virtual machine and install all requirements.
### Store Personal access tokens 
To get access to github repository , you have to generate Personal access tokens and then store Personal access tokens in AWS Secret Manager.
### Setup Source
At the beginning of the project it's essentil to setup the source. Store the code in your github respository. Add the github repository path in Source of pipeline stack.
### Bootstrap your AWS environments
Before you can use CDK Pipelines, you must bootstrap the AWS environment(s) to which you will deploy your stacks. An environment is an account/region pair to which you want to deploy a CDK stack. Add the Acount ID, Region , qualifier name (of your choice) and toolkit name (of your choice) in the command and run this command in terminal to boostrap the AWS enviroment.
`
$ cdk bootstrap aws://<Acount ID>/<Region> --qualifier <name> --toolkit-stack-name <name>
`

### install requirements 
copy the files and update file in CDK project file. 
``````
$ python -m pip install aws-cdk.core==1.135.0
$ pip install -r requirements.txt
$ nvm install v16.3.0 && nvm use 16.3.0 && nvm alias default v16.3.0
$ npm install -g aws-cdk
$ export PATH=$PATH:$(npm get prefix)/bin
$ pip install aws-cdk.aws-s3 aws-cdk.aws-lambda
$ pip install aws-cdk.aws_cloudwatch_actions==1.135.0
$ pip isntall boto3
``````
now all required requirements are done on machine. 
### Test Code
To test code run these commands
``
$ cdk synth
$ cdk deploy
``
if there is no error you can see the graphs of latency and availability on cludwatch and also you will get notification email when there is alarm trigger.  


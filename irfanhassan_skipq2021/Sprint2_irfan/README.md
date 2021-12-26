# ProximaCentauri Sprint2
# Continuous integration and delivery (CI/CD) using CDK Pipelines

## Table of contents
* [Project Description](#Project-Description)
* [Technologies](#technologies)
* [Setup](#setup)


## Project Description
As DeveOps I create multi-stage pipeline having Beta and Prod stage using CDK. I setup the source from my Github repositroy for Pipeline. pipeline will get webHealth monitor application'source code from github repository and will automate the process of building, testing and deploying application. First it install requirements for source code and then synth the code. I added Beta stage where it run unit test and intigration test and then deploy the source code. After then I added Prostage which get mannual approval then deploy the source code. When add new stacks/stage or update anything in application, the pipeline automatically reconfigures itself to deploy those new stages and stacks. 

## Technologies 
Project is created with follwoing AWS services
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
* ###  Environment creation on AWS
First of all login in aws.amazon and create a virtual machine and install all requirements.
* ### Store Personal access tokens 
To get access to github repository , you have to generate Personal access tokens and then store Personal access tokens in AWS Secret Manager.
* ### Setup Source
At the beginning of the project it's essentil to setup the source. Store the code in your github respository. Add the github repository path in Source of pipeline stack.
* ### Bootstrap your AWS environments
Before you can use CDK Pipelines, you must bootstrap the AWS environment(s) to which you will deploy your stacks. An environment is an account/region pair to which you want to deploy a CDK stack. Add the Acount ID, Region , qualifier name (of your choice) and toolkit name (of your choice) in the command and run this command in terminal to boostrap the AWS enviroment.
```
$ cdk bootstrap aws://<Acount ID>/<Region> --qualifier <name> --toolkit-stack-name <name>
```
make sure to add your quaifier name in cdk.json file. add qualifier name in this follwing form.
```
"@aws-cdk/core:bootstrapQualifier": "<qualifier name>"
```
* ### Deploy Pipeline 
Once the envirement is boostrap successfully then deploy the pipeline stack using this command. use your pipeline stack name instead of pipelinestack  
```
$ cdk deploy pipelinestack
```
now all required requirements are done on machine. 
* ### CodePipeline
To check that your CDK pipeline is created successfully open CodePipeline and observe your pipeline stack. 
* ### observe Result
When pipeline is comleted successfully then open cloudwatch to observe the webhealth of URLs and then check Email and dynamodb Tables to observed the alarma notifications.
####Author
Muhammad Irfan Hassan 
Trainee @skipQ 
muhammad.irfan.hassan.s@skipq.org

Thanks! Enjoy:)

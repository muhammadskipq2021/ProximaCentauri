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

## SetUp
To run this project, follow these steps 
### Environment creation on AWS
First of all login in aws.amazon and create a virtual machine. 
### Update Python and AWS 
check version of python and if it is old version check new version is available then make new version as default version using these commands.
 ```
 $ python --version
 $ python3 --version
 $ source ~/.bashrc
 ```
 then add this line in bashrc file
```
$alis python='/usr/bin/python3' (press ESC on keybaord)
$:w! (press Enter on keybaord)
$:q! (press Enter on keybaord) 
```
check version of aws and then update it to new version using these commands.
````
$ aws --version 
$ curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
$ unzip awscliv2.zip
$ sudo ./aws/install
````
### Create CDK project 
create directory of your choice and change directory to new created and then create cdk project using these commands. 
```
$ mkdir IrfanskipQ_Project1
$ cd IrfanskipQ_Project1
$ cdk init app --language python
```

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


# ProximaCentauri Sprint5
# API Test Client for CRUD API Gateway using Pyresttest and Syntribos 

## Table of contents
* [Project Description](#Project-Description)
* [Technologies](#technologies)
* [Setup](#setup)


## Project Description
Create API test client using Pyresttest and Syntribos to exercise the CRUD API Gateway operations 
(GET, PUT AND DELETE). Build images using Docker and push build images to Elastic Container 
Registry (ECR). Pull and deploy images using Pipeline and send test data to Cloud watch metrics 
and add alarm to metrics. 
  

## Technologies 
Project is created with follwoing AWS services
* Docker 
* AWS ECR 
* AWS ECS 
* PyRestTest 
* Syntribos 


## SetUp
To run this project, follow these steps 
* ###  Install requirements
First Install Visual Studio, Python, Docker Desktop, and AWS CLI on your PC/Laptop. 
* ### Create API test Client and build images
Open cmd and create a directory using this command and change the directory to that 
directory. 
```
$ mkdir example-project
$ cd example-project 
```
Create a new file with the name Dockerfile and write code. 
Create a new file prettiest.yaml and add code to it for your test. 
Now open cmd and run this command to build a docker image from a docker file using 
this command.
```
$docker build -t image-name . 
```
Check image is created by using this command 
```
$docker images
```
If your image is there then run the image using the below command. 
```
$docker run -rm image-name <URL-API> <YAMLFILE>
```
If the image is running successfully then move onward. 
* ### Create Repositry in ECR and push images
Create an ECR repository and set the name as your image name. 
Create IAM user and add policy and save excel file having AWS access key ID and AWS 
access key. Then run this command in cmd to configure AWS.
```
$aws configure
```
And give access key ID and Access key and then give other things accordingly to your 
account and requirements. 
Go into your ECR repo and click on the option push command. There will be 4 commands. 
Run all commands one by one and your image will be pushed to ECR. 

* ### Clone Local Machine to Github repository
To clone the github repository to local machine run this command
```
$ git clone <github repository url>
```
Then chnage directory to your project folder using this command.
```
$ cd <projectfolder path>
```
if you add any thing to project then commit and push code to github repo using these command. 
 ```
 $ git status
 $ git add .
 $ git commit -m "updated file"
 $git push
 ```
* ### Bootstrap your AWS environments
Before deploying CDK Pipelines, you must bootstrap the AWS environment. An environment is an account/region pair where you want to deploy a CDK stack. Add the Account ID, Region, qualifier name (of your choice), and toolkit name (of your choice) in the command and run this command in the terminal to bootstrap the AWS environment.
```
$ cdk bootstrap aws://<Acount ID>/<Region> --qualifier <name> --toolkit-stack-name <name>
```
Make sure to add your qualifier name in the cdk.json file, add the qualifier name in the following form.
```
"@aws-cdk/core:bootstrapQualifier": "<qualifier name>"
```
* ### Deploy Pipeline 
Once the environment is bootstrap successfully, deploy the pipeline stack using this command. use your pipeline stack name instead of pipeline stack  
```
$ cdk deploy pipelinestack
```

### Author
Muhammad Irfan Hassan Trainee @skipQ  muhammad.irfan.hassan.s@skipq.org

Thanks! Enjoy:)

# AWS Playground

The integrations below are different AWS integrations/architectures that I have learned

## Lambda-SQS

An introduction to SQS Standard Queues using a Python based Lambda function to populate the queue using boto3 SDK. The lambda function is connected to the SQS queue with basic permissions in its resource policy that allow for CRUD message operations.

## Lambda-API Gateway REST API

Constructed a REST-API using API Gateway and a Lambda function as a trigger. This is a proxied integration meaning all requests to the designated endpoint in API Gateway will be forwarded to one Lambda function and the Lambda function is responsible for parsing the event contents to output the desired behavior. Utilizes Python to produce the responses.

## DynamoDB-Lambda-API Gateway CRUD REST API

Designed a REST-API using API Gateway and a Lambda function as a trigger like the example above. However, this time I used the boto3 SDK to perform various CRUD operations on a DynamoDB table. 

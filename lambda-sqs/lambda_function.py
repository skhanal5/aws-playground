import json
import boto3

def lambda_handler(event, context):
    
    # initialize sqs instance
    sqs = boto3.resource('sqs')
    
    # use existing queue by name
    client = sqs.get_queue_by_name(QueueName='standard')
    
    # all events passed into this lambda have a "action" field and additional 
    # fields if necessary
    
    if event["action"] == "send":
        response = client.send_message(
            MessageBody=event["message"],
        )
        return {
            'statusCode': 200,
            'body': 'Invoked send',
            'response': response
        }   
        
    elif event["action"] == "delete":
        response = client.delete_messages(
            Entries = [ {
                'Id': "sampleid123456",
                'ReceiptHandle': event["receiptHandle"]    
            }
            ]
        )

        return {
            'statusCode': 200,
            'body': 'Invoked delete',
            'response': response
        }
        
    elif event["action"] == "receive":
        response = client.receive_messages(
            AttributeNames = ['All'],
            MaxNumberOfMessages = 1,
        )
        
        return {
            'statusCode': 200,
            'body': 'Invoked receive',
            'message-contents': response[0].body if len(response) == 1 else "",
            'attributes': response[0].attributes if len(response) == 1 else "",
            'other-data': json.dumps(response,default=str)
        }
        
    elif event["action"] == "change":
        response = client.change_message_visibility_batch(
            Entries = [ {
                'Id': "sampleid123456",
                'ReceiptHandle': event["receiptHandle"], 
                'VisibilityTimeout': event["timeout"]
            }
            ]
        )
        
        return {
            'statusCode': 200,
            'body': 'Invoked change visibility timeout',
            'response': response
        }
        
    return {
        'statusCode': 200,
        'body': json.dumps('Default response for testing purposes')
    }

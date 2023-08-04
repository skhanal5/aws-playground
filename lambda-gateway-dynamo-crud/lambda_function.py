import json
import boto3

def lambda_handler(event, context):
    
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('crud')
    body = ""
       
    method = event['requestContext']['http']['method']
  
    
    if method == "GET":
        id = event['pathParameters']['id']
        response = table.get_item(
            Key={
                'id': id
            }
        )
        body = response['Item']
        
    elif method == "POST":
        id = event['queryStringParameters']['id']
        price = event['queryStringParameters']['price']
        quantity = event['queryStringParameters']['quantity']
        table.put_item(
            Item={
                'id': id,
                'price': price,
                'quantity': quantity,
            }   
        )
        body = f"Added {id} with price: {price} and quantity: {quantity} to the table."

    elif method == "PUT":
        id = event['pathParameters']['id']
        price = event['queryStringParameters']['price']
        quantity = event['queryStringParameters']['quantity']
        
        table.update_item(
            Key={
                'id': id,
            },
            UpdateExpression='SET price = :field1, quantity = :field2',
            ExpressionAttributeValues={
                ':field1': price,
                ':field2': quantity,
            }
        )
        body = f"Updated {id} with price: {price} and quantity: {quantity} to the table."
        
    elif method == "DELETE":
        id = event['pathParameters']['id']
        
        table.delete_item(
            Key={
                'id': id
            }
        )
        body = f"Deleted {id} from the table"
        
   
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps(body)
    }
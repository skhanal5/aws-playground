import json

def lambda_handler(event, context):
    
    method = event['requestContext']['http']['method']
    route = event['requestContext']['http']['path']
    message = ""
    params = "" if "queryStringParameters" not in event else event['queryStringParameters']
    data = ""

    # Using proxy based integration -> handle routes manually
    if method == "GET":
        message = f"Received {method} request on route {route}"
        data = f"Simulating {params} being retrieved"
    elif method == "POST":
        message = f"Received {method} request on route {route}"
        data = f"Simulating {params} being sent"
    elif method == "DELETE":
        message = f"Received {method} request on route {route}"
        data = f"Simulating {params} being deleted"
    elif method == "PUT":
        message = f"Received {method} request on route {route}"
        data = f"Simulating {params} being inserted"
    
    input = f"Here is the input data that was passed for testing {params}"
    
    body = {
        'message': message,
        'data': data,
        'input': input
    }
    
    return {
        'statusCode': 200,
        'body': json.dumps(body),
    }
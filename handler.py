import json

def hello(event, context):
    return {
        "statusCode": 200,
        "body": json.dumps("Hello, world!"),
    }

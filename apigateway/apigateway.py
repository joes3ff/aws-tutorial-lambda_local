def lambda_handler(event, context):
    return event.get("queryStringParameters", {}).get("foo")


#sam local invoke -e ./apigateway/apigateway_event.json ApiGatewayFunction
#sam local start-api

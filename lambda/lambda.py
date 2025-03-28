
def lambda_handler(event, context):
    return event.get("data")

#sam local invoke -e ./lambda/lambda_event.json LambdaDemoFunction  
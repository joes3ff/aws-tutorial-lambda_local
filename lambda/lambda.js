
exports.lambdaHandler = async (event, context) => {
    return event.data;
};

// demo push

//sam local invoke -e ./lambda/lambda_event.json LambdaDemoFunction  
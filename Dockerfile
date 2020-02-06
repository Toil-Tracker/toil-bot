FROM node:10



RUN npm install serverless -g

## RUN serverless install -u https://github.com/serverless/examples/tree/master/aws-python-rest-api-with-dynamodb -n  aws-python-rest-api-with-dynamodb
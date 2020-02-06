import json
import logging
import os
import time
import uuid
import ast
from urllib import parse
from datetime import datetime

import boto3
dynamodb = boto3.resource('dynamodb')


def create(event, context):
    print("Event obj: {}".format(json.dumps(event)))

    domainName = json.dumps(event["requestContext"]["domainName"])
    path = json.dumps(event["requestContext"]["path"])
    queryStringParams = json.dumps(event["body"])
    url = "https://{}{}?{}".format(ast.literal_eval(domainName), ast.literal_eval(path), ast.literal_eval(queryStringParams))
    print(url)
    parsed_url = parse.urlsplit(url)
    print(parsed_url)
    qsp_dict = dict(parse.parse_qsl(parse.urlsplit(url).query))
    print(json.dumps(qsp_dict))

    timestamp = str(datetime.utcnow().isoformat())

    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])

    item = {
        'id': str(uuid.uuid1()),
        'text': qsp_dict['text'],
        'checked': False,
        'createdAt': timestamp,
        'updatedAt': timestamp,
    }

    # write the todo to the database
    table.put_item(Item=item)

    # create a response
    response = {
        "statusCode": 200,
        "body": json.dumps(item)
    }

    return response

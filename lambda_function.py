import json
import random
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def fetchdata():
    data = ['1','2','3','4']
    return random.choice(data)


def lambda_handler(event, context):
    logger.info("Event data: %s", event)
    data=fetchdata()
    message=f"my new number {data}"
    response_dict = {'statusCode': 200,'body': json.dumps({"message":message})}
    logger.info("Response data: %s", response_dict)
    return response_dict
import datetime as dt
import uuid
from typing import Any, Dict, Optional, List, Tuple

import boto3

from rabbit_manager.model.rabbit import Rabbit

ddb = boto3.resource('dynamodb')
table_name = 'RabbitManager'
table = ddb.Table(table_name)


def create_rabbit(rabbit: Rabbit) -> None:
    rabbit.id = str(uuid.uuid4())
    rabbit.birth_date = dt.datetime.now().date()
    rabbit.validate(nullable=False)
    rabbit_item = rabbit.to_dict()
    table.put_item(Item=rabbit_item)


def list_rabbits(last_key=None) -> Tuple[List[Rabbit], Optional[str]]:
    if last_key is None:
        response = table.scan()
    else:
        response = table.scan(ExclusiveStartKey=last_key)
    rabbit_list = [
        Rabbit.from_dict(item)
        for item in response['Items']
    ]
    last_key = None
    if 'LastEvaluatedKey' in response:
        last_key = response['LastEvaluatedKey']
    return rabbit_list, last_key


def get_rabbit_by_id(rabbit_id: str) -> Optional[Rabbit]:
    response = table.get_item(Key={
        'id': rabbit_id
    })
    if 'Item' not in response:
        return None
    item = response['Item']
    return Rabbit.from_dict(item)


def update_rabbit_by_id(rabbit_id: str, rabbit: Rabbit) -> None:
    rabbit_item: Dict[str, Any] = rabbit.to_dict()
    rabbit_update: Dict[str, Dict[str, Any]] = {
        key: {'Value': rabbit_item[key]}
        for key in rabbit_item
    }
    table.update_item(
        Key={
            'id': rabbit_id,
        },
        AttributeUpdates=rabbit_update,
        Expected={
            'id': {
                'Value': rabbit_id,
                'Exists': True,
            }
        },
    )


def delete_rabbit_by_id(rabbit_id: str) -> None:
    table.delete_item(
        Key={
            'id': rabbit_id,
        },
    )

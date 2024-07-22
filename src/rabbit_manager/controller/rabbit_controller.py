import json
from typing import Any, Dict

from rabbit_manager.model.rabbit import Rabbit
from rabbit_manager.service import rabbit_service


def get_rabbits() -> Dict[str, Any]:
    rabbit_list, last_key = rabbit_service.list_rabbits()
    response_body = {
        'rabbits': [
            rabbit.to_dict()
            for rabbit in rabbit_list
        ],
    }
    if last_key is not None:
        response_body['lastKey'] = last_key
    return {
        'statusCode': 200,
        'body': json.dumps(response_body, indent=2)
    }


def post_rabbits(request_body) -> Dict[str, Any]:
    rabbit = Rabbit.from_dict(request_body, request=True)
    rabbit_service.create_rabbit(rabbit)
    return {
        'statusCode': 201,  # Created.
    }


def get_rabbit_by_id(rabbit_id) -> Dict[str, Any]:
    rabbit = rabbit_service.get_rabbit_by_id(rabbit_id)
    if rabbit is None:
        return {
            'statusCode': 404,
        }
    response_body = rabbit.to_dict()
    return {
        'statusCode': 200,
        'body': json.dumps(response_body, indent=2)
    }


def post_rabbit_by_id(rabbit_id, request_body) -> Dict[str, Any]:
    rabbit = Rabbit.from_dict(request_body, request=True)
    rabbit_service.update_rabbit_by_id(rabbit_id, rabbit)
    return {
        'statusCode': 200,
    }


def delete_rabbit_by_id(rabbit_id) -> Dict[str, Any]:
    rabbit_service.delete_rabbit_by_id(rabbit_id)
    return {
        'statusCode': 204,  # No Content.
    }

import json
from typing import Any, Dict

from rabbit_manager.controller import rabbit_controller
from rabbit_manager.utils import common_utils


def lambda_handler(event, context) -> Dict[str, Any]:
    request_context = event['requestContext']
    resource_path = request_context['resourcePath']
    http_method = request_context['httpMethod']
    request_body = ''

    # Loads request body if the HTTP method is POST.
    if http_method == 'POST':
        try:
            request_body = json.loads(event['body'])
        except RuntimeError:
            pass

    if resource_path == '/rabbits':
        if http_method == 'GET':
            return rabbit_controller.get_rabbits()
        elif http_method == 'POST':
            common_utils.validate_type(request_body, dict)
            return rabbit_controller.post_rabbits(request_body)
        else:
            return {
                'statusCode': 405,  # Method Not Allowed.
            }
    elif resource_path == '/rabbits/{rabbitId+}':
        rabbit_id = event['pathParameters']['rabbitId']
        if http_method == 'GET':
            return rabbit_controller.get_rabbit_by_id(rabbit_id)
        elif http_method == 'POST':
            common_utils.validate_type(request_body, dict)
            return rabbit_controller.post_rabbit_by_id(rabbit_id, request_body)
        elif http_method == "DELETE":
            return rabbit_controller.delete_rabbit_by_id(rabbit_id)
        else:
            return {
                'statusCode': 405,  # Method Not Allowed.
            }
    else:
        return {
            'statusCode': 403,  # Forbidden.
        }

import json
import requests


def isitdown(event, context):
    hostname = event.get('pathParameters', {}).get('url')
    status_code = None
    isitdown = False
    try:
        status_code = requests.get(f'http://{hostname}').status_code
    except requests.ConnectionError:
        isitdown = True
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json',
        },
        'body': json.dumps({
            'host': hostname,
            'isitdown': isitdown,
            'status_code': status_code
        }),
    }

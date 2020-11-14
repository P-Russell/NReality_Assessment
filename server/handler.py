import json
import xmltodict
from urllib.request import Request, urlopen
from urllib.error import HTTPError
from os import environ
import boto3
from botocore.exceptions import ClientError


dynamodb = boto3.resource('dynamodb', region_name=environ['REGION'])
table = dynamodb.Table(environ['DYNAMODB_TABLE'])

github_url = 'https://github.com'

def feed(event, context):
    try: 
        github_handle =  event['pathParameters']['handle']
        req = Request( github_url + '/' + github_handle)
        req.add_header('Accept', 'application/atom+xml')

        content = urlopen(req).read()

        parsed_content = xmltodict.parse(content)

        response = table.get_item(Key = {'github_handle': github_handle})
        if 'Item' not in response:
            table.put_item(Item={
                'github_handle': github_handle,
                'read_later': []
            })
        else:
            for id in response['Item']['read_later']:
                # Perfrom some filtering



        # try:
        #     print('Found ITEM')
        #     print(query['Item'])
        # except ClientError as e:
        #     print(e.response['Error']['Code'])

        # except dynamodb.Client.exceptions.ResourceNotFoundException as e:
        #     print('Createing new entry')
        #     table.put_item(Item={
        #         'github_handle': github_handle,
        #         'read_later': []
        #     })



        return {
            'statusCode': 200,
            'body': json.dumps(parsed_content['feed']['entry'])
        }

    except HTTPError as e:
        return {
            'statusCode': e.code,
            'reason': e.reason,
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': 'internal server error'
        }


def read_later(event, context):
    '''
    y
    '''
    ad_id = event['body']['id']
    user_handel = event['body']['id']

    body = {
        'message': 'Go Serverless v1.0! Your function executed successfully!',
        'input': event
    }

    response = {
        'statusCode': 200,
        'body': json.dumps(body)
    }

    return response

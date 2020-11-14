import xmltodict
from urllib.request import Request, urlopen
import boto3
from os import environ


dynamodb = boto3.resource('dynamodb', region_name=environ['REGION'])
table = dynamodb.Table(environ['DYNAMODB_TABLE'])


def fetch_github_feed_entries(github_handle):
    req = Request('https://github.com/' + github_handle)
    req.add_header('Accept', 'application/atom+xml')
    content = urlopen(req).read()
    parsed_content = xmltodict.parse(content)
    return parsed_content['feed']['entry']


def create_table_entry(github_handle):
    table.put_item(Item={
        github_handle: github_handle,
        read_later: []
    })


def fetch_read_later_list(github_handle):
    res = table.get_item(Key = {'github_handle': github_handle})
    if 'Item' not in res:
        return None
    return res['Item']['read_later']


def add_to_read_later_list(github_handle, entry_id):
    response = table.get_item(Key = {'github_handle': github_handle})
    item = response['Item']
    item['read_later'].append(entry_id)
    table.put_item(Item=item)


def response_entries(all_entries, read_later, include_read_later):
    if include_read_later:
        return list(filter(lambda entry : entry['id'] in read_later, all_entries))
    else:
        return list(filter(lambda entry : not (entry['id'] in read_later), all_entries))
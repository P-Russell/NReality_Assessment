import json
from urllib.error import HTTPError
from botocore.exceptions import ClientError
from helpers import *
import logging


def feed(event, context):
    try:
        post_body = json.loads(event['body'])
        github_handle = post_body['handle'].lower()
        show_read_later = post_body['read_later']

        all_entries = fetch_github_feed_entries(github_handle)
        read_later_list = fetch_read_later_list(github_handle)

        if type(read_later_list) == list:
            entries = response_entries(
                all_entries, read_later_list, show_read_later)
        else:
            create_table_entry(github_handle)
            entries = all_entries

        return response(code=200, body=entries)

    except HTTPError as e:
        logging.error(e)
        return response(code=e.code, body=e.reason)
    except Exception as e:
        logging.error(e)
        return response(code=500, body='internal server error')


def read_later(event, context):
    try:
        post_body = json.loads(event['body'])
        github_handle = post_body['handle'].lower()
        entry_id = post_body['entry_id']

        add_to_read_later_list(github_handle, entry_id)

        return response(code=200, body=entry_id)
    except Exception as e:
        logging.error(e)
        return response(code=500, body='internal server error')

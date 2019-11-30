import json
import sys
from typing import Text

import requests
from data_readers import get_page_access_token


def add_get_started_button(intent_name: Text):
    """
    Function setting "Get_Started" button on a Messenger welcome screen for a new users.
    :param intent_name: intent which will be triggered after clicking "get_started" button
    """
    page_access_token = get_page_access_token()
    url = "https://graph.facebook.com/v2.6/me/messenger_profile?access_token="
    headers = {"Content-Type": "application/json"}
    data = {"get_started": {"payload": "/" + intent_name}}
    data = json.dumps(data)
    r = requests.post(url=url+page_access_token, data=data, headers=headers)
    if r.json()['result'] == 'success':
        print("Successfully added get_started button with '{}' intent.".format(intent_name))


if __name__ == '__main__':
    if len(sys.argv) == 2:
        intent = sys.argv[1]
        add_get_started_button(intent)
    else:
        print("Usage: python3 add_get_started_button.py intent_name")
        print("Example: python3 add_get_started_button.py menu")

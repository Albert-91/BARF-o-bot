import json
import sys
from typing import Text

import requests
from data_readers import get_facebook_token_from_credentials


def add_get_started_button(intent_name: Text, credential_file_path: Text):
    """
    Function setting "Get_Started" button on a Messenger welcome screen for a new users.
    :param credential_file_path: Rasa file with Facebook credentials
    :param intent_name: intent which will be triggered after clicking "get_started" button
    """
    page_access_token = get_facebook_token_from_credentials(credential_file_path)
    url = "https://graph.facebook.com/v2.6/me/messenger_profile?access_token="
    headers = {"Content-Type": "application/json"}
    data = {"get_started": {"payload": "/" + intent_name}}
    data = json.dumps(data)
    r = requests.post(url=url+page_access_token, data=data, headers=headers)
    if r.json()['result'] == 'success':
        print("Successfully added get_started button with '{}' intent.".format(intent_name))


if __name__ == '__main__':
    if len(sys.argv) == 3:
        intent = sys.argv[1]
        credential_file = sys.argv[2]
        add_get_started_button(intent, credential_file)
    else:
        print("Usage: python3 add_get_started_button.py intent_name credentials_file_path")
        print("Example: python3 add_get_started_button.py menu ../config/dev.credentials.yml")

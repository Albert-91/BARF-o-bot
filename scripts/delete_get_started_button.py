import json
import sys
from typing import Text

import requests
from data_readers import get_facebook_token_from_credentials


def delete_get_started_button(credential_file_path: Text):
    """
    Function removing "Get_Started" button from Messenger welcome screen for a new users.
    :param credential_file_path: Rasa file with Facebook credentials
    :param intent_name: intent which will be triggered after clicking "get_started" button
    """

    page_access_token = get_facebook_token_from_credentials(credential_file_path)
    url = "https://graph.facebook.com/v2.6/me/messenger_profile?access_token="
    headers = {"Content-Type": "application/json"}
    data = {"fields": ["get_started"]}
    data = json.dumps(data)
    r = requests.delete(url=url+page_access_token, data=data, headers=headers)
    if r.json()['result'] == 'success':
        print("Successfully deleted get_started button.")


if __name__ == '__main__':
    if len(sys.argv) == 2:
        credential_file = sys.argv[1]
        delete_get_started_button(credential_file)
    else:
        print("Usage: python3 delete_get_started_button.py credentials_file_path")
        print("Example: python3 delete_get_started_button.py ../config/dev.credentials.yml")

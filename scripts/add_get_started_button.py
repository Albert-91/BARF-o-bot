import sys
from typing import Text

import yaml
import json
import requests


def add_get_started_button(intent_name: Text, credential_file_path: Text):
    """
    curl -X POST -H "Content-Type: application/json" -d '{
  "get_started": {"payload": "<postback_payload>"}
}' "https://graph.facebook.com/v2.6/me/messenger_profile?access_token=<PAGE_ACCESS_TOKEN>"

    :param intent_name:
    :return:
    """
    page_access_token = get_token_from_credentials(credential_file_path)
    url = "https://graph.facebook.com/v2.6/me/messenger_profile?access_token="
    headers = {"Content-Type": "application/json"}
    data = {"get_started": {"payload": "/" + intent_name}}
    data = json.dumps(data)
    r = requests.post(url=url+page_access_token, data=data, headers=headers)
    print(r.status_code)
    print(r.json())


def get_token_from_credentials(credential_file_path: Text) -> Text:
    with open(credential_file_path, 'r') as stream:
        try:
            data = yaml.safe_load(stream)
            page_access_token = data['facebook']['page-access-token']
            return page_access_token
        except yaml.YAMLError as exc:
            print(exc)


if __name__ == '__main__':
    if len(sys.argv) == 3:
        intent = sys.argv[1]
        credential_file = sys.argv[2]
        add_get_started_button(intent, credential_file)
    else:
        print("Usage: python3 add_get_started_button.py intent_name credentials_file_path")
        print("Example: python3 add_get_started_button.py menu ../config/dev.credentials.yml")

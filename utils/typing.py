import json
from pathlib import Path

import requests
from dotenv import dotenv_values


def do_typing_on(psid):
    page_access_token = get_page_access_token()
    url = "https://graph.facebook.com/v2.6/me/messenger_profile?access_token="
    headers = {"Content-Type": "application/json"}
    data = {"recipient": {"id": psid}, "sender_action": "typing_on"}
    data = json.dumps(data)
    requests.post(url=url+page_access_token, data=data, headers=headers)


def get_page_access_token():
    env_path = Path('.') / '../.env'
    return dotenv_values(dotenv_path=env_path)['FACEBOOK_PAGE_ACCESS_TOKEN']


do_typing_on("3356313284408976")
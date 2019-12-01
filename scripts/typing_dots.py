import json

import requests

from utils.data_readers import get_page_access_token


def do_typing_on(psid):
    page_access_token = get_page_access_token()
    url = "https://graph.facebook.com/v2.6/me/messages?access_token="
    headers = {"Content-Type": "application/json"}
    data = {"recipient": {"id": psid}, "sender_action": "typing_on"}
    data = json.dumps(data)
    requests.post(url=url+page_access_token, data=data, headers=headers)

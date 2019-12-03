import json
import os
from enum import Enum
from typing import Text

import requests


class SenderAction(Enum):
    TYPING_ON = "typing_on"
    TYPING_OFF = "typing_off"
    MARK_SEEN = "mark_seen"


def sender_action_request(psid: Text, action: SenderAction):
    page_access_token = os.environ.get('FACEBOOK_PAGE_ACCESS_TOKEN')
    url = "https://graph.facebook.com/v2.6/me/messages?access_token="
    headers = {"Content-Type": "application/json"}
    data = {"recipient": {"id": psid}, "sender_action": action.value}
    data = json.dumps(data)
    requests.post(url=url+page_access_token, data=data, headers=headers)

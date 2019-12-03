import json
import os
from enum import Enum
from typing import Text

import requests


class TypingState(Enum):
    TYPING_ON = "typing_on"
    TYPING_OFF = "typing_off"


def sender_action_request(psid: Text, typing_action: TypingState):
    page_access_token = os.environ.get('FACEBOOK_PAGE_ACCESS_TOKEN')
    url = "https://graph.facebook.com/v2.6/me/messages?access_token="
    headers = {"Content-Type": "application/json"}
    data = {"recipient": {"id": psid}, "sender_action": typing_action.value}
    data = json.dumps(data)
    requests.post(url=url+page_access_token, data=data, headers=headers)

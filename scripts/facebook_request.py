import os
from abc import ABC
from enum import Enum
from typing import Text
import json
import logging
from urllib.parse import urlencode

import requests

logger = logging.getLogger(__name__)


class SenderActionType(Enum):
    TYPING_ON = "typing_on"
    TYPING_OFF = "typing_off"
    MARK_SEEN = "mark_seen"


class FacebookRequest:
    ENDPOINT = "https://graph.facebook.com/v5.0/me/messages"

    def __init__(self, token, psid):
        self.token = token
        self.psid = psid

    @property
    def api_url(self):
        return self.ENDPOINT + "?" + urlencode({"access_token": self.token})

    @property
    def headers(self):
        return {"Content-Type": "application/json"}

    def send_post_request(self, data):
        r = requests.post(url=self.api_url, data=data, headers=self.headers)
        if r.json()['result'] == 'success':
            print("Success.")

    def send_delete_request(self, data):
        r = requests.delete(url=self.api_url, data=data, headers=self.headers)
        if r.json()['result'] == 'success':
            print("Success.")


class SenderActions(FacebookRequest):

    def __init__(self, token, psid):
        super().__init__(token, psid)

    def typing_on(self):
        data = self.data(SenderActionType.TYPING_ON)
        self.send_post_request(data=data)

    def typing_off(self):
        data = self.data(SenderActionType.TYPING_OFF)
        self.send_post_request(data=data)

    def mark_seen(self):
        data = self.data(SenderActionType.MARK_SEEN)
        self.send_post_request(data=data)

    def data(self, action: SenderActionType):
        data = {"recipient": {"id": self.psid}, "sender_action": action.value}
        return json.dumps(data)


class GetStartedButton(FacebookRequest):

    def __init__(self, token, psid, intent=None):
        super().__init__(token, psid)
        self.intent = intent

    def add(self):
        data = {"get_started": {"payload": "/" + self.intent}}
        self.send_post_request(data=data)

    def delete(self):
        data = {"fields": ["get_started"]}
        self.send_delete_request(data=data)


# a = GetStartedButton()
# a.add()
# a.delete()

from utils.data_readers import get_page_access_token


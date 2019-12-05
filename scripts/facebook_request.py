import json
import logging
from enum import Enum
from urllib.parse import urlencode

import requests

logger = logging.getLogger(__name__)


class SenderActionType(Enum):
    TYPING_ON = "typing_on"
    TYPING_OFF = "typing_off"
    MARK_SEEN = "mark_seen"


class FacebookRequest:

    def __init__(self, token, psid):
        self.token = token
        self.psid = psid

    def api_url(self, endpoint):
        return endpoint + "?" + urlencode({"access_token": self.token})

    @property
    def headers(self):
        return {"Content-Type": "application/json"}

    def send_post_request(self, data, endpoint):
        r = requests.post(url=self.api_url(endpoint), data=data, headers=self.headers)
        if 'error' not in r.json().keys():
            print("Success.")
        else:
            print(r.json())

    def send_delete_request(self, data, endpoint):
        r = requests.delete(url=self.api_url(endpoint), data=data, headers=self.headers)
        if 'error' not in r.json().keys():
            print("Success.")
        else:
            print(r.json())


class MessagesRequest(FacebookRequest):

    MESSAGES_ENDPOINT = "https://graph.facebook.com/v5.0/me/messages"

    @property
    def endpoint(self):
        return self.MESSAGES_ENDPOINT


class MessengerProfileRequest(FacebookRequest):

    MESSENGER_PROFILE_ENDPOINT = "https://graph.facebook.com/v2.6/me/messenger_profile"

    @property
    def endpoint(self):
        return self.MESSENGER_PROFILE_ENDPOINT


class SenderActions(MessagesRequest):

    def __init__(self, token, psid):
        super().__init__(token, psid)

    def typing_on(self):
        data = self.data(SenderActionType.TYPING_ON)
        self.send_post_request(data=data, endpoint=self.endpoint)

    def typing_off(self):
        data = self.data(SenderActionType.TYPING_OFF)
        self.send_post_request(data=data, endpoint=self.endpoint)

    def mark_seen(self):
        data = self.data(SenderActionType.MARK_SEEN)
        self.send_post_request(data=data, endpoint=self.endpoint)

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



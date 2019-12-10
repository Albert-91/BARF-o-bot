import json
import logging
import os
from enum import Enum
from typing import List, Dict
from urllib.parse import urlencode

import requests

logger = logging.getLogger(__name__)


class SenderActionType(Enum):
    TYPING_ON = "typing_on"
    TYPING_OFF = "typing_off"
    MARK_SEEN = "mark_seen"


class MessengerProfileFields(Enum):
    GET_STARTED = "get_started"
    PERSISTENT_MENU = "persistent_menu"
    GREETING = "greeting"
    ICE_BREAKERS = "ice_breakers"


class FacebookRequest:

    def __init__(self, token=os.environ.get('FACEBOOK_PAGE_ACCESS_TOKEN'), psid=None):
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

    MESSENGER_PROFILE_ENDPOINT = "https://graph.facebook.com/v5.0/me/messenger_profile"

    @property
    def endpoint(self):
        return self.MESSENGER_PROFILE_ENDPOINT


class SenderActions(MessagesRequest):
    """
    https://developers.facebook.com/docs/messenger-platform/send-messages/sender-actions/
    """

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


class MessengerProfile(MessengerProfileRequest):

    def set_get_started_button(self, intent):
        """
        Method's setting "Get_Started" button on a Messenger welcome screen for a new users.
        :param intent: intent which will be triggered after clicking "get_started" button
        """
        data = {"get_started": {"payload": "/" + intent}}
        data = json.dumps(data)
        self.send_post_request(data=data, endpoint=self.endpoint)

    def set_persistent_menu(self, actions: List[Dict], locale="default"):
        """
         https://developers.facebook.com/docs/messenger-platform/send-messages/persistent-menu

         Example of data to set:
         {
             "persistent_menu": [
                 {
                     "locale": "default",
                     "composer_input_disabled": false,
                     "call_to_actions": [
                         {
                             "type": "postback",
                             "title": "Talk to an agent",
                             "payload": "CARE_HELP"
                         },
                         {
                             "type": "postback",
                             "title": "Outfit suggestions",
                             "payload": "CURATION"
                         },
                         {
                             "type": "web_url",
                             "title": "Shop now",
                             "url": "https://www.originalcoastclothing.com/",
                             "webview_height_ratio": "full"
                         }
                     ]
                 }
             ]
         }
         """
        data = {
            "persistent_menu": [
                {
                    "locale": locale,
                    "composer_input_disabled": False,
                    "call_to_actions": actions
                }
            ]
        }
        data = json.dumps(data)
        self.send_post_request(data=data, endpoint=self.endpoint)

    def set_greeting(self, actions: List[Dict]):
        """
        https://developers.facebook.com/docs/messenger-platform/reference/messenger-profile-api/greeting

        Example of data to set:
        "greeting":[
            {
            "locale":"default",
            "text":"Hello {{user_first_name}}!"
            }
        ]
        """
        data = {
            "greeting": actions
        }
        data = json.dumps(data)
        self.send_post_request(data=data, endpoint=self.endpoint)

    def set_ice_breakers(self, actions: List[Dict]):
        """
        https://developers.facebook.com/docs/messenger-platform/reference/messenger-profile-api/greeting

        Example of data to set:
        {
            "ice_breakers":[
                 {
                    "question": "Where are you located?",
                    "payload": "LOCATION_POSTBACK_PAYLOAD",
                 },
                 {
                    "question": "What are your hours?",
                    "payload": "HOURS_POSTBACK_PAYLOAD",
                 }
            ]
        }
        """
        data = {
            "ice_breakers": actions
        }
        data = json.dumps(data)
        self.send_post_request(data=data, endpoint=self.endpoint)

    def delete_field(self, field: MessengerProfileFields):
        data = {"fields": [field.value]}
        data = json.dumps(data)
        self.send_delete_request(data=data, endpoint=self.endpoint)

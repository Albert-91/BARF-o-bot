import json

import requests
from data_readers import get_page_access_token_from_dotenv


def delete_get_started_button():
    """
    Function removing "Get_Started" button from Messenger welcome screen for a new users.
    """
    page_access_token = get_page_access_token_from_dotenv()
    url = "https://graph.facebook.com/v2.6/me/messenger_profile?access_token="
    headers = {"Content-Type": "application/json"}
    data = {"fields": ["get_started"]}
    data = json.dumps(data)
    r = requests.delete(url=url+page_access_token, data=data, headers=headers)
    if r.json()['result'] == 'success':
        print("Successfully deleted get_started button.")


if __name__ == '__main__':
    delete_get_started_button()

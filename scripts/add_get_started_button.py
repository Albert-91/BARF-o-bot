from typing import Text

import json
import requests


def add_get_started_button(intent: Text):
    """
    curl -X POST -H "Content-Type: application/json" -d '{
  "get_started": {"payload": "<postback_payload>"}
}' "https://graph.facebook.com/v2.6/me/messenger_profile?access_token=<PAGE_ACCESS_TOKEN>"

    :param intent:
    :return:
    """
    page_access_token = ""
    data = {
        "get_started": {
            "payload": "/" + intent
        }
    }
    data = json.dumps(data)
    headers = {"Content-Type": "application/json"}
    url = "https://graph.facebook.com/v2.6/me/messenger_profile?access_token="
    r = requests.post(url=url+page_access_token, data=data, headers=headers)
    print(r.status_code)
    print(r.json())


if __name__ == '__main__':
    add_get_started_button("menu")
    # if len(sys.argv) == 4:
    #     DB_NAME = sys.argv[1]
    #     START_DATE = sys.argv[2]
    #     END_DATE = sys.argv[3]
    #     main(DB_NAME, START_DATE, END_DATE)
    # else:
    #     print("Usage: python3 analytics.py data_base_name.db start_date end_date")
    #     print("Example: python3 analytics.py wyrocznia_store.db 01.07.2019 30.07.2019")

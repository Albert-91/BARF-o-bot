from typing import Text

from environs import Env


def get_page_access_token() -> Text:
    env = Env()
    env.read_env()
    return env('FACEBOOK_PAGE_ACCESS_TOKEN')

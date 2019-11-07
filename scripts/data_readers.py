from pathlib import Path

from dotenv import dotenv_values


def get_page_access_token_from_dotenv():
    env_path = Path('.') / '../.env'
    return dotenv_values(dotenv_path=env_path)['FACEBOOK_PAGE_ACCESS_TOKEN']

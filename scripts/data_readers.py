from typing import Text

import yaml


def get_facebook_token_from_credentials(credential_file_path: Text) -> Text:
    with open(credential_file_path, 'r') as stream:
        try:
            data = yaml.safe_load(stream)
            return data['facebook']['page-access-token']
        except yaml.YAMLError as exc:
            print(exc)

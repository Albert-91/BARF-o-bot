import re
from typing import Text


def add_new_lines_to_text(string: Text) -> Text:
    """
    Function replaces all "\n" and "\n " to new lines.
    :param string:
    :return: string with new lines
    """
    s = re.sub(r"\\n ", "\n", string)
    s = re.sub(r"\\n", "\n", s)
    return s

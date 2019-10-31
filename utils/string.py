import re
from decimal import Decimal
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


def get_correct_week_word(quantity: Decimal) -> Text:
    if quantity == Decimal(1):
        return "tydzień"
    else:
        return "tygodnie"

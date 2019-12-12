MEAT_AMOUNT_UPPER_LIMIT = 100
DAILY_PORTION_UPPER_LIMIT = 3000
WEEKLY_CYCLE_UPPER_LIMIT = 4

# sender actions
DEFAULT_TYPING_TIME = 2
MINIMUM_TYPING_TIME = 1
MAXIMUM_TYPING_TIME = 8
AVARAGE_SIGN_PER_SECOND = 35
TIME_FROM_MARK_SEEN_TO_TYPING = 0.5

# messenger profile
GET_STARTED_BUTTON_INTENT = "menu"
GREETING_ACTIONS = [
    {
        "locale": "default",
        "text": "Cześć {{user_first_name}}! Czekałem tu na Ciebie!"
    }
]
ICE_BREAKERS_ACTIONS = [
    {
        "question": "Co to jest BARF?",
        "payload": "co to barf",
    },
    {
        "question": "Jak wprowadzić BARF?",
        "payload": "jak wprowadzić barf",
    }
]
PERSISTENT_MENU_ACTIONS = [
    {
        "type": "postback",
        "title": "Wróć do menu",
        "payload": "/menu"
    }
]

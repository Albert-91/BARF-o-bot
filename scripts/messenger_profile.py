from actions.settings import GET_STARTED_BUTTON_INTENT, GREETING_ACTIONS, ICE_BREAKERS_ACTIONS, PERSISTENT_MENU_ACTIONS
from facebook_request import MessengerProfile


def set_messenger_profile():
    messenger_profile = MessengerProfile()
    messenger_profile.set_get_started_button(GET_STARTED_BUTTON_INTENT)
    messenger_profile.set_greeting(GREETING_ACTIONS)
    messenger_profile.set_ice_breakers(ICE_BREAKERS_ACTIONS)
    messenger_profile.set_persistent_menu(PERSISTENT_MENU_ACTIONS)

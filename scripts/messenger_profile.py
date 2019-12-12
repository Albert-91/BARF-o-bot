from config.settings import *
from utils.data_readers import get_page_access_token
from facebook.facebook_request import MessengerProfile


def set_messenger_profile():
    token = get_page_access_token()
    messenger_profile = MessengerProfile(token=token)
    messenger_profile.set_get_started_button(GET_STARTED_BUTTON_INTENT)
    messenger_profile.set_greeting(GREETING_ACTIONS)
    messenger_profile.set_ice_breakers(ICE_BREAKERS_ACTIONS)
    messenger_profile.set_persistent_menu(PERSISTENT_MENU_ACTIONS)

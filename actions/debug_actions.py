"""
Debug Actions - use in stories for testing purposes
"""
from typing import Text
from rasa_sdk import Action
from rasa_sdk.events import SlotSet


class Debug1Action(Action):
    """Just utters "debug 1" marker"""

    def name(self):
        return 'action_debug_1'

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message("--- DEBUG 1 ---")
        return [SlotSet('debug_flag', True)]


class Debug2Action(Action):
    """Just utters "debug 2" marker"""

    def name(self):
        return 'action_debug_2'

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message("--- DEBUG 2 ---")
        return [SlotSet('debug_flag', None)]


class Debug3Action(Action):
    """Just utters "debug 3" marker"""

    def name(self):
        return 'action_debug_3'

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message("--- DEBUG 3 ---")
        return []


class DebugInfoAction(Action):
    """Utters detailed debug info related to current tracker state"""

    def name(self):
        return 'action_debug_info'

    def run(self, dispatcher, tracker, domain):
        current_state = tracker.current_state()
        dispatcher.utter_message("--- DEBUG INFO BEGIN ---")
        dispatcher.utter_message(f"@ latest action name: {str(current_state['latest_action_name'])}")
        dispatcher.utter_message(f"@ active form: {str(current_state['active_form'])}")
        dispatcher.utter_message(f"@ slots: {str(current_state['slots'])}")
        dispatcher.utter_message(f"@ latest msg:{str(current_state['latest_message'])}")
        dispatcher.utter_message("--- DEBUG INFO END ---")
        return []


class ActionTest1(Action):
    def name(self) -> Text:
        return 'action_test_1'

    def run(self, dispatcher, tracker, domain):
        return []


class ActionTest2(Action):
    def name(self) -> Text:
        return 'action_test_2'

    def run(self, dispatcher, tracker, domain):
        return []


import os
from json import JSONDecodeError
from typing import Text

import requests
from requests import RequestException

from rasa.constants import DEFAULT_CREDENTIALS_PATH
from rasa.utils.io import read_config_file
from rasa_sdk import Action
from rasa_sdk.events import SlotSet, ActionExecuted, UserUttered, Form


class CommonActionMixin:
    """Mixin with additional action helpers needed by some project actions"""

    def inject_intent(self, intent):
        """Returns events that injects given intent into tracker state to allow handling them on stories same way
           as comes from user input. Use this method in other actions in theirs return statement.
           [More details here ](https://forum.rasa.com/t/trigger-a-story-or-intent-from-a-custom-action/13784/9)"""

        return [ActionExecuted('action_listen', confidence=1.0), UserUttered(
            text='/' + intent, parse_data={'intent': {'name': intent, 'confidence': 1.0}, 'entities': []})]

    def inject_user_utterance_event(self, user_event):
        """Returns events that injects given user utterance event (with all appropriate data) into tracker state to
           allow handling them on stories same way as comes from user input. Use this method in other actions
           in theirs return statement.
           [More details here ](https://forum.rasa.com/t/trigger-a-story-or-intent-from-a-custom-action/13784/9)"""

        return [ActionExecuted('action_listen', confidence=1.0), user_event]


class SetOutOfScopeDetectedStateAction(Action):
    def name(self):
        return 'action_set_out_of_scope_detected'

    def run(self, dispatcher, tracker, domain):
        return [SlotSet('out_of_scope_detected', True)]


class SetOutOfScopeNotDetectedStateAction(Action):
    def name(self):
        return 'action_set_out_of_scope_not_detected'

    def run(self, dispatcher, tracker, domain):
        return [SlotSet('out_of_scope_detected', False)]


class ResetOutOfScopeDetectedStateAction(Action):
    def name(self):
        return 'action_reset_out_of_scope_detected'

    def run(self, dispatcher, tracker, domain):
        return [SlotSet('out_of_scope_detected', None)]


class ResetRequestedSlotAction(Action):
    def name(self):
        return 'action_reset_requested_slot'

    def run(self, dispatcher, tracker, domain):
        return [SlotSet('requested_slot', None)]


class GetFacebookUserProfileDataAction(Action):
    """Gets Facebook User profile data (name, surname, photo) and save it to slots if available"""

    fb_get_name_endpoint_tmpl = 'https://graph.facebook.com/{}?fields=first_name,last_name,profile_pic&access_token={}'

    def name(self):
        return 'action_get_fb_user_profile_data'

    def run(self, dispatcher, tracker, domain):
        most_recent_state = tracker.current_state()
        sender_id = most_recent_state['sender_id']
        # try getting fb data only if sender_id exists and bot not run in a rasa shell instance
        if sender_id and sender_id != 'default' and not tracker.get_slot('user_name'):
            credentials_file = os.environ.get('RASA_CREDENTIALS_FILE_PATH', DEFAULT_CREDENTIALS_PATH)
            try:
                fb_access_token = read_config_file(credentials_file)['facebook']['page-access-token']
                r = requests.get(self.fb_get_name_endpoint_tmpl.format(sender_id, fb_access_token)).json()
            except (RequestException, JSONDecodeError, KeyError):
                return []
            return [SlotSet('user_name', r['first_name']), SlotSet('user_surname', r['last_name']),
                    SlotSet('user_photo', r['profile_pic'])]
        return []


class StartShowcaseModeAction(Action):
    """Initiates a showcase mode"""

    def name(self):
        return 'action_start_showcase'

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_template('utter_showcase_menu', tracker)
        # resets slots used for showcase scenarios to ensure start it fresh again
        return [SlotSet('vehicle_type', None), SlotSet('vehicle_age', None),
                SlotSet('loan_amount', None), SlotSet('loan_length', None)]


class StartConversationModeAction(Action):
    """Initiates a play-with-bot mode"""

    def name(self):
        return 'action_start_play_with_bot'

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_template('utter_play_with_bot_intro', tracker)
        return []


class ShowcaseSolveProblemAction(Action):
    """Initiates a play-with-bot mode"""

    def name(self):
        return 'action_showcase_solve_problems'

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_template('utter_showcase_solve_problems_intro', tracker)
        return []


class InjectIntentStartCarLoanFormAction(CommonActionMixin, Action):
    """Injects intent `start_car_loan_form` to the tracker so stories may handle it accordingly to scenarion neeeds"""
    def name(self) -> Text:
        return 'action_inject_intent_start_car_loan_form'

    def run(self, dispatcher, tracker, domain):
        return self.inject_intent('start_car_loan_form')


class InjectIntentStartSolveProblem(CommonActionMixin, Action):
    """Injects intent `start_solve_problem` to the tracker so stories may handle it accordingly to scenarion neeeds"""
    def name(self) -> Text:
        return 'action_inject_intent_start_solve_problem'

    def run(self, dispatcher, tracker, domain):
        return self.inject_intent('start_solve_problem')


class UtterWrongRequestedSlotValueAction(Action):
    """Utters user with appropriate "wrong" utterance (that informs what values are valid/is expected) related to
       current requested slot. I.e. if current requested slot is `vehicle_age` it displays utterance
       `utter_wrong_vehicle_age`. May be used in forms processing to handle generic "wrong" messages for whole form
        in one story (no need to provide separate stories for every requested form slots).
        REMARK: this is generic action, works for any form as lon as related "expalin" utter templates are provided"""

    def name(self) -> Text:
        return 'action_utter_wrong_requested_slot_value'

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_template('utter_wrong_' + tracker.get_slot('requested_slot'), tracker)
        return []


class UtterExplainRequestedSlotAction(Action):
    """Utters user with appropriate "explain" utterance (that informs why bot ask for them) related to
       current requested slot. I.e. if current requested slot is `vehicle_age` it displays utterance
       `utter_explain_vehicle_age`. May be used in forms processing to handle generic "explain" messages for whole form
        in one story (no need to provide separate stories for every requested form slots).
        REMARK: this is generic action, works for any form as lon as related "expalin" utter templates are provided"""

    def name(self) -> Text:
        return 'action_utter_explain_requested_slot_value'

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_template('utter_explain_' + tracker.get_slot('requested_slot'), tracker)
        return []

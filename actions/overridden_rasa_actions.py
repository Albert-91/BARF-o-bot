import json
import logging
import os
from typing import List, Text, Dict, Any

from rasa_sdk import Action, Tracker
from rasa_sdk.events import Restarted, AllSlotsReset, Form, SlotSet, UserUtteranceReverted, ConversationPaused
from rasa_sdk.executor import CollectingDispatcher

from actions.actions import CommonActionMixin
from utils.string import add_new_lines_to_text


logger = logging.getLogger(__name__)


class RestartBotAction(Action):
    """Resets the tracker to its initial state (resets slot values etc), displays utter_restart
       template message and fires action that displays welcome message"""

    def name(self):
        return 'action_restart'

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict]:
        dispatcher.utter_template('utter_restart', tracker, silent_fail=True)
        return [Restarted(), AllSlotsReset()]


# # REMARK: currently not used
# class DefaultAskAffirmationAction(Action):
#     """Asks for an affirmation of the intent if NLU threshold is not met.
#        Solution adopted from rasa-demo bot."""
#
#     def name(self) -> Text:
#         return 'action_default_ask_affirmation'
#
#     def __init__(self) -> None:
#         import pandas as pd
#         intent_description_mapping_file = os.environ.get('INTENT_DESCRIPTION_MAPPING_FILE_PATH')
#         self.intent_mappings = pd.read_csv(intent_description_mapping_file, comment='#')
#         self.intent_mappings.fillna('', inplace=True)
#         self.intent_mappings.entities = self.intent_mappings.entities.map(
#             lambda entities: {e.strip() for e in entities.split(',')}
#         )
#
#     def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict]:
#         intent_ranking = tracker.latest_message.get('intent_ranking', [])
#         if len(intent_ranking) > 1:
#             diff_intent_confidence = intent_ranking[0].get('confidence') - intent_ranking[1].get('confidence')
#             intent_ranking = intent_ranking[:2] if diff_intent_confidence < 0.2 else intent_ranking[:1]
#         first_intent_names = [intent.get('name', '') for intent in intent_ranking
#                               if intent.get('name', '') != 'out_of_scope']
#         entities = tracker.latest_message.get('entities', [])
#         entities = {e['entity']: e['value'] for e in entities}
#         entities_json = json.dumps(entities)
#         buttons = []
#         for intent in first_intent_names:
#             logger.debug(intent)
#             logger.debug(entities)
#             buttons.append({'title': self.get_button_title(intent, entities),
#                             'payload': "/{}{}".format(intent, entities_json)})
#         buttons.append({'title': self.get_button_title('out_of_scope', entities), 'payload': '/out_of_scope'})
#         dispatcher.utter_button_message(
#             domain['templates']['utter_default_ask_affirmation_headline'][0]['text'], buttons=buttons)
#         return []
#
#     def get_button_title(self, intent: Text, entities: Dict[Text, Text]) -> Text:
#         default_utterance_query = self.intent_mappings.intent == intent
#         utterance_query = (self.intent_mappings.entities == entities.keys() & default_utterance_query)
#         utterances = self.intent_mappings[utterance_query].button.tolist()
#         if len(utterances) > 0:
#             button_title = utterances[0]
#         else:
#             utterances = self.intent_mappings[default_utterance_query].button.tolist()
#             button_title = utterances[0] if len(utterances) > 0 else intent
#         return button_title.format(**entities)


class ActionDefaultFallback(CommonActionMixin, Action):
    """
    Special version of default fallback action that "extends" Rasa for very missing feature - generic `out_of_scope`
    intent that this action injects into tracker (as if were "fired" by user input processing) so it may be handled
    on stories to control dialog flow or provide context-dependent utterances.

    When using this action as fallback action (used by configured fallback policies) you have to wrote your stories
    in a special way as this is the only way to fool the Rasa memoization machinery to work properly with
    injected intents - stories that handles desire intent must be splitted into two separate stories:
    one that handles desired intent detected with high confidence and one that handles generated out_of_scope intent
    for case when desired intent has been detected with low confidence. Here is an self-explaining example:

    ## 1st story that handles some_intent that has been detected with high NLU confidence (above NLU threshold)
    ## and runs action_xxx in this case
    <!-- some_intent detected initially (case "with high confidence") -->
    * some_intent
      - action_default_fallback  <!-- our action is called and do it's job according to some_intent confidence -->
      - slot{"out_of_scope_detected": false} <!-- memoized case when confidence is above NLU threshold -->
      - form{"name": null}  <!-- our action always deactivates form so it must be memoized -->
      <!-- when some_intent detected initially has high confidence, our action injects it again, so can be handled here normally -->
    * some_intent
      - action_xxx

    ## 2nd story that handles some_intent that has been recognised with low NLU confidence (below NLU threshold)
    ## and runs action_yyy in this case
    <!-- some_intent detected initially (case "with low confidence")-->
    * some_intent
      - action_default_fallback  <!-- our action is called and do it's job according to some_intent confidence -->
      - slot{"out_of_scope_detected": true}  <!-- memoized case when confidence is below NLU threshold -->
      - form{"name": null}  <!-- our action always deactivates form so it must be memoized -->
      <!-- when some_intent detected initially has low confidence, out_of_scope intent is injected o can be handled here normally -->
    * out_of_scope
      - action_yyy

    Tricky and hacky but works awesome! Enjoy! ;)
    """

    def name(self) -> Text:
        return 'action_default_fallback'

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict]:

        # check if special behavior is enabled, otherwise run standard behavior
        if not tracker.get_slot('conf.use_generic_out_of_scope_intent_injection_in_fallback_action'):
            # REMARK: currently TwoStageFallbackPolicy not used
            # Fallback caused by TwoStageFallbackPolicy
            # if len(tracker.events) >= 4 and tracker.events[-4].get('name') == 'action_default_ask_affirmation':
            #     dispatcher.utter_template('utter_restart_with_button', tracker)
            #     # return [SlotSet("feedback_value", "negative"), ConversationPaused()]
            #     return [ConversationPaused()]
            # # Fallback caused by Core
            # else:
            #     dispatcher.utter_template('utter_default', tracker)
            #     return [UserUtteranceReverted()]

            # default behavior
            dispatcher.utter_template('utter_default', tracker)
            return [UserUtteranceReverted()]
        else:
            # find last user utterance event (contains intent and its confidence / data)
            last_user_utterance_event = None
            for event in reversed(tracker.events):
                if event['event'] == 'user':
                    last_user_utterance_event = event
                    break

            if not last_user_utterance_event:
                # just in case... run "default" behaviour
                logger.error("No last user utterance found, unexpected behavior!")
                dispatcher.utter_template('utter_default', tracker)
                return [UserUtteranceReverted()]

            logger.debug(f"\nlatest user utterance event found: {last_user_utterance_event}\n")

            if last_user_utterance_event['parse_data']['intent']['confidence'] < 0.85:
                # user intent below desired NLU threshold so inject `out_of_scope` intent and set special slot
                # used in stories that keeps info that out of scope has been detected as True
                return [Form(None), SlotSet('out_of_scope_detected', True)] + self.inject_intent('out_of_scope')
            else:
                # user intent above NLU threshold so inject last user utterance again and set special slot
                # used in stories that keeps info that out of scope has been detected as False to notice that
                # user intent should be processed normally "as is", not as an out of scope
                return [Form(None), SlotSet('out_of_scope_detected', False)] + self.inject_user_utterance_event(
                    last_user_utterance_event)


class ActionRetrieveResponseFaq(Action):
    """Queries the Response Selector for the appropriate response."""

    def name(self) -> Text:
        return "action_respond_faq"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict]:
        """Query the appropriate response and create a bot utterance with that."""

        # Whole method structure is almost the same as built-in Rasa method because this action will be used for the
        # next faq response selectors and all next modification will be easier.

        MESSAGE_SELECTOR_PROPERTY_NAME = "response_selector"
        DEFAULT_OPEN_UTTERANCE_TYPE = "default"
        OPEN_UTTERANCE_PREDICTION_KEY = "response"

        response_selector_properties = tracker.latest_message[
            MESSAGE_SELECTOR_PROPERTY_NAME
        ]

        if "faq_debit_card" in response_selector_properties:
            query_key = "faq_debit_card"
        elif "faq_credit_card" in response_selector_properties:
            query_key = "faq_credit_card"
        elif DEFAULT_OPEN_UTTERANCE_TYPE in response_selector_properties:
            query_key = DEFAULT_OPEN_UTTERANCE_TYPE
        else:
            logger.error(
                "Couldn't create message for response action '{}'."
                "".format("respond_faq")
            )
            return []

        logger.debug("Picking response from selector of type {}".format(query_key))
        message = {
            "text": response_selector_properties[query_key][
                OPEN_UTTERANCE_PREDICTION_KEY
            ]["name"]
        }
        message = add_new_lines_to_text(message['text'])
        dispatcher.utter_message(message)
        return []

from decimal import Decimal
from typing import Text, List, Dict, Union, Any

from rasa_sdk import Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction

from utils.products_calculator import calculate_products_to_buy, calculate_ingredients_distribution
from utils.string import get_correct_week_word
from .settings import *


class CalculateProductsToBuyForm(FormAction):

    def name(self) -> Text:
        return 'form_calculate_products_to_buy'

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return ['meat_amount']

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        return {'meat_amount': [self.from_entity(entity='number', intent='enter_meat_amount'),
                                self.from_entity(entity='number')]}

    def validate_meat_amount(self, value: Text, dispatcher: CollectingDispatcher, tracker: Tracker,
                             domain: Dict[Text, Any]) -> Dict[Text, Any]:
        try:
            meat_amount = int(value[0])
            if not 1 < meat_amount <= MEAT_AMOUNT_UPPER_LIMIT:
                raise ValueError
        except (ValueError, TypeError):
            dispatcher.utter_template('utter_wrong_meat_amount', tracker)
            return {'meat_amount': None}
        return {'meat_amount': str(value[0])}

    def round_number(self, number: Decimal, decimal_places: int):
        decimal_value = Decimal(number)
        return decimal_value.quantize(Decimal(10) ** -decimal_places)

    def submit(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict]:
        meat_amount = Decimal(tracker.get_slot('meat_amount'))
        dispatcher.utter_template('utter_loan_summarize', tracker)
        products_amounts = calculate_products_to_buy(meat_amount)
        dispatcher.utter_template('utter_summarize_products_to_buy_form', tracker,
                                  meat_amount=int(meat_amount),
                                  liver_amount=float(self.round_number(products_amounts['liver'], 2)),
                                  offal_amount=float(self.round_number(products_amounts['offal'], 2)),
                                  bones_amount=float(self.round_number(products_amounts['bones'], 2)))
        return []


class CalculateIngredientsDistribution(FormAction):

    def name(self) -> Text:
        return 'form_calculate_ingredients_distribution'

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return ['daily_portion', 'weekly_cycle']

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        return {'daily_portion': [self.from_entity(entity='number'),
                                  self.from_entity(entity='number', intent='enter_daily_portion')],
                'weekly_cycle': [self.from_entity(entity='number'),
                                 self.from_entity(entity='number', intent='enter_weekly_cycle')]}

    def validate_daily_portion(self, value: Text, dispatcher: CollectingDispatcher, tracker: Tracker,
                             domain: Dict[Text, Any]) -> Dict[Text, Any]:
        try:
            daily_portion = int(value[0])
            if not 1 < daily_portion <= DAILY_PORTION_UPPER_LIMIT:
                raise ValueError
        except (ValueError, TypeError):
            dispatcher.utter_template('utter_wrong_daily_portion', tracker)
            return {'daily_portion': None}
        return {'daily_portion': str(value[0])}

    def validate_weekly_cycle(self, value: Text, dispatcher: CollectingDispatcher, tracker: Tracker,
                             domain: Dict[Text, Any]) -> Dict[Text, Any]:
        try:
            weekly_cycle = int(value[0])
            if not 1 < weekly_cycle <= WEEKLY_CYCLE_UPPER_LIMIT:
                raise ValueError
        except (ValueError, TypeError):
            dispatcher.utter_template('utter_wrong_weekly_cycle', tracker)
            return {'weekly_cycle': None}
        return {'weekly_cycle': str(value[0])}

    def round_number(self, number: Decimal, decimal_places: int):
        decimal_value = Decimal(number)
        return decimal_value.quantize(Decimal(10) ** -decimal_places)

    def submit(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict]:
        weekly_cycle = Decimal(tracker.get_slot('weekly_cycle'))
        daily_portion = Decimal(tracker.get_slot('daily_portion'))
        week = get_correct_week_word(weekly_cycle)
        ingredients = calculate_ingredients_distribution(weekly_cycle, daily_portion)
        dispatcher.utter_template('utter_summarize_ingredients_distribution_form', tracker,
                                  weekly_cycle=int(weekly_cycle),
                                  daily_portion=int(daily_portion),
                                  week=week,
                                  meat_amount=int(ingredients['meat']),
                                  liver_amount=int(ingredients['liver']),
                                  offal_amount=int(ingredients['offal']),
                                  bones_amount=int(ingredients['bones']))
        return []


class WeatherForm(FormAction):

    def name(self) -> Text:
        return 'form_weather'

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return ['location']

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        return {'location': [self.from_entity(entity='location', intent='enter_location'),
                             self.from_entity(entity='location', intent='weather')]}

    def submit(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict]:

        return []


class FeedbackForm(FormAction):
    """Form that handles collecting feedback"""

    def name(self) -> Text:
        return 'form_feedback'

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        if tracker.get_slot('feedback_value') == 'not_provided':
            return ['feedback_value']  # user don't want share feedback, we're done, don't ask for anything else
        elif tracker.get_slot('give_feedback_message') is False:
            return ['feedback_value', 'give_feedback_message']  # user skipped feedback message, don't ask for it
        else:
            return ['feedback_value', 'give_feedback_message', 'feedback_message']

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        return {'feedback_value': [self.from_entity('feedback_value'),
                                   self.from_intent(intent='affirm', value='positive'),
                                   self.from_intent(intent='deny', value='negative'),
                                   self.from_intent(intent='stop', value='not_provided')],
                'give_feedback_message': [self.from_intent(intent='affirm', value=True),
                                          self.from_intent(intent='deny', value=False),
                                          self.from_intent(intent='stop', value=False)],
                'feedback_message': [self.from_text()]}

    def submit(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict]:
        if tracker.get_slot('feedback_value') in ['positive', 'negative']:
            dispatcher.utter_template('utter_thanks_for_feedback', tracker)
        return [SlotSet('feedback_value', None), SlotSet('feedback_message', None),
                SlotSet('give_feedback_message', None)]

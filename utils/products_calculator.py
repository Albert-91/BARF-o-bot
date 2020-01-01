from decimal import Decimal
from enum import Enum
from typing import Dict, Text, List


class ProductsRatio(Enum):
    LIVER = 0.07
    OFFAL = 0.2
    BONES = 0.3
    MEAT = 1 - LIVER - OFFAL - BONES

    @staticmethod
    def get_all_products() -> List:
        return list(map(lambda c: c, ProductsRatio))


def calculate_products_to_buy(meat_amount: Decimal) -> Dict[Text, Decimal]:
    """
    Function gets amount of meat and depends on ratio of each product returns a dictionary with
    weights of rest of all products.
    :param meat_amount: in "kg" unit
    :return: dictionary with values in "kg" unit of liver, offal and bones
    """

    products = ProductsRatio.get_all_products()
    return {product.name: (meat_amount * Decimal(product.value) / Decimal(ProductsRatio.MEAT.value))
            for product in products if product is not ProductsRatio.MEAT}


def calculate_ingredients_distribution(weekly_cycle: Decimal, daily_portion: Decimal) -> Dict[Text, Decimal]:
    """
    Function gets number of cycles and amount of daily portion and returns a dict with total weight of each product
    in cycle.
    :param weekly_cycle: Decimal
    :param daily_portion: Decimal
    :return: dictionary with values in "kg" unit of each product in cycle
    """

    total_cycle_food = daily_portion * Decimal(7) * weekly_cycle
    return {ingredient.name: (Decimal(ingredient.value) * total_cycle_food) for ingredient in ProductsRatio.get_all_products()}

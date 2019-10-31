from decimal import Decimal
from enum import Enum
from typing import Dict, Text


class ProductsRatio(Enum):
    LIVER = 0.07
    OFFAL = 0.2
    BONES = 0.3
    MEAT = 1 - LIVER - OFFAL - BONES


def calculate_products_to_buy(meat_amount: Decimal) -> Dict[Text, Decimal]:
    """
    Function gets amount of meat and depends on ratio of each product returns a dictionary with weights of all products.
    :param meat_amount: in "kg" unit
    :return: dictionary with values in "kg" unit of liver, offal and bones
    """
    liver_to_buy = meat_amount * Decimal(ProductsRatio.LIVER.value) / Decimal(ProductsRatio.MEAT.value)
    offal_to_buy = meat_amount * Decimal(ProductsRatio.OFFAL.value) / Decimal(ProductsRatio.MEAT.value)
    bones_to_buy = meat_amount * Decimal(ProductsRatio.BONES.value) / Decimal(ProductsRatio.MEAT.value)
    return {
        "liver": liver_to_buy,
        "offal": offal_to_buy,
        "bones": bones_to_buy,
    }


def calculate_ingredients_distribution(weekly_cycle: Decimal, daily_portion: Decimal) -> Dict[Text, Decimal]:
    """
    Function gets number of cycles and amount of daily portion and returns a dict with total weight of each product
    in cycle.
    :param weekly_cycle: Decimal
    :param daily_portion: Decimal
    :return: dictionary with values in "kg" unit of each product in cycle
    """
    total_cycle_food = daily_portion * Decimal(7) * weekly_cycle
    liver_to_cycle = Decimal(ProductsRatio.LIVER.value) * total_cycle_food
    meat_to_cycle = Decimal(ProductsRatio.MEAT.value) * total_cycle_food
    offal_to_cycle = Decimal(ProductsRatio.OFFAL.value) * total_cycle_food
    bones_to_cycle = Decimal(ProductsRatio.BONES.value) * total_cycle_food
    return {
        "liver": liver_to_cycle,
        "meat": meat_to_cycle,
        "offal": offal_to_cycle,
        "bones": bones_to_cycle,
    }

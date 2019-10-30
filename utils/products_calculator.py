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

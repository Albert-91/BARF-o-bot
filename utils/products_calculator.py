from decimal import Decimal
from enum import Enum
from typing import Dict, Text


class ProductsRatio(Enum):
    LIVER = 0.07
    OFFAL = 0.2
    BONES = 0.3


def calculate_products_to_buy(meat_amount: Decimal) -> Dict[Text, Decimal]:
    MEAT_RATIO = Decimal(1 - ProductsRatio.BONES.value - ProductsRatio.OFFAL.value - ProductsRatio.LIVER.value)
    liver_to_buy = meat_amount * Decimal(ProductsRatio.LIVER.value) / MEAT_RATIO
    offal_to_buy = meat_amount * Decimal(ProductsRatio.OFFAL.value) / MEAT_RATIO
    bones_to_buy = meat_amount * Decimal(ProductsRatio.BONES.value) / MEAT_RATIO
    return {
        "liver": liver_to_buy,
        "offal": offal_to_buy,
        "bones": bones_to_buy,
    }

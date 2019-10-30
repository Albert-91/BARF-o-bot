from decimal import Decimal
from enum import Enum
from typing import Dict, Text


class ProductsRatio(Enum):
    LIVER = 0.07
    OFFAL = 0.2
    BONES = 0.3
    MEAT = 1 - LIVER.value - OFFAL.value - BONES.value


def calculate_products_to_buy(meat_amount: Decimal) -> Dict[Text, Decimal]:
    liver_to_buy = meat_amount * Decimal(ProductsRatio.LIVER.value) / ProductsRatio.MEAT.value
    offal_to_buy = meat_amount * Decimal(ProductsRatio.OFFAL.value) / ProductsRatio.MEAT.value
    bones_to_buy = meat_amount * Decimal(ProductsRatio.BONES.value) / ProductsRatio.MEAT.value
    return {
        "liver": liver_to_buy,
        "offal": offal_to_buy,
        "bones": bones_to_buy,
    }

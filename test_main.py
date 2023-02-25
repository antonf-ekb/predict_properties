from main import calculate_values
from main import get_models


def test_calculate_values():
    assert calculate_values("Mn2CoCrP2", get_models()) == [6.07, 163, 95]


def test_calculate_values_bad():
    assert calculate_values("e", get_models()) == [0]
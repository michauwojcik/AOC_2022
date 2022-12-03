import pytest 
import sys
import os 

sys.path.append(os.path.abspath(__file__ + "/../.."))
from rucksacks import RucksackManager


@pytest.mark.parametrize(
    "test_input,expected", [
        ("asdfhjka", 1),
        ("obbi", 2),
        ("aa", 1),
        ("zioz", 26),
    ]
)
def test_get_points_whole_game(test_input, expected):
    rucksack = RucksackManager(test_input)
    
    assert rucksack.get_rucksack_value() == expected

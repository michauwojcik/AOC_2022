import pytest 
import sys
import os 

sys.path.append(os.path.abspath(__file__ + "/../.."))
from rucksacks import RucksackManager

@pytest.mark.parametrize(
    "test_input,expected", 
    [
        ("asdfhjka", {"a"}),
        ("obbi",     {"b"}),
        ("aa",       {"a"}),
        ("zioz",     {"z"}),
        ("CCABCC",   {"C"}),
        ("CCAACC",   {"C", "A"})
    ]
)
def test_get_common_items(test_input, expected):
    rucksack = RucksackManager(test_input)
    
    assert rucksack.get_common_items() == expected


@pytest.mark.parametrize(
    "test_input,expected", 
    [
        ("asdfhjka",  1),
        ("obbi",      2),
        ("aa",        1),
        ("zioz",      26),
        ("CCAACC",    56),
        ("aAbCAa",    28)
    ]
)
def test_get_rucksack_value(test_input, expected):
    rucksack = RucksackManager(test_input)
    
    assert rucksack.get_rucksack_value() == expected






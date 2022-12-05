import pytest 
import sys
import os 

from sections import CommonSectionsFinder


@pytest.mark.parametrize(
    "test_input,expected", [
        ('2-6', {2,3,4,5,6}),
        ('4-8', {4,5,6,7,8}),
        ('6-6', {6}),
        ('1-2', {1,2})
    ]
)
def test_get_sections_range(test_input, expected):
    sections = CommonSectionsFinder([])
    assert sections.get_sections_range(test_input) == expected


@pytest.mark.parametrize(
    "test_input,expected", [
        ([['2-4', '6-8'], ['2-3', '4-5']], [({2,3,4}, {6,7,8}), ({2,3}, {4,5})]),
        ([['1-1', '2-3'], ['6-6', '3-3']], [({1}, {2,3}), ({6}, {3})])
    ]
)
def test_get_sections_sets_pairs(test_input, expected):
    sections = CommonSectionsFinder(test_input)
    assert sections.get_sections_sets_pairs() == expected


@pytest.mark.parametrize(
    "test_input,expected", [
        ( [ ({2,3}   ,{4,5}    ), ({3}, {3}) ], 1),
        ( [ ({2,3,4} ,{2,3,4,5}), ({3}, {3}) ], 2),
        ( [ ({2,3,4,5} ,{2,3,4}), ({3}, {3}) ], 2),
        ( [ ({2,3,4,5} ,{2,3,4}), ({3}, {3}), ({1,2,3}, {1,2,4})], 2),
    ]
)
def test_count_common_sections(test_input, expected):
    sections = CommonSectionsFinder([])
    assert sections.count_common_sections(test_input) == expected


@pytest.mark.parametrize(
    "test_input1,test_input2,expected", [
        ({4}, {4}, True),
        ({2,3,4}, {2,3,4}, True),
        ({2,3}, {2,3,4}, True),
        ({2,3,4}, {2,3}, True),
        ({2,4,5}, {2,3}, False),
        ({2,3}, {2,4,5}, False),
    ]
)
def test_check_two_sets(test_input1, test_input2, expected):
    assert CommonSectionsFinder.check_two_sets(test_input1, test_input2) == expected
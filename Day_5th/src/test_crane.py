""" Unit tests for CraneDriver's methods """

import pytest 
import sys
import os 

from crane import CraneDriver


@pytest.mark.parametrize(
    "test_input_instruction,test_input_crates,expected", [
        ((1, 2, 1), {1: ['Z', 'N', 'D'], 2: ['M', 'C'], 3: ['P']}, {1: ['Z', 'N', 'D', 'C'], 2: ['M'], 3: ['P']}),
        ((1, 2, 3), {1: ['Z', 'N', 'D'], 2: ['M', 'C'], 3: []},    {1: ['Z', 'N', 'D'], 2: ['M'], 3: ['C']}),
        ((1, 1, 3), {1: ['Z', 'N'], 2: [], 3: []},                 {1: ['Z'], 2: [], 3: ['N']}),
        ((1, 3, 2), {1: ['Z', 'N', 'D'], 2: ['M'], 3: ['P']},      {1: ['Z', 'N', 'D'], 2: ['M', 'P'], 3: []}),
    ]
)
def test_move_one_crate(test_input_instruction, test_input_crates, expected):
    crane = CraneDriver(
        crates_in_stacks=test_input_crates, 
        procedure=()
    )

    crane.move_one_crate(test_input_instruction)

    assert crane.crates_in_stacks == expected

    
@pytest.mark.parametrize(
    "test_input_procedure,test_input_crates,expected", [
        (
            ((1, 2, 1), (3, 1, 3), (2, 2, 1), (1, 1, 2)), 
            {1: ['Z', 'N'], 2: ['M', 'C', 'D'], 3: ['P']}, 
            {1: ['C'],      2: ['M'],           3: ['P', 'D', 'N', 'Z']}
        ),

        (
            ((1, 2, 1), (1, 3, 1), (3, 1, 3)), 
            {1: ['Z'],   2: ['M'],    3: ['P']}, 
            {1: [],      2: [],       3: ['P', 'M', 'Z']}
        ),

        (
            ((3, 1, 2), (3, 2, 3)), 
            {1: ['A', 'B', 'C'], 2: [],    3: []}, 
            {1: [],              2: [],    3: ['A', 'B', 'C']}
        )

    ]
)
def test_perform_procedure(test_input_procedure, test_input_crates, expected):
    crane = CraneDriver(
        crates_in_stacks=test_input_crates, 
        procedure=test_input_procedure
    )

    crane.perform_procedure()
    
    crane.crates_in_stacks == expected


@pytest.mark.parametrize(
    "test_input_crates,expected", [
        ({1: ['Z', 'N', 'D'], 2: ['M', 'C'], 3: ['P']}, 'DCP'),
        ({1: ['A', 'B', 'C'], 2: [],         3: []},    'C'),
        ({1: [],              2: [],         3: []},    '')
    ]
)
def test_get_top_crates(test_input_crates, expected):
    crane = CraneDriver(
        crates_in_stacks=test_input_crates, 
        procedure=()
    )

    assert crane.get_top_crates() == expected

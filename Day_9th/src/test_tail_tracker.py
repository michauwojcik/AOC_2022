import pytest 
import sys
import os 
import numpy as np

sys.path.append("../../Common")
from tail_tracker import TailTracker
from text_file_manager import TextFileManager

input = TextFileManager("../data/moves_example.txt")




@pytest.mark.parametrize(
    "test_input_starting_point,test_input_curr_tail_position,expected", [
        (np.array([5, 6]), np.array([6, 6]), True),
        (np.array([5, 5]), np.array([6, 6]), True),
        (np.array([-1, -2]), np.array([0, -1]), True),
        # (np.array([5, 6]), np.array([6, 6]), True),
        # (np.array([5, 6]), np.array([6, 6]), True),
    ]
)
def test_check_tail_neighborhood(test_input_starting_point, test_input_curr_tail_position, expected):
    tracker = TailTracker(input.lines)
    tracker.curr_tail_position = test_input_curr_tail_position
    assert tracker.check_tail_neighborhood(test_input_starting_point) == expected
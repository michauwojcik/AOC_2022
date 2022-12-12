import pytest 
import sys
import os 
import numpy as np

sys.path.append("../../Common")
from cartesian_coordinates_system import CartesianCoordinateSystem
from text_file_manager import TextFileManager

input = TextFileManager("../data/moves_example.txt")




@pytest.mark.parametrize(
    "test_input_p1, test_input_p2, expected", [
        (np.array([2, 4]), np.array([1, 4]), True),
        (np.array([4, 3]), np.array([2, 4]), False),
        (np.array([1,  4]), np.array([-3,  3]), False),
        (np.array([1,  4]), np.array([4,  3]), False),
        # (np.array([5, 6]), np.array([6, 6]), True),
        # (np.array([5, 6]), np.array([6, 6]), True),
    ]
)
def test_check_point_neighborhood(test_input_p1, test_input_p2, expected):
    

    system = CartesianCoordinateSystem()

    assert system.check_point_neighborhood(test_input_p1, test_input_p2) == expected
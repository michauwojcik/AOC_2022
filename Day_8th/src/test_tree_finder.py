import pytest 
import sys
import os 
import numpy as np

sys.path.append("../../Common")
from tree_finder import Forest
from text_file_manager import TextFileManager

input = TextFileManager("../data/forest_plan_example2.txt")




@pytest.mark.parametrize(
    "test_input_trees,test_input_tree_height,expected", [
        (np.array([1, 2, 3, 4, 5, 6, 7]), 4, 5),
        (np.array([7, 7, 7, 7, 7, 3, 3]), 4, 1),
        (np.array([3, 3, 3, 3, 3, 3, 4]), 4, 7),
        (np.array([3, 3, 3, 3, 3, 3, 3]), 4, 7),
        (np.array([3, 3, 3, 3, 3, 3, 3]), 3, 1)
    ]
)
def test_find_first_higher_tree(test_input_tree_height, test_input_trees,  expected):
    assert Forest.get_tree_view(test_input_tree_height, test_input_trees) == expected
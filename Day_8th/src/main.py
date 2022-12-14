""" 
    Program: 
        1. Finds all visibles trees in given forest (and counts them)
        2. Calculates view score for each tree (and finds the one with highest score)
"""

from tree_finder import Forest
import sys
sys.path.append("../../Common")
from text_file_manager import TextFileManager

forest_plan = sys.argv[1]

def main(forest_plan):
    input = TextFileManager(forest_plan)
    
    forest = Forest(input.lines)
    print(f"Forest plan: \n{forest}")
    print(f"Forest dimensions: \n{forest.length} x {forest.width}\n")
    
    forest.count_all_visible_trees()
    print(f"Coordinates of visibles trees:\n{forest.visible_trees_coors}\n")
    print(f"Number of all visible trees in the forest:\n{forest.visible_trees}\n")
    print(f"Edges tree: \n{forest.edge_trees}\n")

    forest.calculate_trees_view_score()
    tree, view_score = forest.get_tree_with_highest_score()
    print(f"The tree with highest score: {tree}\nThe highest view score: {view_score}")


if __name__ == "__main__":
    main(forest_plan)
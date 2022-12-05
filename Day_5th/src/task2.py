"""
    Program for the new crane - CraneMover9001
    Main program for finding crates on the top of each stack. 

    1. Loads the drawing from given path
    2. Parses input into more convenient structures (crates_in_stacks, procedure)
    3. Simulates all crane's move
    4. Finds the crates which are on the top of each stack.

"""

import sys
from crane import Crane9001Driver 
from drawing_parser import DrawingParser
sys.path.append("../../Common")
from text_file_manager import TextFileManager

crates = sys.argv[1]

def main(crates):
    # Parsing input 
    text = TextFileManager(crates)
    parser = DrawingParser(text.content)
    crates_in_stacks, procedure = parser.get_drawing_and_procedure()

    # Moving crane
    crane = Crane9001Driver(procedure, crates_in_stacks)
    crane.perform_procedure()
    top_crates = crane.get_top_crates()

    # Result
    print(top_crates)
    

if __name__ == "__main__":
    main(crates)
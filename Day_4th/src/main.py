"""
    Main program for find fully covered sections.

    1. Loads the input (textfile) with sections ranges. Each line is pair of two elves' sections
    2. Creates a list of pairs, where each pair is a tuple of sections (represented as sets) which will be compared.
    3. Finds the sections which are fully covered by other elf's sections range

"""

import sys
sys.path.append("../../Common")
from text_file_manager import TextFileManager
from sections import CommonSectionsFinder

sections = sys.argv[1]

def main(sections):
    
    text_file = TextFileManager(sections)
    subslists = text_file.split_lines_into_sublists()

    sections = CommonSectionsFinder(subslists)
    sections_pairs_sets = sections.get_sections_sets_pairs()
    n_fully_covered_sections = sections.count_common_sections(sections_pairs_sets)

    print(n_fully_covered_sections)

    
if __name__ == "__main__":
    main(sections)
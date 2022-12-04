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
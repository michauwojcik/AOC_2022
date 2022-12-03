import sys
sys.path.append("../../Common")
from text_file_manager import TextFileManager
from rucksacks import RucksackManager, RucksacksMapper

rucksack_file_path = sys.argv[1]

def main(rucksack_file_path):
    
    text_file = TextFileManager(rucksack_file_path)
    rucksacks = RucksacksMapper(text_file.lines)
    all_items_value = rucksacks.get_all_rucksacks_value()

    print(all_items_value)


if __name__ == "__main__":
    main(rucksack_file_path)
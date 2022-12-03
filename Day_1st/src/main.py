import sys
from elf_finder import ElfFinder
from calories_group_counter import CaloriesGroupCounter
sys.path.append("../../Common")
from text_file_manager import TextFileManager


file_path = sys.argv[1]

def main(path=file_path):


    text_file = TextFileManager(path)
    inventory = CaloriesGroupCounter()
    cal_counter = ElfFinder()

    calories_group = inventory.prepare_calories_group(text_file.lines)
    cal_counter.count_group_calories(calories_group)
    max_calories, elves_index = cal_counter.find_elf_with_max_cals()

    print(f"max calories: {max_calories}, elf's number: {elves_index}")


if __name__ == "__main__":
    main()
    

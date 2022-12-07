"""
    Program which calculates the sum of small directories' size and the smallest directory which can be deleted size.

    # Task 1
    1. Reads input (shell's history)
    2. Based on shells's history creates the directories' structure.
    3. Calculates each directory's size, then calculates each directory's total size. 
    4. Finds the total size of small directories. 

    # Task 2
    5. Calculates the amount of space which must be deleted to gain enough free space for an update. 
    6. Finds the smallest directory which must be deleted to free enough space, then returns its size. 

"""


from filesystem_crawler import FileSystemCrawler, FilesDeleter
import sys
sys.path.append("../../Common")
from text_file_manager import TextFileManager

shell_output = sys.argv[1]

def main(shell_output):
    input = TextFileManager(shell_output)
    
    crawler = FileSystemCrawler(input.lines)
    crawler.create_dir_sizes_dict()
    crawler.get_dir_size()
    crawler.get_dir_total_size()
    result = crawler.get_small_directories_sizes_sum()
    print(f"Filesystem's small directories' size: {result}")
    
    deleter = FilesDeleter(crawler.total_dir_sizes)
    space_to_del = deleter.get_space_to_delete()
    result_dir = deleter.get_smallest_available_dir_size(space_to_del)

    print(f"The smallest directory which can be deleted size: {result_dir}")


if __name__ == "__main__":
    main(shell_output)
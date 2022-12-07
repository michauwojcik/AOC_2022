import os

class FileSystemCrawler:
    """
    FileSystemCrawler allows for finding directories structure based on shell's history. 
    Calculates the size of each directory (sum of directory's files' sizes).
    Also calculates the total size of each directory (sum of directory's files and subdirectories' sizes).
    """
    
    SMALL_DIR_THRESHOLD = 100_000
    

    def __init__(self, filesystem_steps: list): 
        self.filesystem_steps = filesystem_steps
        self.dir_sizes = dict()
        self.total_dir_sizes = dict()


    def create_dir_sizes_dict(self):
        """
        Get all unique paths to directories
        """
        all_directories = self.get_all_directories()
        all_paths = []
        curr_path = "/"
        for dir_ in all_directories:
            curr_path = os.path.abspath(os.path.join(curr_path, dir_))
            
            if curr_path not in all_paths:
                self.dir_sizes[curr_path] = 0
        
        
    def get_all_directories(self):
        """
        Searches in terminal's output for command 'cd' and finds directories which were accessed.

        Returns: (tuple): accessed directories in chronological order.
        """
        
        only_cds = tuple(filter(lambda x: x[:4] == "$ cd", self.filesystem_steps))
        all_directories = tuple(map(lambda x: x[5:], only_cds))
        
        return all_directories
        
    
    def get_dir_size(self):
        """
        Calculates each directory's size. 
        """
        
        curr_path = "/"
        for line in self.filesystem_steps:
            if line[:4] == "$ cd":
                curr_path = os.path.abspath(os.path.join(curr_path, line[5:]))

            if line.split()[0].isdigit():
                self.dir_sizes[curr_path] += int(line.split()[0])
        
        
    def get_dir_total_size(self):
        """
        Calculates total size of each directory (sum of subdirectories' sizes). 
        Assignes the total size to each directory.
        """
        
        self.total_dir_sizes = self.dir_sizes.copy()
        
        for k in self.dir_sizes.keys():
            for k2 in self.dir_sizes.keys():
                if (k in k2) & (k != k2):
                    self.total_dir_sizes[k] += self.dir_sizes[k2]
    
    
    def get_small_directories_sizes_sum(self):
        """
        Calculates the total size for small directories. 
        Small directories are directories whose size is smaller than SMALL_DIR_THRESHOLD

        Returns:
            (int): Sum of small directories' sizes.
        """
        
        small_dirs = list(filter(lambda x: self.total_dir_sizes[x] < self.SMALL_DIR_THRESHOLD, self.total_dir_sizes))
        result = sum(list(map(lambda x: self.total_dir_sizes[x], small_dirs)))
        
        return result
    
    
    
class FilesDeleter:
    """
    Allows for finding demanded disk space to download system's update. 
    Gives ability to find the smallest directory's size which must be deleted to gain demanded free diskspace.

    """

    TOTAL_DISK_SPACE = 70_000_000
    DEMANDED_FREE_SPACE = 30_000_000
    
    
    def __init__(self, total_dir_sizes: dict):
        self.total_dir_sizes = total_dir_sizes
        
        
    def get_space_to_delete(self):
        """
        Returns:
            (int): disk space which must be freed to have enough  space for update
        """

        free_space = self.TOTAL_DISK_SPACE - self.total_dir_sizes["/"] 
        space_to_delete = self.DEMANDED_FREE_SPACE - free_space
        
        
        return space_to_delete
    
    
    def get_smallest_available_dir_size(self, space_to_delete: dict):
        """
        Args:
            space_to_delete (dict): disk space which must be freed to have enough  space for update

        Returns:
            (int): the smallest directory's size which must be deleted to gain demanded free diskspace.
        """

        avaiable_dirs = {k: v for k,v in self.total_dir_sizes.items() if v > space_to_delete}
        dir_with_min_size = min(avaiable_dirs, key=avaiable_dirs.get)
        
        return self.total_dir_sizes[dir_with_min_size]
    
        
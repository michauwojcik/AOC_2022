""" 
    Utils managing reading and writing to files.

"""


class TextFileManager:
    def __init__(self, file_path):
        self.file_path = file_path
        self.content = self.get_file_content(file_path)
        self.lines = self.get_file_lines(file_path)


    def get_file_lines(self, file_name: str):
        """
        Returns lines of content as a list. 

        Args:
            file_name (str): a relative path to file

        Returns:
            (list): file_name's content 
        """

        with open(file_name, 'r') as f:
            lines = f.read().split("\n")

        return lines

    
    def get_file_content(self, file_name: str):
        """
        Returns lines of content as a list. 

        Args:
            file_name (str): a relative path to file

        Returns:
            (list): file_name's content 
        """

        with open(file_name, 'r') as f:
            file_content = f.read()

        return file_content

    
    def split_lines_into_sublists(self, sep=","):
        return [el.split(sep) for el in self.lines]











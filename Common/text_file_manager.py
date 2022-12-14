""" 
    Utils managing reading and writing to files.

"""


class TextFileManager:
    def __init__(self, file_path):
        self.file_path = file_path
        self.content = self.get_file_content()
        self.lines = self.get_file_lines()

    def get_file_lines(self):
        """
        Returns lines of content as a list. 

        Returns:
            (list): file_name's content 
        """

        with open(self.file_path, 'r') as f:
            lines = f.read().split("\n")

        return lines

    
    def get_file_content(self):
        """
        Returns lines of content as a list. 

        Returns:
            (list): file_name's content 
        """

        with open(self.file_path, 'r') as f:
            file_content = f.read()

        return file_content

    
    def split_lines_into_sublists(self, sep=","):
        return [el.split(sep) for el in self.lines]











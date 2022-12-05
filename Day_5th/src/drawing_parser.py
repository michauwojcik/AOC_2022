class DrawingParser:
    """
    Drawing Parser allows for parsing raw input (textfile) with drawing 
    into more programmatic structure. 

    'get_drawing_and_procedure' is a getter which returns:
        - stacks of crates (dict of lists) 
          where keys are stacks' numbers and values are crates.
          the last element in each list represents a crate on the top of the stack
        - procedure (tuple of tuples) 
          the way in which crane performs moving crates between stacks. 
          first element of each tuple is a number of crates to be moved, the second 
          - the stack from which crate is taken, and the third is the stack on which crate will be placed

    """

    def __init__(self, file_content): 
        self.file_content = file_content
        self.n_stacks = None
        self.crates_in_stacks  = None
        self.procedure = None
    

    def get_drawing_and_procedure(self):
        """
        Based on input parses drawing and procedure. 
        Drawing is returned as a dict, where keys are stacks' numbers and values are crates
        Procedure is tuple of tuples, where each tuple contains (number_of_crates, old_stack, stack_new).

        Returns:
            (dict, tuple): drawing, procedure
        """
        raw_crates_in_stacks, raw_procedure = self.split_drawing_and_procedure()
        self.parse_procedure(raw_procedure)
        self.get_number_of_stacks(raw_crates_in_stacks)
        self.parse_crates_stacks(raw_crates_in_stacks)

        return self.crates_in_stacks, self.procedure

    
    def split_drawing_and_procedure(self):
        """
        Extracts raw version of drawing and crane's procedure

        Returns:
            (list, list): each element of list represents crates on the certain level of stack, 
                          procedure splitted line by line 
        """
        raw_crates_in_stacks = self.file_content.split("\n\n")[0].split("\n")
        raw_procedure = self.file_content.split("\n\n")[1].split("\n")
        
        return raw_crates_in_stacks, raw_procedure
    
    
    def parse_procedure(self, raw_procedure:list):
        """
        Represents moving procedure as a tuple of tuples

        Args:
            procedure (list): procedure splitted line by line 
        """

        self.procedure = tuple(map(self.get_only_digits, raw_procedure))
    
    
    @staticmethod
    def get_only_digits(procedure_line: str):
        """
        Extracts only numbers from given string
        and returns it as a tuple of tuples

        Args:
            procedure_line (str): one step from procedure
        """

        return tuple(int(s) for s in procedure_line.split(" ") if s.isdigit())


    ### STACKS 
    def get_number_of_stacks(self, raw_crates_in_stacks:list):
        """
        Calculates number of stacks based on numbering in drawing. 

        Args:
            drawing (list): raw drawing splitted level by level of crates
        """

        stacks = tuple(map(self.get_only_digits, raw_crates_in_stacks))
        self.n_stacks = max(max(stacks))
    

    def parse_crates_stacks(self, raw_crates_in_stacks:list):
        """
        Create represantion of crates in stacks as a dict.
        Each stack is a list with creates ordered from bottom

        Args:
            drawing (list): raw drawing splitted level by level of crates
        """
        
        self.crates_in_stacks = dict()
        for n in range(0, self.n_stacks):
            stack = []
            for level in raw_crates_in_stacks[:-1]:
                position = level[4*n + 1]
                if position != ' ':
                    stack.append(level[4*n + 1])
            self.crates_in_stacks[n+1] = stack[::-1]
    
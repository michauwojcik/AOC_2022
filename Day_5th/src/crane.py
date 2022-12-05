class CraneDriver:
    """
    Simulates crane's moves according to given *procedure*.

    Procedure is a sequnence of instructions where each instruction is given as follows: 
    (number of crates to be moved, stack from which a crate will be taken, stack on which crate will be placed)

    Crane moves only one crate at a time, so to move n crates crane needs to perdorm n moves.

    """

    def __init__(self, procedure, crates_in_stacks): 
        self.procedure = procedure
        self.crates_in_stacks = crates_in_stacks
        

    def perform_procedure(self):
        """
        Follows the instructions given in *procedure*.
        For each instruction in procedures moves the demanded number of crates.
        """

        for i, instruction in enumerate(self.procedure):
            n_crates_to_move = instruction[0]
            for crate in range(n_crates_to_move):
                self.move_one_crate(instruction)
            
    
    def move_one_crate(self, instruction: tuple):
        """
        Performs one move. 
        Only one crates is being moved, so only *old_stack* and *new_stack* are used.

        Args:
            instruction (tuple): (number_of_crates, old_stack, new_stack)
        """

        _, old_stack, new_stack = instruction

        crate_to_move = self.crates_in_stacks[old_stack][-1]
        self.crates_in_stacks[old_stack] = self.crates_in_stacks[old_stack][:-1]
        self.crates_in_stacks[new_stack] += crate_to_move

    
    def get_top_crates(self):
        """
        Gets the crates which are on the top of each stack

        Returns:
            (str): crates on top withou spaces, e.g. 'DMZ'
        """

        top_crates = ""
        for stack in self.crates_in_stacks.keys():
            top_crate = self.crates_in_stacks[stack][-1] if self.crates_in_stacks[stack] else ""
            top_crates += top_crate

        return top_crates



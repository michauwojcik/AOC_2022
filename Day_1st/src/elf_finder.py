

class ElfFinder:
    """
    Class allows to find an elf (or elves) with maximum calories from whole inventory
    and to find their number 

    """

    def __init__(self):
        self.cal_groups = []

    def count_group_calories(self, inventory_lines: list):
        """
        Sums calories in each group. 
        cal_groups is a list of calories' sums. 

        Args:
            inventory_lines (list): lines of elves' inventory
        """

        cal_counter = 0

        for line in inventory_lines:
            if line == "":
                self.cal_groups.append(cal_counter)
                cal_counter = 0
            else:
                cal_counter += line
        
        if line != "":
            self.cal_groups.append(cal_counter)
    

    def find_elf_with_max_cals(self):
        """
        Gets the index of Elve who has the max calories.
        If two (or more) Elves have the maximum value of calories return their number

        Returns:
            (int, int): maximum of calories, index of elves with maximum calories
        """

        max_calories = max(self.cal_groups)
        elves_index = [index + 1 for index, calories in enumerate(self.cal_groups) if calories == max_calories]
        elves_index = elves_index[0] if len(elves_index) == 1 else elves_index

        return max_calories, elves_index



                





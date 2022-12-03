import string


class RucksackManager:
    """
    Operates on a particualar rucksack (one line of a given textfile)
    and gets the rucksack's value. 
    """

    def __init__(self, rucksack: str):
        self.rucksack = rucksack
        self.item_dict = self.create_item_dict()
        self.test_rucksack_length()


    @staticmethod
    def create_item_dict():
        """
        Assigns corresponding value to each letter from alphabet.
        'a' gets 1, ..., 'z' gets 26, 'A' gets 27, ..., 'Z' gets 52
        """

        return {letter: value + 1 for value, letter in enumerate(string.ascii_letters)}
    
    
    def test_rucksack_length(self):
        """Length of a given rucksack must be even."""
        assert len(self.rucksack) % 2 == 0, "Rucksack's length is not even."


    def get_rucksack_value(self):
        """
        Calculates a particular rucksuck's value
        """

        first_half, second_half = self.split_rucksack_in_half(self.rucksack)
        rucksack_value = self.get_value_of_common_items(first_half, second_half)

        return rucksack_value


    def split_rucksack_in_half(self, rucksuck: str):
        """
        Splits a given *rucksuck* into two pieces of equal length

        Args:
            rucksuck (str): all items in a certain rucksuck

        Returns:
            (set, set): a rucksuck splitted in half 
        """

        half_index = int(len(rucksuck) / 2) 

        first_half = {item for item in rucksuck[:half_index]}
        second_half = {item for item in rucksuck[half_index:]}

        return first_half, second_half

    
    def get_value_of_common_items(self, first_half: set, second_half: set):
        """
        Sums the value of items which occur in both halfs

        Args:
            first_half (set): the rucksack's first half of items
            second_half (set): the rucksack's second half of items

        Returns:
            (int): common items' value
        """

        common_items = first_half & second_half
        common_items_value = sum(self.item_dict[item] for item in common_items)

        return common_items_value



class RucksacksMapper:
    """
    Operates on a list of rucksacks (whole text file)
    and gets the total sum of all rucksacks 
    """

    def __init__(self, all_rucksacks: list):
        self.all_rucksacks = all_rucksacks

    def get_all_rucksacks_value(self):
        rucksacks_values = self.get_each_rucksack_value()
        return sum(rucksacks_values)

    def get_each_rucksack_value(self):
        rucksacks_values = (RucksackManager(rucksack).get_rucksack_value() for rucksack in self.all_rucksacks)

        return rucksacks_values
    


    
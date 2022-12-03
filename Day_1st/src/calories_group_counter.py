class CaloriesGroupCounter:
    """
    Sums calories in each inventory's group
    """

    def prepare_calories_group(self, lines: list):
        """
        Returns lines of content as a list. 

        Args:
            file_name (str): a relative path to file

        Returns:
            (list): file_name's content 
        """

        lines = self.replace_values_in_list(lines, "\n", "")
        lines = [self.convert_to_int(l) for l in lines]

        return lines


    def convert_to_int(self, variable: str):
        return int(variable) if variable != "" else variable 


    def replace_values_in_list(self, list_: list, item_to_replace: str, new_item: str):
        """
        Replaces *item_to_replace* in *list_* for a *new_item*.
    
        Args:
            list_ (list): list with items to be replaced 
            item_to_replace (str): item which should be replace
            new_item (str): a new value for item 
    
        Returns:
            (list): list with replace values
        """
    
        for i, el in enumerate(list_):
            list_[i]  = el.replace(item_to_replace, new_item)
            
        return list_








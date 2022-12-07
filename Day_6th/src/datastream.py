
class DatastreamReceiver:
    """
    Allows for finding starting point for message and packet in given datastream buffer.    
    """
    
    def __init__(self, datastream, window_size): 
        self.datastream = datastream
        self.window_size = window_size


    def find_starting_index(self):
        """
        Iterates over letters in datastream and counts unique characters in sliding window. 
        When all characters in window are unique in window the loop iterating stops.
        Returns the index which is the starting point for packet or message.

        Returns:
            (int): starting point index
        """
        
        indeces_to_iter = len(self.datastream) - self.window_size + 1
        for i in range(indeces_to_iter):
            n_uniq_chars = self.count_unique_characters(i)
            if n_uniq_chars == self.window_size:
                return i + self.window_size
                break


    def count_unique_characters(self, index: int):
        """
        Count unique characters in given window.

        Args:
            index (int): index from which start counting in datastream buffer.

        Returns:
            (int): number of uniq characters in given window 
        """
        
        characters_in_window = self.datastream[index:(index + self.window_size)]
        
        return len(set(characters_in_window))
        


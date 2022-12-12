import numpy as np
from cartesian_coordinates_system import CartesianCoordinateSystem

system = CartesianCoordinateSystem()

class TailTracker:
    """
    Finds tail's position
    """

    OPPOSITE_DIRECTIONS = {"R": "L", "L": "R", "U": "D", "D": "U"}

    def __str__(self):
        head_position = f"Current head's position: {self.curr_head_position}\n"
        tail_position = f"Current tail's position: {self.curr_tail_position}\n"
            
        return head_position + tail_position
            
    
    def __init__(self, moves: list):
        self.moves = self.parse_moves(moves)
        self.curr_head_position = system.ORIGIN.copy()
        self.curr_tail_position = system.ORIGIN.copy()
        self.tail_moving_history = []
        
    
    def parse_moves(self, moves: list):
        """
        Represents moves as a list of tuples, where each tuple is a move. 

        Args:
            moves (list): all moves to be taken by head. 

        Returns:
            tuple: tuple of tuples. Each tuple is a move 
                   and its first element is a direction and the second element is a number of position to move
        """
        return tuple((i[0], int(i[-1])) for i in moves)
    

    def move(self):
        """
        Simulates all head and tail's moves.
        Firstly head moves and its current position is calculated (after move).
        Then tail moves and its current and starting position is calculated (before and after move).

        Determining the positions visited by the tail starts with its current position (after move). 
        The visited position is changed by one field in the opposite direction to the direction of movement. 
        When the visited position is in the neighborhood of the tail's starting point, 
        the loop is broken and the tail's initial position is added to the visited positions.
        """

        for i, move in enumerate(self.moves):
            tmp_tail_history = []
            direction = move[0]
            self.find_head_pos_after_move(move)
            tail_pos_start = self.curr_tail_position.copy()
            self.find_tail_pos_after_move(move)

            pos_tmp = self.curr_tail_position.copy()
            print(i, move)
            print("parameters")
            print("self.curr_head_position: ", self.curr_head_position)
            print("self.curr_tail_position: ", self.curr_tail_position)
            print("tail start: ", tail_pos_start)

            while system.check_point_neighborhood(tail_pos_start, pos_tmp) is False:
                visited_position = tuple(pos_tmp.tolist())
                self.tail_moving_history.append(visited_position)
                tmp_tail_history.append(visited_position)
                pos_tmp += system.get_unit_vector(self.OPPOSITE_DIRECTIONS[direction])

            self.tail_moving_history.append(tuple(pos_tmp.tolist()))
            tmp_tail_history.append(tuple(pos_tmp.tolist()))

            self.tail_moving_history.append(tuple(tail_pos_start.tolist()))
            tmp_tail_history.append(tuple(tail_pos_start.tolist()))

            print(f"tmp_tail_history: {tmp_tail_history} \n")

    
    def count_visited_positions(self):
        return len(set(self.tail_moving_history))

    
    def plot_visited_positions(self):
        """
        Visualizes positions visited by tail.
        """

        from matplotlib import pyplot as plt
        x = [el[0] for el in set(self.tail_moving_history)]
        y = [el[1] for el in set(self.tail_moving_history)]
        plt.title("Matplotlib demo") 
        plt.xlabel("x axis caption") 
        plt.ylabel("y axis caption") 
        plt.scatter(x,y) 
        plt.show()


    def find_head_pos_after_move(self, move):
        """
        Updates head's current position after each move

        Args:
            move (tuple): first element is a direction, the second is numbe of positions head moves. 
        """
        self.curr_head_position += system.create_vector(*move)

    
    def find_tail_pos_after_move(self, move: tuple):
        """
        Updates tail's current position after each move.
        Head's move must be done first. 
        If head moves 0 positions tail's position does not change.
        If head moves 1 position, but head is still in tail's neihborhood tail's position also does not change. 

        Args:
            move (tuple): first element is a direction, the second is numbe of positions head moves. 
        """
        
        direction, steps = move
        opposite_direction = self.OPPOSITE_DIRECTIONS[direction]

        if steps == 0:
            pass
        elif system.check_point_neighborhood(self.curr_head_position, self.curr_tail_position) is True:
            pass
        else:
            self.curr_tail_position = self.curr_head_position + system.get_unit_vector(opposite_direction)


    def check_tail_neighborhood(self, starting_point: tuple):
        """
        Checks whether tail's position afters move is in the neighbourhood of tail's position before move. 
        """

        if abs(self.curr_tail_position[0] - starting_point[0] <= 1) & abs(self.curr_tail_position[0] - starting_point[0] <= 1):
            return True

        return False


    
    ## może wydzielić do oddzielnej klasy?:

        
        
        

        
        
        

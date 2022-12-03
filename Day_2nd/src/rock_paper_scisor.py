""" 
    Opponent:
    - A for Rock
    - B for Paper
    - C for Scissors
    
    You:
    - X for Rock
    - Y for Paper
    - Z for Scissors

    Scoring:
        - 1 for Rock
        - 2 for Paper
        - 3 for Scissors
        
        - 0 if you lost
        - 3 if the round was a draw
        - 6 if you won
"""

ALL_GAMES =  {
    # WINS:
    "C X": 7, "A Y": 8, "B Z": 9, 
    # DRAWS
    "A X": 4, "B Y": 5, "C Z": 6, 
    # LOSES
    "B X": 1, "C Y": 2, "A Z": 3
}
    
    
def get_points_whole_game(strategy: list):
    """
    Counts points you earn in each game
    and returns a sum of point.

    Args:
        strategy (list[str]): each element represents round of the game 

    Returns:
        int: sum of points gained in whole game 
    """
    
    each_game_points = list(map(lambda x: ALL_GAMES[x], strategy))
    
    return sum(each_game_points)
    
    

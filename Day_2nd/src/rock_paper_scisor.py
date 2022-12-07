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

ALL_GAMES_TASK_2 =  {
    # WINS:
    "A Z": 8,  "B Z": 9,  "C Z": 7,
    # DRAWS
    "A Y": 4,  "B Y": 5,  "C Y": 6,
    # LOSES
    "A X": 3,  "B X": 1,  "C X": 2
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
    
    
def get_points_whole_game_second_version(strategy: list):
    """
    Counts points you earn in each game
    and returns a sum of point.

    Args:
        strategy (list[str]): each element represents round of the game 

    Returns:
        int: sum of points gained in whole game 
    """
    
    each_game_points = list(map(lambda x: ALL_GAMES_TASK_2[x], strategy))
    
    return sum(each_game_points)
    
import sys
from rock_paper_scisor import get_points_whole_game
sys.path.append("../../Common")
from text_file_manager import TextFileManager

strategy_file_path = sys.argv[1]

def main(strategy_file_path):
    
    text_file = TextFileManager(strategy_file_path)
    points = get_points_whole_game(text_file.lines)
    
    print(points)
    return points
    
if __name__ == "__main__":
    main(strategy_file_path)
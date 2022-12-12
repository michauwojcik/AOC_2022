from tail_tracker import TailTracker
import sys
sys.path.append("../../Common")
from text_file_manager import TextFileManager

moves = sys.argv[1]

def main(input_file):
    input = TextFileManager(input_file)
    
    tracker = TailTracker(input.lines)
    
    tracker.move()
    print(tracker.count_visited_positions())
    tracker.plot_visited_positions()
    # print(tracker.tail_moving_history)


if __name__ == "__main__":
    main(moves)
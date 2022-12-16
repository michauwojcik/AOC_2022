""" 

"""

from monkey_catcher import MonkeyCatcher
import sys
sys.path.append("../../Common")
from text_file_manager import TextFileManager

notes = sys.argv[1]

def main(notes):
    input = TextFileManager(notes)
    
    monkeys = MonkeyCatcher(input.content)
    monkeys.parse_monkeys()

    print(f"Monkeys attributes:\n ")
    for k in monkeys.monkeys_attributes.keys():
        print(monkeys.monkeys_attributes[k])
    # print(f"Forest plan: \n{forest}")
    monkeys.play_monkey_game()
    print(monkeys.find_monkeys_business())

    # TASK 2
    div = 3
    while monkeys.find_monkeys_business() != 2_713_310_158:
        monkeys = MonkeyCatcher(input.content)
        monkeys.DIVISOR = div
        monkeys.play_monkey_game()
        for k in monkeys.monkeys_attributes.keys():
            print(monkeys.monkeys_attributes[k])
        div += 1
        print(f"Div: {div}, Monkeys' business: {monkeys.find_monkeys_business()}")

    print("Final:")
    print(f"Div: {div}, Monkeys' business: {monkeys.find_monkeys_business()}")



if __name__ == "__main__":
    main(notes)
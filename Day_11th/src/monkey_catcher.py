from math import floor

class MonkeyCatcher:
    ROUNDS = 10_000
    DIVISOR = 3
    N_MOST_ACTIVE_MONKEYS = 2 

    def __init__(self, notes_raw: str):
        self.notes_raw = notes_raw
        self.monkeys_attributes = {}

    
    def parse_monkeys(self):
        """
        Creates dictionary with monkeys and theris properties.
        Firstly just extracts information from textfile (*notes_raw*)
        Then creates proper data structures and converts types.
        """

        each_monkey = [m.split("\n") for m in self.notes_raw.split("\n\n")]
        self.monkeys_attributes = {i: {} for i, _ in enumerate(each_monkey)}

        # Extract from textfile 
        for i, m in enumerate(each_monkey):
            self.monkeys_attributes[i]["items"] = list(filter(lambda x: x.isdigit(), m[1].replace(",", " ").split(" ")))
            self.monkeys_attributes[i]["operation"] = m[2].split("Operation: new = old ")[1]
            self.monkeys_attributes[i]["test"] = list(filter(lambda x: x.isdigit(), m[3].split(" ")))
            self.monkeys_attributes[i]["if_true"] = list(filter(lambda x: x.isdigit(), m[4].split(" ")))
            self.monkeys_attributes[i]["if_false"] = list(filter(lambda x: x.isdigit(), m[5].split(" ")))

        # Assure proper types and structure
        for i, m in enumerate(each_monkey):
            self.monkeys_attributes[i]["items"] = [int(item) for item in self.monkeys_attributes[i]["items"]]

            operation, multiplier = self.monkeys_attributes[i]["operation"].replace("* old", "** 2").split(" ")
            self.monkeys_attributes[i]["operation"] = (operation, multiplier)
            
            self.monkeys_attributes[i]["test"] = int(self.monkeys_attributes[i]["test"][0])
            self.monkeys_attributes[i]["if_true"] = int(self.monkeys_attributes[i]["if_true"][0])
            self.monkeys_attributes[i]["if_false"] = int(self.monkeys_attributes[i]["if_false"][0])

            self.monkeys_attributes[i]["inspected_items_number"] = 0


    def play_monkey_game(self):
        """
        Simulates whole monkeys' game with *self.ROUNDS* rounds.
        """

        for round in range(self.ROUNDS):
            print(f'Round: {round} \n')
            for i_monkey, monkey in enumerate(self.monkeys_attributes):
                self.one_monkey_inspection(monkey_number=i_monkey)


    def one_monkey_inspection(self, monkey_number: int):
        """
        Simulates actions perfmored by one monkey in a round.

        Args:
            monkey_number (int): monkey's index 
        """

        for item in self.monkeys_attributes[monkey_number]["items"]:
            self.monkeys_attributes[monkey_number]["inspected_items_number"] += 1
            worry_level_monkey_bored = self.perform_operation(item, monkey_number)

            if worry_level_monkey_bored % self.monkeys_attributes[monkey_number]["test"] == 0:
                new_monkey_number = self.monkeys_attributes[monkey_number]["if_true"]
                self.monkeys_attributes[new_monkey_number]["items"].append(worry_level_monkey_bored)
                self.monkeys_attributes[monkey_number]["items"] = self.monkeys_attributes[monkey_number]["items"][1:]
            else:
                new_monkey_number = self.monkeys_attributes[monkey_number]["if_false"]
                self.monkeys_attributes[new_monkey_number]["items"].append(worry_level_monkey_bored)
                self.monkeys_attributes[monkey_number]["items"] = self.monkeys_attributes[monkey_number]["items"][1:]


    def perform_operation(self, item_worry_level: int, monkey_number: int):
        """
        Based on monkeys' atrributes' "operation" calculates worry level after monkey playing with the item.

        Args:
            item_worry_level (int): starting worry level
            monkey_number (int): monkey's index 

        Returns:
            (int): item's worry level when monkey is bored with the item
        """

        sign = self.monkeys_attributes[monkey_number]["operation"][0]
        number = self.monkeys_attributes[monkey_number]["operation"][1]

        worry_level_tmp = eval(f"{item_worry_level} {sign} {number}")
        
        monkey_bored_worry_level = floor(worry_level_tmp / self.DIVISOR)

        return monkey_bored_worry_level


    def find_monkeys_business(self):
        """
        Calculates monkeys' business for two monkeys which were most active. 
        Most active means they interacted with the largest number of items.

        Returns:
            (int): most active monkeys' business
        """


        inspected_items = {i: self.monkeys_attributes[i]['inspected_items_number'] for i in self.monkeys_attributes.keys()}

        most_active_monkeys = {}
        monkey_business = 1
        for _ in range(self.N_MOST_ACTIVE_MONKEYS):
            key = max(inspected_items, key=inspected_items.get)
            most_active_monkeys[key] = inspected_items[key]
            monkey_business *= inspected_items[key]
            del inspected_items[key]

        
        return monkey_business





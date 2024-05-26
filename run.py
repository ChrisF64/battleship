# Functions to randomly populate playing field

import random
distribution = ["horizontal", "vertical"]
up_down = ["up", "down"]
left_right = ["left", "right"]
def select_random_field(selection):
    return random.choice(selection)
def select_random_distribution():
    return random.choice(distribution)
def select_random_up_down():
    return random.choice(up_down)
def select_random_left_right():
    return random.choice(left_right)

# Playing board class

class Playfield :

    #Creates an instance of a playing board
    def __init__(self):
        self.empty = """
         ____ ____ ____ ____ ____ ____ ____ ____ ____ ____
        |    |    |    |    |    |    |    |    |    |    |
        | A0 | A1 | A2 | A3 | A4 | A5 | A6 | A7 | A8 | A9 |
        |____|____|____|____|____|____|____|____|____|____|
        |    |    |    |    |    |    |    |    |    |    |
        | B0 | B1 | B2 | B3 | B4 | B5 | B6 | B7 | B8 | B9 |
        |____|____|____|____|____|____|____|____|____|____|
        |    |    |    |    |    |    |    |    |    |    |
        | C0 | C1 | C2 | C3 | C4 | C5 | C6 | C7 | C8 | C9 |
        |____|____|____|____|____|____|____|____|____|____|
        |    |    |    |    |    |    |    |    |    |    |
        | D0 | D1 | D2 | D3 | D4 | D5 | D6 | D7 | D8 | D9 |
        |____|____|____|____|____|____|____|____|____|____|
        |    |    |    |    |    |    |    |    |    |    |
        | E0 | E1 | E2 | E3 | E4 | E5 | E6 | E7 | E8 | E9 |
        |____|____|____|____|____|____|____|____|____|____|
        |    |    |    |    |    |    |    |    |    |    |
        | F0 | F1 | F2 | F3 | F4 | F5 | F6 | F7 | F8 | F9 |
        |____|____|____|____|____|____|____|____|____|____|
        |    |    |    |    |    |    |    |    |    |    |
        | G0 | G1 | G2 | G3 | G4 | G5 | G6 | G7 | G8 | G9 |
        |____|____|____|____|____|____|____|____|____|____|
        |    |    |    |    |    |    |    |    |    |    |
        | H0 | H1 | H2 | H3 | H4 | H5 | H6 | H7 | H8 | H9 |
        |____|____|____|____|____|____|____|____|____|____|
        |    |    |    |    |    |    |    |    |    |    |
        | I0 | I1 | I2 | I3 | I4 | I5 | I6 | I7 | I8 | I9 |
        |____|____|____|____|____|____|____|____|____|____|
        |    |    |    |    |    |    |    |    |    |    |
        | J0 | J1 | J2 | J3 | J4 | J5 | J6 | J7 | J8 | J9 |
        |____|____|____|____|____|____|____|____|____|____|
        """

        self.rows = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
        self.columns = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        self.fields = [self.rows[i] + column for i in range(10) for column in self.columns]

    # Populates the board and returns a list of occupied spaces as well as a list containing all placed ships.
    def populate(self, ship_list):
        available_fields = self.fields.copy()
        occupied_fields = []
        for ship in ship_list:
            while ship.is_occupied(available_fields):
                ship.place(self.fields)
            occupied_fields += ship.fields
            ship.remove(available_fields)
        return occupied_fields, ship_list

    # Updates board appearance after each player move
    def update(self, hit_list, miss_list):
        update = self.empty
        for field in hit_list:
            update = update.replace( " " + field + " ", "@@@@")
        for field in miss_list:
            update = update.replace(" " + field + " ", "----")
        return update
        
    # Updates board appearance to show where ships are located
    def solution(self, occupied_fields):
        solution = self.empty
        for field in self.fields:
            if field in occupied_fields:
                solution = solution.replace(" " + field + " ", "@@@@")
            else:
                solution = solution.replace(" " + field + " ", "----")
        return solution


# Ship class
class Ship:
    
    # Creates an instance of a ship in the form of a list containing the pre-defined number of fields
    def __init__(self, size):
        self.size = size
        self.fields = []
        for i in range(size):
            self.fields.append("")
    
    # Randomly places ship on the playing board
    def place(self, playing_fields):
        self.playing_fields = playing_fields
        self.fields[0] = select_random_field(playing_fields)
        if self.size > 1:     
            index_counter = playing_fields.index(self.fields[0])
            dist = select_random_distribution()
            if dist == "horizontal":
                if str(self.size-2) in self.fields[0] or str(self.size-3) in self.fields[0] or str(self.size-4) in self.fields[0]:
                    dir = "right"
                elif str(11-self.size) in self.fields[0] or str(12-self.size) in self.fields[0] or str(13-self.size) in self.fields[0]:
                    dir = "left"
                else:
                    dir = select_random_left_right()
                for i in range(self.size-1):
                    if dir == "right":
                        index_counter += 1
                        self.fields[i+1] = playing_fields[index_counter]
                    else:
                        index_counter -=1
                        self.fields[i+1] = playing_fields[index_counter]
            else:
                if index_counter < (self.size-1)*10:
                    dir = "down"
                elif index_counter > (len(playing_fields)-1) - (self.size-1)*10:
                    dir = "up"
                else:
                    dir = select_random_up_down()
                for i in range(self.size-1):
                    if dir == "down":
                        index_counter += 10
                        self.fields[i+1] = playing_fields[index_counter]
                    else:
                        index_counter -=10
                        self.fields[i+1] = playing_fields[index_counter]
        return self.fields
    
    # Remove the fields occupied by the ship and surrounded no longer selectable fields from the available fields
    def remove(self, from_fields):
        fields_to_be_removed = []
        available_fields = Playfield().fields
        for i in range(self.size):
            idx = available_fields.index(self.fields[i])
            if self.fields[i] == "A0":
                fields_to_be_removed += [available_fields[idx], available_fields[idx+1], available_fields[idx+10], available_fields[idx+11]]
            elif self.fields[i] == "J9":
                fields_to_be_removed += [available_fields[idx], available_fields[idx-1], available_fields[idx-10], available_fields[idx-11]]
            elif "A" in self.fields[i]:
                fields_to_be_removed += [available_fields[idx], available_fields[idx-1], available_fields[idx+1], available_fields[idx+9], available_fields[idx+10], available_fields[idx+11]]
            elif "J" in self.fields[i]:
                fields_to_be_removed += [available_fields[idx], available_fields[idx-1], available_fields[idx-9], available_fields[idx-10], available_fields[idx-11], available_fields[idx+1]]
            elif "0" in self.fields[i]:
                fields_to_be_removed += [available_fields[idx], available_fields[idx-9], available_fields[idx-10], available_fields[idx+1], available_fields[idx+10], available_fields[idx+11]]
            elif "9" in self.fields[i]:
                fields_to_be_removed += [available_fields[idx], available_fields[idx-1], available_fields[idx-10], available_fields[idx-11], available_fields[idx+9], available_fields[idx+10]]
            else:
                fields_to_be_removed += [available_fields[idx], available_fields[idx-1], available_fields[idx-9], available_fields[idx-10], available_fields[idx-11], available_fields[idx+1], available_fields[idx+9], available_fields[idx+10], available_fields[idx+11]]
        for field in fields_to_be_removed:
            if field in from_fields:
                from_fields.pop(from_fields.index(field))
        return from_fields

    # Check if the fields selected for the ship are already occupied
    def is_occupied(self, available_fields):
        return any(field not in available_fields for field in self.fields)

#Intro and Welcome Screen

print(
        """\
    \u001b[33m
               ____        _   _   _           _     _           
              |  _ \      | | | | | |         | |   (_)          
              | |_) | __ _| |_| |_| | ___  ___| |__  _ _ __ 
              |  _ < / _` | __| __| |/ _ \/ __| '_ \| | '_ \ 
              | |_) | (_| | |_| |_| |  __/\__ \ | | | | |_) |
              |____/ \__,_|\__|\__|_|\___||___/_| |_|_| .__/
                                                      | |        
                                                      |_| 
    \u001b[0m       
    """
    )

welcome_msg = "\nWelcome to Battleship\n"

print(welcome_msg)
input("Press ENTER to start")
player1 = input("\nSo, you want to play Battleship? Please enter your name!\n> ")
while player1 == "":
    player1 = input("\nPlease, enter your name.\n> ")
else:
    print(f"\nOk then, {player1}, let's begin.\n")

rules = """ 
10 ships will be hidden on the play board. Together, they occupy a total of 20 fields.
Ships will be distributed horizontally or vertically, but not diagonally.
No ship will touch another (not even diagonally).
The placed ships will comprise of:
- 1 carrier (4 fields)
- 2 battleships (3 fields each)
- 3 carriers (2 fields each)
- 4 destroyers (1 field each)
You will be notified once you have sunk a ship.
Depending on the difficulty level you will have 80, 70, 60 or 50 missiles in total.
You must sink all ships to win.
"""

answer_rules = input(f"\nAre you familiar with the rules of the game {player1}? (y/n)\n> ").lower()
while answer_rules != "y" and answer_rules != "n":
    answer_rules = input("\nCome again? Please enter y for yes or n for no.\n> ").lower()
else:
    if answer_rules == "y":
        print("\nOK, we are good to go.")    
    else:
        print(rules)
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
input("Press ENTER to start\n>")
player = input("\nSo, you want to play Battleship? Let's begin by entering your name...\n> ")
while player == "":
    player = input("\n\u001b[31m Please, enter your name... \u001b[0m\n> ")
else:
    print(f"\nOk then {player}, let's get started...\n")

rules = """ 
10 ships will be hidden on the play board. Together, they occupy a total of 20 fields.
Ships will be distributed horizontally or vertically, but not diagonally.
No ship will touch another.
Ships on the play board will comprise of:
- 1 carrier (4 fields)
- 2 battleships (3 fields each)
- 3 carriers (2 fields each)
- 4 destroyers (1 field each)
You will be notified once you have sunk a ship.
Depending on the chosen difficulty level, you will have 80, 70, 60 or 50 missiles to use.
You must sink all ships to win.
"""

answer_rules = input(f"\nAre you familiar with the rules of the game {player}? (y/n)\n> ").lower()
while answer_rules != "y" and answer_rules != "n":
    answer_rules = input("\nPlease enter y for yes or n for no.\n> ").lower()
else:
    if answer_rules == "y":
        print("\n\u001b[32mPrepare to launch missiles...\u001b[0m")    
    else:
        print(rules)

# Game functionality

def battleship_game(play_count=0, won_count=0, lost_count=0):
    
    # Sets up playing board and creates empty fleet of ships

    playing_field = Playfield()
    playing_fields = playing_field.fields

    car = Ship(4)
    bat_1 = Ship(3)
    bat_2 = Ship(3)
    cru_1 = Ship(2)
    cru_2 = Ship(2)
    cru_3 = Ship(2)
    des_1 = Ship(1)
    des_2 = Ship(1)
    des_3 = Ship(1)
    des_4 = Ship(1)

    empty_fleet = [car, bat_1, bat_2, cru_1, cru_2, cru_3, des_1, des_2, des_3, des_4]

    # Populates playing field and determines position of ships

    occupied_fields, fleet = playing_field.populate(empty_fleet)

    carrier = fleet[0].fields
    battleship_1 = fleet[1].fields
    battleship_2 = fleet[2].fields
    battleships = battleship_1 + battleship_2
    cruiser_1 = fleet[3].fields
    cruiser_2 = fleet[4].fields
    cruiser_3 = fleet[5].fields
    cruisers = cruiser_1 + cruiser_2 + cruiser_3
    destroyers = fleet[6].fields + fleet[7].fields + fleet[8].fields + fleet[9].fields

    hit_list = []
    miss_list = []
    total_missiles = 0
    total_hits = 0
    num_missiles = 0

    # Main body of the game

    difficulty_levels = ["1", "2", "3", "4"]
    selection = input("\nHow difficult would you like the game to be?\nEasy (1), Medium (2), Hard (3) or Extreme (4)?\n> ")
    while selection not in difficulty_levels:
        selection = input("\n\u001b[31m Incorrect input. Please, type 1 for Easy, 2 for Medium, 3 for Hard or 4 for Extreme.\u001b[0m\n> ")
    else:
        difficulty = int(selection)
    if difficulty == 1:
        print(f"\nWise decision {player}. Take it slow in the beginning.")
        num_missiles = 80
    if difficulty == 2:
        print(f"\nLet's see how good your skills are {player}.")
        num_missiles = 70
    if difficulty == 3:
        print(f"\nBrave decision {player}!")
        num_missiles = 60
    if difficulty == 4:
        print(f"\nSo, you're an expert {player}?")
        num_missiles = 50

    input("\n\u001b[32mPress ENTER to set up playing field GOOD HUNTING!\u001b[0m\n>")
    print(playing_field.empty)
    print("\nEnemy ships are well hidden.\nIf you would like to review the rules at any point, enter '?'.\nEnter the coordinates of your first target.")

    # Gets player input, checks it against game conditionals and gives appropriate feedback to player
    
    for i in range(num_missiles):
        target = input("> ").upper()
        outcome = ""
        message = ""
        if target == "?":
            outcome = "RULES"
            message = rules
            total_missiles -= 1
        elif target in hit_list or target in miss_list:
            outcome = "ALREADY DESTROYED"
            message = "You have already hit this target."
        elif target not in playing_fields:
            outcome = "INCORRECT COORDINATES"
            message = "Your coordinates are outside the target area. Try again."
        elif target in occupied_fields:
            outcome = "HIT"
            hit_list.append(target)
            total_hits += 1
        else:
            outcome = "MISS"
            miss_list.append(target)
        total_missiles +=1
        print(f"\n*** {outcome} ***")
        if outcome == "HIT":
            if target in destroyers:
                print("*** SHIP SUNK ***")
                print("You have sunk one enemy destroyer.")
                if all(field in hit_list for field in destroyers):
                    print("All destroyers down.")
            elif target in cruiser_1:
                if all(field in hit_list for field in cruiser_1):
                    print("*** SHIP SUNK ***")
                    print("You have sunk one enemy cruiser.")
                    if all(field in hit_list for field in cruisers):
                        print("All cruisers down.")
            elif target in cruiser_2:
                if all(field in hit_list for field in cruiser_2):
                    print("*** SHIP SUNK ***")
                    print("You have sunk one enemy cruiser.")
                    if all(field in hit_list for field in cruisers):
                        print("All cruisers down.")
            elif target in cruiser_3:
                if all(field in hit_list for field in cruiser_3):
                    print("*** SHIP SUNK ***")
                    print("You have sunk one enemy cruiser.")
                    if all(field in hit_list for field in cruisers):
                        print("All cruisers down.")
            elif target in battleship_1:
                if all(field in hit_list for field in battleship_1):
                    print("*** SHIP SUNK ***")
                    print("You have sunk one enemy battleship.")
                    if all(field in hit_list for field in battleships):
                        print("All battleships down.")
            elif target in battleship_2:
                if all(field in hit_list for field in battleship_2):
                    print("*** SHIP SUNK ***")
                    print("You have sunk one enemy battleship.")
                    if all(field in hit_list for field in battleships):
                        print("All battleships down.")
            else:
                if all(field in hit_list for field in carrier):
                    print("*** SHIP SUNK ***")
                    print("You have sunk an enemy carrier.")
        else:
            print(message)        
        print(playing_field.update(hit_list, miss_list))

        if total_hits == 0:
            if total_missiles == 1:
                print("You have launched " + str(total_missiles) + " missile, " + str(num_missiles-total_missiles) + " missiles left.")
                print("So far your missiles haven't hit any enemy ships.")
                print(str(len(occupied_fields)-total_hits) + " more hits needed to win this battle.\n")
                print("Enter coordinates for your next target.")
            elif total_missiles == num_missiles-1:
                print("You have launched " + str(total_missiles) + " missiles, " + str(num_missiles-total_missiles) + " missile left.")
                print("So far your missiles haven't hit any enemy ships.")
                print(str(len(occupied_fields)-total_hits) + " more hits needed to win this battle.\n")
                print("Enter coordinates for your next target.")
            else:
                print("You have launched " + str(total_missiles) + " missiles, " + str(num_missiles-total_missiles) + " missiles left.")
                print("So far your missiles haven't hit any enemy ships.")
                print(str(len(occupied_fields)-total_hits) + " more hits needed to win this battle.\n")
                if total_missiles == num_missiles:
                    continue
                else:
                    print("Enter coordinates for your next target.")
        elif total_hits == 1:
            if total_missiles == 1:
                print("You have launched " + str(total_missiles) + " missile, " + str(num_missiles-total_missiles) + " missiles left.")
                print("So far your missiles hit enemy ships once.")
                print(str(len(occupied_fields)-total_hits) + " more hits needed to win this battle.\n")
                print("Enter coordinates for your next target.")
            elif total_missiles == num_missiles-1:
                print("You have launched " + str(total_missiles) + " missiles, " + str(num_missiles-total_missiles) + " missile left.")
                print("So far your missiles hit enemy ships once.")
                print(str(len(occupied_fields)-total_hits) + " more hits needed to win this battle.\n")
                print("Enter coordinates for your next target.")
            else:
                print("You have launched " + str(total_missiles) + " missiles, " + str(num_missiles-total_missiles) + " missiles left.")
                print("So far your missiles hit enemy ships once.")
                print(str(len(occupied_fields)-total_hits) + " more hits needed to win this battle.\n")
                if total_missiles == num_missiles:
                    continue
                else:
                    print("Enter coordinates for your next target.")
        elif total_hits == 2:
            if total_missiles == 1:
                print("You have launched " + str(total_missiles) + " missile, " + str(num_missiles-total_missiles) + " missiles left.")
                print("Your missiles hit enemy ships twice.")
                print(str(len(occupied_fields)-total_hits) + " more hits needed to win this battle.\n")
                print("Enter coordinates for your next target.")
            elif total_missiles == num_missiles-1:
                print("You have launched " + str(total_missiles) + " missiles, " + str(num_missiles-total_missiles) + " missile left.")
                print("So far your missiles hit enemy ships twice.")
                print(str(len(occupied_fields)-total_hits) + " more hits needed to win this battle.\n")
                print("Enter coordinates for your next target.")
            else:
                print("You have launched " + str(total_missiles) + " missiles, " + str(num_missiles-total_missiles) + " missiles left.")
                print("So far your missiles hit enemy ships twice.")
                print(str(len(occupied_fields)-total_hits) + " more hits needed to win this battle.\n")
                if total_missiles == num_missiles:
                    continue
                else:
                    print("Enter coordinates for your next target.")
        elif total_hits == 19:
            if total_missiles == 1:
                print("You have launched " + str(total_missiles) + " missile, " + str(num_missiles-total_missiles) + " missiles left.")
                print("So far your missiles hit enemy ships " + str(total_hits) + " times: " + str(hit_list))
                print(str(len(occupied_fields)-total_hits) + " more hit needed to win this battle.\n")
                print("Enter coordinates for your next target.")
            elif total_missiles == num_missiles-1:
                print("You have launched " + str(total_missiles) + " missiles, " + str(num_missiles-total_missiles) + " missile left.")
                print("So far your missiles hit enemy ships " + str(total_hits) + " times: " + str(hit_list))
                print(str(len(occupied_fields)-total_hits) + " more hit needed to win this battle.\n")
                print("Enter coordinates for your next target.")
            else:
                print("You have launched " + str(total_missiles) + " missiles, " + str(num_missiles-total_missiles) + " missiles left.")
                print("So far your missiles hit enemy ships " + str(total_hits) + " times: " + str(hit_list))
                print(str(len(occupied_fields)-total_hits) + " more hit needed to win this battle.\n")
                if total_missiles == num_missiles:
                    continue
                else:
                    print("Enter coordinates for your next target.")
        elif total_hits < 20:
            if total_missiles == 1:
                print("You have launched " + str(total_missiles) + " missile, " + str(num_missiles-total_missiles) + " missiles left.")
                print("So far your missiles hit enemy ships " + str(total_hits) + " times: " + str(hit_list))
                print(str(len(occupied_fields)-total_hits) + " more hits needed to win this battle.\n")
                print("Enter coordinates for your next target.")
            elif total_missiles == num_missiles-1:
                print("You have launched " + str(total_missiles) + " missiles, " + str(num_missiles-total_missiles) + " missile left.")
                print("So far your missiles hit enemy ships " + str(total_hits) + " times: " + str(hit_list))
                print(str(len(occupied_fields)-total_hits) + " more hits needed to win this battle.\n")
                print("Enter coordinates for your next target.")
            else:
                print("You have launched " + str(total_missiles) + " missiles, " + str(num_missiles-total_missiles) + " missiles left.")
                print("So far your missiles hit enemy ships " + str(total_hits) + " times: " + str(hit_list))
                print(str(len(occupied_fields)-total_hits) + " more hits needed to win this battle.\n")
                if total_missiles == num_missiles:
                    continue
                else:
                    print("Enter coordinates for your next target.")
        else:
            break

    if total_hits == 20:
        won_count += 1
        print("\n\u001b[32m*****   YOU WIN   *****\u001b[0m\n\nCongratulations! It took " + str(total_missiles) + " missiles to take all enemy ships down. \nWell done " + player + "!")
    else:
        lost_count +=1
        print("\n\u001b[31m*****   YOU LOSE   *****\u001b[0m\n\nSorry, " + player + ". You didn't manage to destroy all enemy ships with the number of missiles at your disposal.")
        print("Here is the solution:")
        print(playing_field.solution(occupied_fields))
        print("You managed to hit " + str(total_hits) + " targets. Here is the complete list: " + str(hit_list))
    play_count += 1
    print(f"\nGames played: {play_count}\nGames won: {won_count}\nGames lost: {lost_count}")
    
    # Define a loop for playing the game again
    
    answer = input("\nWant to play another round? (y/n)\n> ").lower()
    if answer == "y":
        print(f"Ok {player}. Lets begin again.")
        battleship_game(play_count, won_count, lost_count)
    else:
        print(f"It was nice playing with you {player}, see you next time!")  

battleship_game() 
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
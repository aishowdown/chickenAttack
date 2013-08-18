from collections import namedtuple

Order = namedtuple('Order', ['starting_position', 'quantity', 'direction'])

""" Action codes for moving your guys """
STAY = 5
UP = 1
RIGHT = 2
DOWN = 3
LEFT = 4

ALL_ACTIONS = [ STAY, RIGHT, DOWN, LEFT, UP ]

OFFSETS = {
    STAY: (0, 0),
    RIGHT: (1, 0),
    LEFT: (-1, 0),
    UP: (0, 1),
    DOWN: (0, -1)
}

def next_pos(starting_pos, direction):
    if direction not in ALL_ACTIONS:
        return starting_pos
    x_off, y_off = OFFSETS[direction]
    x, y = starting_pos
    return x + x_off, y + y_off

import actions

class Player:

    #Get passed all the board information that never changes throughout the game.
    #It is recommended that you store these in member variables since you will probably need to look at them later.
    # PARAMS:

    #  money_payout_rates:
    #   This is a 50x50 2D array of floats between 0.0 and 1.0 that tell your bot how money per turn this spot produces
    #   Food production is the inverse of money production and follow the formula food_payout_rate = 1.0 - money_payout_rate
    #   This means areas that produce a lot of money, produce less food

    #  my_spawn_point:
    #   An (x, y) tuple of where your new chickens will hatch each turn

    #  their_spawn_point:
    #   An (x, y) tuple of where your opponent's chickens will hatch each turn
    def __init__(self, money_payout_rates, my_spawn_point, their_spawn_point):
        self.money_payout_rates = money_payout_rates,
        self.my_spawn_point = my_spawn_point
        self.their_spawn_point = their_spawn_point


    # Gets called each turn and where you decide where your chickens will go
    # PARAMS:

    #   guys:
    #       A 50x50 2D matrix showing where all the guys are on the board.
    #       An entry of 'None' indicates an unoccupied spot.
    #       A space with chickens will be an object with "num_guys" and "is_mine" properties.
    #

    #   my_food:
    #       A float showing how much food you have left over from last turn.

    #   their_food:
    #       A float showing how much food your opponent has left over from last run.

    #   my_money:
    #       A float showing how much money you will earn at market so far

    #   their_money:
    #       A float showing how much money your opponent will earn at market so far

    # RETURN:
    #   a python dict that takes a tuple ((x_pos, y_pos), direction) as a key and the number of guys to move as the value.
    #   direction is defined in action.py

    def take_turn(self, guys, my_food, their_food, my_money, their_money):
        width = len(guys)
        height = len(guys[0])

        orders ={}
        for x in range(width):
            for y in range(height):
                if not guys[x][y]: continue

                num_guys, is_mine = guys[x][y]
                if not is_mine: continue

                for i in range(num_guys):
                    key = ((x, y), actions.ALL_ACTIONS[i % len(actions.ALL_ACTIONS)])
                    if key not in orders:
                        orders[key] = 1
                    else:
                        orders[key] += 1

        return orders

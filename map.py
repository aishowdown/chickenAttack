import json
import math
import random
import copy

from collections import namedtuple
Population = namedtuple('Population', ['num_guys', 'is_mine'])

import actions

class Gaussian2D:
    """ http://en.wikipedia.org/wiki/Gaussian_function """
    def __init__(self, center, sigma, theta):
        self.cx, self.cy = center
        sx, sy = sigma
        self.a = ((math.cos(theta)**2) / (2 * sx**2) +
                  (math.sin(theta)**2) / (2 * sy**2))
        self.b = ((math.sin(2*theta)) / (4 * sy**2) -
                  (math.sin(2*theta)) / (4 * sx**2))
        self.c = ((math.sin(theta)**2) / (2 * sx**2) +
                  (math.cos(theta)**2) / (2 * sy**2))

    def value(self, point):
        x, y = point
        return math.exp(-1 * ((self.a * (x - self.cx)**2) +
                              (2 * self.b * (x - self.cx) * (y - self.cy)) +
                              (self.c * (y - self.cy)**2)))


class Map:
    """ A class that represents the relevant features of a game board """
    WIDTH = 50
    HEIGHT = 50
    STARTING_FOOD = 10
    STARTING_MONEY = 0

    def __init__(self, num_hills=4, hill_size=30):
        self.width, self.height = Map.WIDTH, Map.HEIGHT
        self.money_payout_rates = self.__generate_payouts(num_hills, hill_size)
        self.p1_guys = [[0] * self.height for x in range(self.width)]
        self.p2_guys = [[0] * self.height for x in range(self.width)]
        self.p1_food = Map.STARTING_FOOD
        self.p2_food = Map.STARTING_FOOD
        self.p1_money = Map.STARTING_MONEY
        self.p2_money = Map.STARTING_MONEY
        self.p1_spawn, self.p2_spawn = self.__generate_spawn_points()

    def board_state_for_json(self):
        p1_guys_json = []
        p2_guys_json = []
        for x in range(self.width):
            for y in range(self.height):
                if self.p1_guys[x][y] > 0:
                    p1_guys_json.append([x, y, self.p1_guys[x][y]])
                elif self.p2_guys[x][y] > 0:
                    p2_guys_json.append([x, y, self.p2_guys[x][y]])
        return {'p1m': self.p1_money, 'p2m': self.p2_money,
                'p1g': p1_guys_json, 'p2g': p2_guys_json}

    def __compute_spawn_amount(self, food):
        if food < 1.0:
            return 0, 0
        base = 1.1
        num_guys = int(math.log(food))
        cost = num_guys**base
        return cost, num_guys

    def spawn_new_guys(self):
        cost, guys_to_spawn = self.__compute_spawn_amount(self.p1_food)
        if guys_to_spawn > 0:
            p1_spawn_x, p1_spawn_y = self.p1_spawn
            current = self.p1_guys[p1_spawn_x][p1_spawn_y]
            self.p1_guys[p1_spawn_x][p1_spawn_y] = int(current) + int(guys_to_spawn)
            self.p1_food -= cost

        cost, guys_to_spawn = self.__compute_spawn_amount(self.p2_food)
        if guys_to_spawn > 0:
            p2_spawn_x, p2_spawn_y = self.p2_spawn
            current = self.p2_guys[p2_spawn_x][p2_spawn_y]
            self.p2_guys[p2_spawn_x][p2_spawn_y] = int(current) + int(guys_to_spawn)
            self.p2_food -= cost

    def give_payouts(self):
        for x in range(self.width):
            for y in range(self.height):
                if self.p1_guys[x][y]:
                    self.p1_money += self.money_payout_rates[x][y]
                    self.p1_food += (1.0 - self.money_payout_rates[x][y])
                elif self.p2_guys[x][y]:
                    self.p2_money += self.money_payout_rates[x][y]
                    self.p2_food += (1.0 - self.money_payout_rates[x][y])

    def apply_moves(self, p1_actions, p2_actions):
        new_p1_guys = [[0] * self.height for x in range(self.width)]
        new_p2_guys = [[0] * self.height for x in range(self.width)]
        for (x, y), direction in p1_actions:
            quantity = int(p1_actions[((x, y), direction)])
            if direction not in actions.ALL_ACTIONS: continue
            if self.p1_guys[x][y] >= quantity:
                new_x, new_y = actions.next_pos((x, y), direction)
                if self.__is_on_board((new_x, new_y)):
                    new_p1_guys[new_x][new_y] += quantity
                    self.p1_guys[x][y] -= quantity
        for (x, y), direction in p2_actions:
            quantity = int(p2_actions[((x, y), direction)])
            if direction not in actions.ALL_ACTIONS: continue
            if self.p2_guys[x][y] >= quantity:
                new_x, new_y = actions.next_pos((x, y), direction)
                if self.__is_on_board((new_x, new_y)):
                    new_p2_guys[new_x][new_y] += quantity
                    self.p2_guys[x][y] -= quantity
        for x in range(self.width):
            for y in range(self.height):
                new_p1_guys[x][y] += self.p1_guys[x][y]
                new_p2_guys[x][y] += self.p2_guys[x][y]
        self.p1_guys = new_p1_guys
        self.p2_guys = new_p2_guys

    def resolve_combat(self):
        for x in range(self.width):
            for y in range(self.height):
                num_dead = min(self.p1_guys[x][y], self.p2_guys[x][y])
                if num_dead < 0:
                    print num_dead
                self.p1_guys[x][y] -= num_dead
                self.p2_guys[x][y] -= num_dead

    def __is_on_board(self, position):
        x, y = position
        if x < 0 or x >= self.width: return False
        if y < 0 or y >= self.height: return False
        return True

    def constructor_data_for_p1(self):
        return (self.money_payout_rates, self.p1_spawn, self.p2_spawn)

    def constructor_data_for_p2(self):
        return (self.money_payout_rates, self.p2_spawn, self.p1_spawn)

    def turn_data_for_p1(self):
        guys = [[None] * self.height for x in range(self.width)]
        for x in range(self.width):
            for y in range(self.height):
                if self.p1_guys[x][y]:
                    guys[x][y] = Population(self.p1_guys[x][y], True)
                elif self.p2_guys[x][y]:
                    guys[x][y] = Population(self.p2_guys[x][y], False)
        return (guys, self.p1_food, self.p2_food, self.p1_money, self.p2_money)

    def turn_data_for_p2(self):
        guys = [[None] * self.height for x in range(self.width)]
        for x in range(self.width):
            for y in range(self.height):
                if self.p1_guys[x][y]:
                    guys[x][y] = Population(self.p1_guys[x][y], False)
                elif self.p2_guys[x][y]:
                    guys[x][y] = Population(self.p2_guys[x][y], True)
        return (guys, self.p2_food, self.p1_food, self.p2_money, self.p1_money)

    def __mirror(self, x, y):
        """ Mirror a point over the diagonal of the map """
        return (self.width - x - 1, self.height - y - 1)

    def __generate_payouts(self, num_hills, hill_size):
        """ Compute several gaussians and build the payout map """
        hills = []
        for i in range(num_hills):
            cx = random.randint(0, self.width - 1)
            cy = random.randint(0, self.height - 1)
            sx = random.random() * hill_size + 1
            sy = random.random() * hill_size + 1
            theta = random.random() * math.pi
            hills.append(Gaussian2D((cx, cy), (sx, sy), theta))
            # Add a mirror image one too to make the map fair
            hills.append(Gaussian2D(self.__mirror(cx, cy), (sx, sy), theta + math.pi))

        # Sum all the hills
        money_payout_rates = [[0.0] * self.height for x in range(self.width)]
        for y in range(self.height):
            for x in range(self.width):
                money_payout_rates[x][y] = sum([h.value((x,y)) for h in hills])

        # Normalize the rates from 0->1
        max_payout = max([max(row) for row in money_payout_rates])
        min_payout = min([min(row) for row in money_payout_rates])
        for y in range(self.height):
            for x in range(self.width):
                offset = money_payout_rates[x][y] - min_payout
                money_payout_rates[x][y] = offset / (max_payout - min_payout)
                money_payout_rates[x][y] = int(1000 * money_payout_rates[x][y]) / 1000.0

        return money_payout_rates

    def __generate_spawn_points(self):
        """ Keep trying random points until it's mirror is far enough away """
        while True:
            p1x = random.randint(0, self.width - 1)
            p1y = random.randint(0, self.height - 1)
            p2x, p2y = self.__mirror(p1x, p1y)
            d_sq = (p1x - p2x)**2 + (p1y - p2y)**2
            if d_sq >= (self.width / 2)**2:
                break
        return (p1x, p1y), (p2x, p2y)

    def to_struct(self):
        return {'p1_spawn': self.p1_spawn,
                'p2_spawn': self.p2_spawn,
                'money_payout_rates': self.money_payout_rates}

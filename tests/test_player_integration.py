import pytest
from game import game_loop
import actions
from map import *
from movementplayer import Player

# Helper function to generate object needed to run mock game
def generate_json_data(game_map):
    return {'p1_spawn': game_map.p1_spawn, 'p2_spawn': game_map.p2_spawn,
        'money_payout_rates': game_map.money_payout_rates, 'turns': [game_map.board_state_for_json()]}

# This test verifies that the player constructor creates spawn points appropriately
def test_player_constructor():
    m = Map()

    p1 = Player(*m.constructor_data_for_p1(), direction = actions.STAY)
    p2 = Player(*m.constructor_data_for_p2(), direction = actions.STAY)

    assert p1.their_spawn_point == p2.my_spawn_point
    assert p2.their_spawn_point == p1.my_spawn_point

# This test verifies basic player movement by moving minions to the edge of the map
def test_player_opposite_directions():
    m = Map()
    m.p1_spawn, m.p2_spawn = (1, 1), (48, 48)

    p1 = Player(*m.constructor_data_for_p1(), direction = actions.LEFT)
    p2 = Player(*m.constructor_data_for_p2(), direction = actions.RIGHT)

    json_data = generate_json_data(m)

    game_loop(m, p1,p2,json_data,10)
    assert m.p1_guys[0][1] > 0
    assert m.p2_guys[49][48] > 0

# This test verifies basic player movement by checking that minions have only gone 10 spaces max
def test_player_limited_moves():
    m = Map()
    m.p1_spawn, m.p2_spawn = (20, 1), (48, 48)

    p1 = Player(*m.constructor_data_for_p1(), direction = actions.LEFT)
    p2 = Player(*m.constructor_data_for_p2(), direction = actions.STAY)

    json_data = generate_json_data(m)

    NUM_MOVES = 10
    game_loop(m, p1,p2,json_data,NUM_MOVES)
    assert m.p1_guys[9][1] == 0
    assert m.p1_guys[11][1] > 0
import pytest
from map import *

# Verify that the center of the gaussian function is 1 and far out is 0 as expected
# for a normal distribution
def test_gaussian_basic():
    gauss = Gaussian2D((0,0), (1, 1) ,0)
    assert gauss.value((0,0)) == 1.0
    assert gauss.value((1000,1000)) == 0

#Verify that guys are spawned after the spawn function is called
def test_map_spawn():
    game_map = Map()
    game_map.spawn_new_guys()
    board_state = game_map.board_state_for_json()
    p1_number_of_guys = board_state["p1g"][0][2]
    p2_number_of_guys = board_state["p2g"][0][2]
    assert game_map.p1_guys[game_map.p1_spawn[0]][game_map.p1_spawn[1]] == 2
    assert game_map.p2_guys[game_map.p2_spawn[0]][game_map.p2_spawn[1]] == 2

#Verify no guys are spawned when player has no food
def test_map_exhaust_food():
    game_map = Map()
    game_map.p1_food = 0
    game_map.spawn_new_guys()
    board_state = game_map.board_state_for_json()
    p1_guys = board_state["p1g"]
    assert p1_guys == []

# Verify money exists for both players after payout function is called
def test_map_payout():
    game_map = Map()
    game_map.spawn_new_guys()
    game_map.give_payouts()
    board_state = game_map.board_state_for_json()
    p1_money = board_state['p1m']
    p2_money = board_state['p2m']
    assert p1_money > 0
    assert p2_money > 0

# Test that the to_struct function returns expected values
def test_struct_creation():
    game_map = Map()
    game_map.p1_spawn = (5, 6)
    game_map.p2_spawn = (7, 8)
    game_map.money_payout_rates = .5

    assert game_map.to_struct() == {'p1_spawn': (5,6), 'p2_spawn': (7,8), 'money_payout_rates': .5}

import sys
import json
import re
import httplib, urllib
from functools import partial

from networkplayer import NetworkPlayer

from map import Map
import actions

NUM_TURNS = 1000
STARTING_MONEY = 100


if len(sys.argv) != 3:
    print "Usage: %s player1_module player2_module" % sys.argv[0]
    sys.exit(1)


if sys.argv[1].endswith(".py"):
    exec('from %s import Player as Player1' % sys.argv[1][:-3])
else:
    Player1 = partial(NetworkPlayer, sys.argv[1])


if sys.argv[2].endswith(".py"):
    exec('from %s import Player as Player2' % sys.argv[2][:-3])
else:
    Player2 = partial(NetworkPlayer, sys.argv[2])


m = Map()
p1 = Player1(*m.constructor_data_for_p1())
p2 = Player2(*m.constructor_data_for_p2())


json_data = {'p1_spawn': m.p1_spawn, 'p2_spawn': m.p2_spawn,
     'money_payout_rates': m.money_payout_rates, 'turns': [m.board_state_for_json()]}

for i in range(NUM_TURNS):
    print 'Turn #%d' % i

    # Get the players' actions
    p1_actions = p1.take_turn(*m.turn_data_for_p1())
    p2_actions = p2.take_turn(*m.turn_data_for_p2())

    m.apply_moves(p1_actions, p2_actions)
    m.resolve_combat()

    m.give_payouts()
    m.spawn_new_guys()

    m.resolve_combat() #in case the new guys spawned into combat

    json_data['turns'].append(m.board_state_for_json())


print '---- FINAL SCORE ----'
print '%s:\t%f' % (sys.argv[1], m.p1_money)
print '%s:\t%f' % (sys.argv[2], m.p2_money)
print

winner = sys.argv[1]
if m.p1_money > m.p2_money:
    print 'WINNER: %s' % sys.argv[1]
elif m.p1_money < m.p2_money:
    print 'WINNER: %s' % sys.argv[2]
else:
    print 'TIED!'

# Save the game log to disk for visualization later
json_str = json.dumps(json_data)
with open('game_log.js', 'w') as f:
    f.write("window.game = %s" % json_str)



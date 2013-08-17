import json

import httplib, urllib

class NetworkPlayer():
    headers = {"Content-type": "application/x-www-form-urlencoded",
           "Accept": "text/plain"}

    def __init__(self, port, money_payout_rates, my_spawn_point, their_spawn_point):
        print "initing with %s" % port
        self.port = port
        conn = httplib.HTTPConnection("127.0.0.1:%s" % self.port)

        jsonmap = json.dumps({
            "money_payout_rates": money_payout_rates,
            "my_spawn_point": my_spawn_point,
            "their_spawn_point": their_spawn_point
            });
        conn.request("POST", "/map", urllib.urlencode({'data': jsonmap}), self.headers)



    def take_turn(self, guys, my_food, their_food, my_money, their_money):
        conn = httplib.HTTPConnection("127.0.0.1:%s" % self.port)

        jsonmap = json.dumps({
            "guys": guys,
            "my_food": my_food,
            "their_food": their_food,
            "my_money": my_money,
            "their_money": their_money
        });
        conn.request("POST", "/", urllib.urlencode({'data': jsonmap}), self.headers)
        resp = conn.getresponse()
        jsonOrders = json.load(resp)
        orders = {}
        #This can be cleaned up

        for order in jsonOrders:
            orders[(order[0], order[1]), order[2]] = order[3]

        return orders;

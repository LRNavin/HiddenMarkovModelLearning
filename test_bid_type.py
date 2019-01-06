import json, collections
import os
from pprint import pprint

class test_bid_type:

    def get_utility_for_bid(self, issues, utilities, bid):
        bid_value = 0
        vals = bid.split(",")
        # keys = ["Fruit", "Juice", "Topping1", "Topping2"]
        keys = utilities.keys()
        for i, v in enumerate(vals):
            key = keys[i]
            weight = utilities[key]["weight"]
            bid_value += weight * utilities[key][v]
        return bid_value


    def get_bid_type(self, prev, curr):
        if (curr[0] == prev[0] and curr[1] == prev[1]):
            return ("silent")
        elif (curr[0] >= prev[0] and curr[1] <= prev[1]):
            return "selfish"
        elif (curr[0] > prev[0] and curr[1] > prev[1]):
            return "fortunate"
        elif (curr[0] == prev[0] and curr[1] > prev[1]):
            return "nice"
        elif (curr[0] < prev[0] and curr[1] > prev[1]):
            return "concession"
        elif (curr[0] < prev[0] and curr[1] <= prev[1]):
            return "unfortunate"
        else:
            return "unknwon"


    def get_bid_types(self, bids, utilities, issues):
        bid_types = [""] * len(bids)
        prev1 = [0] * 2
        curr1 = [0] * 2
        prev1[0] = self.get_utility_for_bid(issues, utilities[0], bids[0]["agent1"])
        prev1[1] = self.get_utility_for_bid(issues, utilities[1], bids[0]["agent1"])
        prev2 = [0] * 2
        curr2 = [0] * 2
        prev2[0] = self.get_utility_for_bid(issues, utilities[1], bids[0]["agent2"])
        prev2[1] = self.get_utility_for_bid(issues, utilities[0], bids[0]["agent2"])
        bids.pop(0)
        bids.pop(len(bids) - 1)
        for i, b in enumerate(bids):
            curr1[0] = self.get_utility_for_bid(issues, utilities[0], b["agent1"])
            curr1[1] = self.get_utility_for_bid(issues, utilities[1], b["agent1"])
            curr2[0] = self.get_utility_for_bid(issues, utilities[1], b["agent2"])
            curr2[1] = self.get_utility_for_bid(issues, utilities[0], b["agent2"])
            bid_type1 = self.get_bid_type(prev1, curr1)
            bid_type2 = self.get_bid_type(prev2, curr2)
            prev1 = curr1[:]
            prev2 = curr2[:]
            obj = {
                "round": i,
                "agent1": bid_type1,
                "agent2": bid_type2
            }
            bid_types[i] = obj
        return bid_types

    def create_bid_types_test_data(self, sourceFile, destination):

        # script_dir = os.path.dirname(__file__)
        with open(sourceFile, 'r') as f:
            data = json.JSONDecoder(object_pairs_hook=collections.OrderedDict).decode(f.read())
            issues = data["issues"]
            utilities = [0] * 2
            utilities[0] = data["Utility1"]
            utilities[1] = data["Utility2"]
            bids = data["bids"]
            bid_types = self.get_bid_types(bids, utilities, issues)
            with open(os.getcwd() + destination, 'w') as outfile:
                json.dump(bid_types, outfile, indent=2)


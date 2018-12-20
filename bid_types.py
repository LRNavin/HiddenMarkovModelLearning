import json
from pprint import pprint


def get_utility_for_bid(isues, utilities, bid):
	bid_value = 0
	vals = bid.split(",")
	keys = ["Fruit", "Juice", "Topping1", "Topping2"]
	for i,v in enumerate(vals):
		key = keys[i];
		weight = utilities[key]["weight"]
		bid_value += weight * utilities[key][v]
	return bid_value

def get_bid_type(prev, curr):
	if(curr[0] > prev[0] and curr[1] < prev[1]):
		return "selfish"
	elif(curr[0] > prev[0] and curr[1] > prev[1]):
		return "fortunate"
	elif(curr[0] == prev[0] and curr[1] > prev[1]):
		return "nice"
	elif(curr[0] < prev[0] and curr[1] > prev[1]):
		return "concession"
	elif(curr[0] < prev[0] and curr[1] < prev[1]):
		return "unfortunate"
	else:
		return "silent"

def get_bid_types(bids, utilities, issues):
	prev = [0]*2
	curr = [0]*2
	prev[0] = get_utility_for_bid(issues, utilities[0], bids[0]["agent1"])
	prev[1] = get_utility_for_bid(issues, utilities[1], bids[0]["agent1"])
	bids.pop(0)
	bids.pop(len(bids)-1)
	bid_types = [""]*len(bids)
	for i,b in enumerate(bids):
		curr[0] = get_utility_for_bid(issues, utilities[0], b["agent1"]) 
		curr[1] = get_utility_for_bid(issues, utilities[1], b["agent1"]) 
		bid_types[i] = get_bid_type(prev, curr)
		prev = curr[:]
	return bid_types
		

log_path = "./training_logs/"
with open(log_path+'conceder_conceder.json') as f:
    data = json.load(f)

issues = data["issues"]
utilities = [0]*2
utilities[0] = data["Utility1"]
utilities[1] = data["Utility2"]
bids = data["bids"]
bid_types = get_bid_types(bids, utilities, issues);
print(bid_types)
# bid_util = get_utility_for_bid(issues, utilities[0], bids[0]["agent1"])


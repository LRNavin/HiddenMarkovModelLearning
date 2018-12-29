import os
import json
import numpy as np
from hmm import hmm

# maps each stratey to a number so we can use int indexes instead of strings
s = {"random": 0, "tft": 1, "hardheaded": 2, "conceder": 3}
m = {"concession": 0, "unfortunate": 1,"nice": 2,"selfish": 3,"fortunate": 4,"silent": 5}
strats = ["Random","Tit For Tat","Hard Headed","Conceder"]

def init_emission():
	with open(os.getcwd() + "/hmm_model/sensoryModel.json") as f:
		emissions = json.load(f)
		emission_probabilities = np.zeros((len(emissions), len(emissions[list(emissions.keys())[0]])))
		for strategy in emissions:
			for move in emissions[strategy]:
				emission_probabilities[s[strategy]][m[move]] = emissions[strategy][move]
		return emission_probabilities

def evidence_to_index(evidence):
	new_evidence = []
	for i, e in enumerate(evidence):
		e = {
			"round": i,
			"agent1": m[e["agent1"]],
			"agent2": m[e["agent2"]] 
		}
		new_evidence.append(e)
	return new_evidence



# np.eye() creates diagonal matrix of ones, this represents prob 1 of transitioning to same strategy
# and prob 0 of transitioning from one strat to another.
emission_probabilities = init_emission()
transition_probabilities = np.eye(len(s), dtype=int)
priors = [float(1)/len(s)]*len(s) # all startegies are equaly probable
with open(os.getcwd() + "/test_types/test3.json") as f:
	e = json.load(f)
	evidence = evidence_to_index(e)
	hmm = hmm(transition_probabilities, emission_probabilities, priors, evidence)
	hmm.set_agent("agent2")
	strategies_prob = hmm.filter()
	for i,strat in enumerate(strategies_prob):
		print(strats[i] + ": " + str(round(strat, 2)) + ",\n")





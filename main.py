import os
import json
import numpy as np

# maps each stratey to a number so we can use int indexes instead of strings
s = {"random": 0, "tft": 1, "hardheaded": 2, "conceder": 3}
m = {"concession": 0, "unfortunate": 1,"nice": 2,"selfish": 3,"fortunate": 4,"silent": 5}

def init_matrices():
	with open(os.getcwd() + "/hmm_model/sensoryModel.json") as f:
		emissions = json.load(f)
		emission_probabilities = np.zeros((len(emissions), len(emissions[list(emissions.keys())[0]])))
		for strategy in emissions:
			for move in emissions[strategy]:
				emission_probabilities[s[strategy]][m[move]] = emissions[strategy][move]
		return emission_probabilities

emission_probabilities = init_matrices()
print(emission_probabilities)
# import numpy as np

class hmm:

	def __init__(self, transition_probabilities, emission_probabilities, prior_probabilities):
		self.transitions = transition_probabilities
		self.emissions = emission_probabilities
		self.priors = prior_probabilities

	


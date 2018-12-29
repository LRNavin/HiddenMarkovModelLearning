import numpy as np

class hmm:

	def __init__(self, transition_probabilities, emission_probabilities, prior_probabilities):
		self.transitions = transition_probabilities
		self.emissions = emission_probabilities
		self.priors = prior_probabilities
		self.agent = ''
		# print(self.emissions)

	def filter(self, evidence):
		p_st = self.priors[:]
		p_st1 = 0
		for _e in evidence:
			e = _e[self.agent]
			one_step_pred = self.one_step_prediction(self.transitions, p_st)
			


	def one_step_prediction(self, transitions, p_st):
		# sum over all possible next states (st+1)
		# p(st+1|st)*p(st)
		prob = np.zeros(len(transitions))
		for i,t in enumerate(transitions):
			prob = np.add(prob, np.multiply(t, p_st[i]))
		return prob

	# def get_evidence_prob(self, evidence):


	def set_agent(self, agent):
		self.agent = agent
			



		




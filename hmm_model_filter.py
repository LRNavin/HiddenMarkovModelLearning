import numpy as np


class hmm_model_filter:
    def __init__(self, transition_probabilities, emission_probabilities, prior_probabilities, evidence):
        self.transitions = transition_probabilities
        self.emissions = emission_probabilities
        self.priors = prior_probabilities
        self.agent = ''
        self.evidence = evidence

    def filter(self):
        p_st = self.priors[:]
        p_st1 = 0
        for _e in self.evidence:
            e = _e[self.agent]
            one_step_pred = self.one_step_prediction(self.transitions, p_st)
            emission_prob = self.get_evidence_prob(e)
            temp = one_step_pred * emission_prob
            p_st = temp / temp.sum(axis=0, keepdims=1)
        return p_st

    def one_step_prediction(self, transitions, p_st):
        # sum over all possible next states (st+1)
        # p(st+1|st)*p(st)
        prob = np.zeros(len(transitions))
        for i, t in enumerate(transitions):
            prob = np.add(prob, np.multiply(t, p_st[i]))
        return prob

    def get_evidence_prob(self, e):
        emission_prob = []
        for emission in self.emissions:
            emission_prob.append(emission[e])
        return emission_prob

    def set_agent(self, agent):
        self.agent = agent









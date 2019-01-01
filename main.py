import os
import json
import numpy as np
from hmm_model_filter import hmm_model_filter
from test_bid_type import test_bid_type

# maps each stratey to a number so we can use int indexes instead of strings
s = {"random": 0, "tft": 1, "hardheaded": 2, "conceder": 3}
m = {"concession": 0, "unfortunate": 1,"nice": 2,"selfish": 3,"fortunate": 4,"silent": 5}
strats = ["Random","Tit For Tat","Hard Headed","Conceder"]

class main:

    def init_emission(self):
        with open(os.getcwd() + "/hmm_model/sensoryModel.json") as f:
            emissions = json.load(f)
            emission_probabilities = np.zeros((len(emissions), len(emissions[list(emissions.keys())[0]])))
            for strategy in emissions:
                for move in emissions[strategy]:
                    emission_probabilities[s[strategy]][m[move]] = emissions[strategy][move]
            return emission_probabilities

    def evidence_to_index(self, evidence):
        new_evidence = []
        for i, e in enumerate(evidence):
            if type(e) is dict and type(m) is dict:
                e = {
                    "round": i,
                    "agent1": m[e["agent1"]],
                    "agent2": m[e["agent2"]]
                }
                new_evidence.append(e)
        return new_evidence


    def run_hmm_prediction(self, test_source_file):

        #Convert Test Logs to Logs Bid Types
        # global test_bid_types
        bid_type_gen = test_bid_type()
        bid_type_gen.create_bid_types_test_data(test_source_file, "/test_logs/test_bid_types.json")

        # np.eye() creates diagonal matrix of ones, this represents prob 1 of transitioning to same strategy
        # and prob 0 of transitioning from one strat to another.
        emission_probabilities = self.init_emission()
        transition_probabilities = np.eye(len(s), dtype=int)
        priors = [float(1)/len(s)]*len(s) # all startegies are equaly probable

        script_dir = os.path.dirname(__file__)

        with open(script_dir + "/test_logs/test_bid_types.json") as f:
            e = json.load(f)
            evidence = self.evidence_to_index(e)
            hmm = hmm_model_filter(transition_probabilities, emission_probabilities, priors, evidence)
            hmm.set_agent("agent1")
            strategies_prob = hmm.filter()
            print('AGENT 1 - Prediction')
            print("\n")
            for i,strat in enumerate(strategies_prob):
                print(strats[i] + ": " + str(round(strat, 2)) )
            print("\n")

            hmm.set_agent("agent2")
            strategies_prob = hmm.filter()
            print('AGENT 2 - Prediction')
            print("\n")
            for i,strat in enumerate(strategies_prob):
                print(strats[i] + ": " + str(round(strat, 2)) )



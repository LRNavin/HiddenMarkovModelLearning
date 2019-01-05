from __future__ import division
import json
import os

# Agent-wise Frequency calculator
probabilityDecimal = 2
sensory_model_file = 'sensoryModel.json'
log_path = "./train_types/"

agentBidFrequency = {}
totalBidCount = {}
sensoryModel = {}

print(len(os.listdir(os.getcwd() + "/train_types")))

for filename in os.listdir(os.getcwd() + "/train_types"):
    with open(log_path + filename) as f:
        data = json.load(f)

        agentNames = ''.join([i for i in filename.split('.')[0] if not i.isdigit()])
        agent1 = agentNames.split('_')[0]
        agent2 = agentNames.split('_')[1]

        for bidRound in data:
            if type(bidRound) is dict:
                agent1_bid_type = bidRound['agent1']
                agent2_bid_type = bidRound['agent2']

                counterKey_agent1 = agent1 + '_' + agent1_bid_type
                counterKey_agent2 = agent2 + '_' + agent2_bid_type

                # Bid Type Frequency Update - agent 1
                if counterKey_agent1 in agentBidFrequency:
                    agentBidFrequency[counterKey_agent1] = agentBidFrequency[counterKey_agent1] + 1
                else:
                    agentBidFrequency[counterKey_agent1] = 1

                # Total Bid Count - agent 1
                if agent1 in totalBidCount:
                    totalBidCount[agent1] = totalBidCount[agent1] + 1
                else:
                    totalBidCount[agent1] = 1

                # Bid Type Frequency Update - agent 2
                if counterKey_agent2 in agentBidFrequency:
                    agentBidFrequency[counterKey_agent2] = agentBidFrequency[counterKey_agent2] + 1
                else:
                    agentBidFrequency[counterKey_agent2] = 1

                # Total Bid Count - agent 2
                if agent2 in totalBidCount:
                    totalBidCount[agent2] = totalBidCount[agent2] + 1
                else:
                    totalBidCount[agent2] = 1

for frequencyCounter in agentBidFrequency.keys():

    agent_name = frequencyCounter.split('_')[0]
    bid_type = frequencyCounter.split('_')[1]
    bid_frequency = agentBidFrequency[frequencyCounter]
    total_agent_bid = totalBidCount[agent_name]

    bid_type_prob = bid_frequency / total_agent_bid
    bid_type_prob = round(bid_type_prob, probabilityDecimal)

    if agent_name not in sensoryModel:
        sensoryModel[agent_name] = {
                                    "selfish": 0.00,
                                    "silent": 0.00,
                                    "fortunate": 0.00,
                                    "unfortunate": 0.00,
                                    "concession": 0.00,
                                    "nice": 0.00
                                  }
    sensoryModel[agent_name][bid_type] = bid_type_prob

print(sensoryModel)

with open(os.getcwd() + '/hmm_model/' + sensory_model_file, 'w') as outfile:
    json.dump(sensoryModel, outfile, indent=2)
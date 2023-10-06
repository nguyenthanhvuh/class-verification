import random
groups = set(["MSK",
              "AI Cubed",
              "Peach Wave",
              "NeuralNet Navigators",
              "NeuroCop",
              "Secure AI Trio",
              "SafetyNetSquad",
              "VerifAI",
              "Neural Nexus",
              "DMSR",
              "NeuralNet Navigators"])


exclude = set(["AI Cubed", " SafetyNetSquad", "Secure AI Trio", 
               "Neural Nexus", "MSK", "NeuroCop", "VerifAI","Peach Wave", "NeuralNet Navigators"])


nselects = 2 
print(random.sample(list(groups-exclude), nselects))

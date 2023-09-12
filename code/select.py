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
            "DMSR"])


exclude = set(["AI Cubed", " SafetyNetSquad", "Secure AI Trio", "Neural Nexus"])


nselects = 2 
print(random.sample(list(groups-exclude), nselects))
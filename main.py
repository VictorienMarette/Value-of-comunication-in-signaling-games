from ClearPunishSignalingGame import ClearPunishSignalingGame

G = ClearPunishSignalingGame.generate_random(2, 2, 2)
print(G)

import numpy as np

n = 5  # nombre d'états
x = np.random.rand(n)      # nombres aléatoires positifs
print(10*x)
prob = x / x.sum()         # normalisation pour que la somme soit 1
print(prob)
print(prob.sum())  # vérifie que ça fait 1

from ClearPunishSignalingGame import ClearPunishSignalingGame


T = ["W", "S"]
S = ["B", "Q"]
A = ["F", "C"]


def Us(t, s, a):
    tot = 0
    if a == "C":
        tot += 2
    if (t == "W" and s == "Q") or (t == "S" and s == "B"):
        tot += 1
    return tot


def Ur(t, s, a):
    if (t == "W" and a == "F") or (t == "S" and a == "C"):
        return 1
    return 0


def P(s):
    return "F"


for i in range(1, 8):
    p = [i/8, 1-i/8]
    print("Probs: " + str(p))
    G = ClearPunishSignalingGame(p, T, S, A, Us, Ur, P=P)
    G.print_ce_outcome()
    print("")

"""
while True:
    G = ClearPunishSignalingGame.generate_random(2, 2, 2)
    V = G.get_ce_vertexes()
    for v in V:
        arette opti
        regarder si payoff BN 
        regarder dim ss espace
"""
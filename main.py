"""from ClearPunishSignalingGame import ClearPunishSignalingGame

while True:
    G = ClearPunishSignalingGame.generate_random(2, 2, 2)
    V = G.get_ce_vertexes()
    BN = False
    bestBn = -15
    bestCE = 0
    for v in V:
        v0 = v[0][0].flatten()
        if G.is_bn(v0):
            Bn = True
            if G.E_us(v0) > bestBn:
                bestBn = G.E_us(v0)
        else:
            if G.E_us(v0) > bestCE:
                bestCE = G.E_us(v0)
    if not BN:
        print("BN pas vertex")
        print(G)
    elif bestBn < bestCE - 1e-12:
        print("BN not best")
        print(G)
"""

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
for i in range(1, 8):
    p = [i/8, 1-i/8]
    print("Probs: " + str(p))
    G = ClearPunishSignalingGame(p, T, S, A, Us, Ur, P=P)
    vertexs = G.get_ce_vertexes()
    for v in vertexs:
        if G.is_bn(v[0].flatten()):
            print(v)

p = [3/4, 1/4]
print("Probs: " + str(p))
G = ClearPunishSignalingGame(p, T, S, A, Us, Ur, P=P)
#vertexs = G.get_ce_vertexes()

print(G.is_bn([1/6, 1/6, 2/3, 0, 1/2, 1/2, 0, 0]))"""
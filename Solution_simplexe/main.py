from signaling_game import SignalingGame
import numpy as np

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

"""for i in range(1, 8):
    p = [i/8, 1-i/8]
    print("Probs: " + str(p))
    G = SignalingGame(p, T, S, A, Us, Ur, P=P)
    G.print_clear_punish_vertexes()"""

pw = 3/4
p = [pw, 1-pw]
G = SignalingGame(p, T, S, A, Us, Ur, P=P)
inq, eq = G.get_clear_punish_conditions(get_parameters=True)

x = np.array([(1/pw-1)/2,(1/pw-1)/2,2-1/pw,0,1/2,1/2,0,0])
for i in inq:
    if np.dot(i[0],x) <= i[1] + 0.001 and np.dot(i[0],x) >= i[1] - 0.001:
        print(i)
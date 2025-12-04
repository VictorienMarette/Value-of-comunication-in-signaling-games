from signaling_game import SignalingGame


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
    G = SignalingGame(p, T, S, A, Us, Ur, P=P)
    G.print_clear_punish_vertexes()

from signaling_game import SignalingGame

p = [1/2, 1/2]

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


G = SignalingGame(p, T, S, A, Us, Ur, P=P)

print(G.get_clear_punish_conditions())
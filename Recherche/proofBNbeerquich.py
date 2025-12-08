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


pw = 3 / 4
p = [pw, 1-pw]
G = SignalingGame(p, T, S, A, Us, Ur, P=P)
inq, eq = G.get_clear_punish_conditions(get_parameters=True)

x = np.array([(1/pw-1)/2, (1/pw-1)/2, 2-1/pw, 0, 1/2, 1/2, 0, 0])
ineq_admissible = []
for i in inq:
    if np.dot(i[0], x) <= i[1] + 0.001 and np.dot(i[0], x) >= i[1] - 0.001:
        if np.linalg.norm(i[0]) > 1e-8:
            print(i)
            # test
            ineq_vec = i[0]
            a4 = ineq_vec[3]
            a8 = ineq_vec[7]
            newv = np.delete(ineq_vec, [3, 7], axis=0)
            for ind in range(3):
                newv[ind] += -a4
                newv[ind+3] += -a8
            coef = i[1] - a4 - a8
            print((newv, float(coef)))
            print("")
            ineq_admissible.append((newv, float(coef)))
            
print("")

# ptdr on text dans le cas ou x4 et x8 = 0

M = np.column_stack([i[0] for i in ineq_admissible])
print(sp.Matrix(M).nullspace())
print(len(sp.Matrix(M).nullspace()))
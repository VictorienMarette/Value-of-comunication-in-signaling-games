from signaling_game import SignalingGame
import numpy as np
from itertools import combinations

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

"""pw = 3 /4
p = [pw, 1-pw]
G = SignalingGame(p, T, S, A, Us, Ur, P=P)
inq, eq = G.get_clear_punish_conditions(get_parameters=True)

x = np.array([(1/pw-1)/2, (1/pw-1)/2, 2-1/pw, 0, 1/2, 1/2, 0, 0])
ineq_admissible = []
for i in inq:
    if np.dot(i[0], x) <= i[1] + 0.001 and np.dot(i[0],x) >= i[1] - 0.001:
        if np.linalg.norm(i[0]) > 1e-8:
            ineq_admissible.append(i)
            print(i)
print("")


def any_null_vector(A, tol=1e-12):

    A = np.asarray(A, dtype=float)
    if A.size == 0:
        return None

    # SVD
    U, S, Vh = np.linalg.svd(A)
    rank = np.sum(S > tol)
    n = A.shape[1]
    null_dim = n - rank

    if null_dim == 0:
        return None  # noyau trivial

    # colonnes de V = Vh.T correspondant aux directions du noyau
    null_space = Vh.T[:, rank:]   # shape (n, null_dim)
    vec = null_space[:, 0]        # on prend une direction quelconque du noyau

    # normaliser (pratique) — évite division par zéro car vec non nul ici
    vec = vec / np.linalg.norm(vec)
    return vec


for m in list(combinations(range(len(ineq_admissible)), 8)):
    M = np.column_stack([ineq_admissible[i][0] for i in m])
    v = any_null_vector(M)
    if v is not None:
        if np.all(v <= 0) or np.all(v >= 0):
            v = np.round(v, 4)
            for i in range(len(ineq_admissible)):
                if i in m:
                    print(ineq_admissible[i])
            print(v)
            print("")"""
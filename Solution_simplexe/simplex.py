import itertools
import numpy as np


def Vertexes(ineq, lenght, epsi):
    candidates = list(itertools.combinations(range(len(ineq)), lenght))
    print(candidates)

    solutions = []

    for c in candidates:
        A = np.vstack([ineq[i][0] for i in c])
        b = np.vstack([ineq[i][1] for i in c])
        print(A)
        try:
            A_inv = np.linalg.inv(A)
            x = A_inv@b
            if in_simplex(x, ineq, epsi):
                solutions.append((A_inv@b, c))  
        except np.linalg.LinAlgError:
            pass

    return solutions


def in_simplex(x, ineq, epsi):
    print(x)
    for i in ineq:
        print(np.dot(np.array(i[0]), x))
        if np.dot(np.array(i[0]), x) > i[1] + epsi:
            return False

    return True

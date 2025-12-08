import itertools
import numpy as np


def vertexes(ineq, eq, space_dim, epsi, plan_index=False):
    dim = space_dim - len(eq)
    candidates = list(itertools.combinations(range(len(ineq)), dim))
    solutions = []
    for c in candidates:
        A = np.vstack([ineq[i][0] for i in c]+[eq[i][0] for i in range(len(eq))])
        b = np.vstack([ineq[i][1] for i in c]+[eq[i][1] for i in range(len(eq))])
        if is_invertible(A):
            A_inv = np.linalg.inv(A)
            x = A_inv@b
            if in_ineq_simplex(x, ineq, epsi):
                if plan_index:
                    solutions.append((x, c))
                else:
                    solutions.append(x)
    return solutions


def sumed_vertexes(ineq, eq, space_dim, epsi, plan_index=False):
    old_vertexes = vertexes(ineq, eq, space_dim, epsi, plan_index=plan_index)
    new = []
    if plan_index:
        pass  # pas fini
    else:
        while old_vertexes:
            v = old_vertexes.pop(0)
            remove_list = []
            for i, v2 in enumerate(old_vertexes):
                if np.linalg.norm(v - v2) <= 0.0001:
                    remove_list.append(i)
            new.append((v, len(remove_list)+1))
            for i in sorted(remove_list, reverse=True):
                del old_vertexes[i]
    return new


def in_ineq_simplex(x, ineq, epsi):
    for i in ineq:
        if np.dot(np.array(i[0]), x) > i[1] + epsi:
            return False
    return True


def in_simplex(x, ineq, eq, epsi):
    if not in_ineq_simplex(x, ineq, epsi):
        return False
    for e in eq:
        if np.dot(np.array(e[0]), x) > e[1] + epsi or np.dot(np.array(e[0]), x) < e[1] - epsi:
            return False
    return True


def is_invertible(A, tol=1e-12):
    s = np.linalg.svd(A, compute_uv=False)
    return np.min(s) > tol

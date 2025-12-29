import numpy as np
import cdd


# Convention ineq: Ax<=b, c'est des np array
def vertexes(ineq, eq):
    lin_set = set(list(range(len(eq))))
    eq2 = [[b, *(-a for a in A)] for A, b in eq]
    ineq2 = [[b, *(-a for a in A)] for A, b in ineq]
    mat = cdd.matrix_from_array(eq2+ineq2, rep_type=cdd.RepType.INEQUALITY, lin_set=lin_set)
    poly = cdd.polyhedron_from_matrix(mat)
    ext = cdd.copy_generators(poly)
    return [v[1:] for v in ext.array]


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

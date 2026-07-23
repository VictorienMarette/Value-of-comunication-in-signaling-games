import numpy as np
from polyhedrons import h_rep_to_v_rep


class CheapTalkGame():
    def __init__(self, T, A, Us, Ur):
        self.T = T
        self.A = A
        self.Us = Us
        self.Ur = Ur

    def index_Us(self, it, ia):
        t = self.T[it]
        a = self.A[ia]
        return self.Us(t, a)

    def index_Ur(self, it, ia):
        t = self.T[it]
        a = self.A[ia]
        return self.Ur(t, a)


def get_G(CheapTalkGame):
    ineq_Hrep_Y, eq_Hrep_Y = get_Hrep_Y(CheapTalkGame)
    V, _, _ = h_rep_to_v_rep(ineq_Hrep_Y, eq_Hrep_Y, get_incidence=True)
    vertexes = project_on_RT(V)


def get_Hrep_Y(CheapTalkGame):
    lenT = len(CheapTalkGame.T)
    lenA = len(CheapTalkGame.A)

    ineqs, eqs = [], []

    eq = np.ones(lenT+2)
    eq[0] = -1
    eq[1] = 0
    eqs.append(eq)

    for it in range(lenT):
        ineq = np.zeros(lenT+2)
        ineq[it+2] = 1
        ineqs.append(ineq)

    for ia in range(lenA):
        ineq = np.zeros(lenT+2)
        ineq[1] = 1
        for it in range(lenT):
            ineq[it+2] = -CheapTalkGame.index_Ur(it, ia)
        ineqs.append(ineq)

    return ineqs, eqs


def project_on_RT(vertexes):
    for v in vertexes:
        v[0].pop(0)
    return vertexes

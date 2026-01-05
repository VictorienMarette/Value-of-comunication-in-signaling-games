import numpy as np
import itertools

from SignalingGame import SignalingGame
from simplex import vertexes, in_simplex


class ClearPunishSignalingGame(SignalingGame):

    def __init__(self, p, T, S, A, Us, Ur, P):
        super().__init__(p, T, S, A, Us, Ur)
        self.P = P
        if not self.chek_punish():
            raise ValueError("P isn't a clear punish")

    def chek_punish(self):
        if self.P is None:
            return False
        for t in self.T:
            for s in self.S:
                for a in self.A:
                    if self.Us(t, s, a) < self.Us(t, s, self.P(s)):
                        return False
        return True

    def get_ce_vertexes(self):
        conditions = self.__get_ce_conditions()
        return vertexes(conditions[0], conditions[1])

    def print_ce_outcome(self):
        vertexes = self.get_ce_vertexes()
        print("Vertex of outcome space:")
        i = 1
        for v in vertexes:
            print("Vertexe " + str(i), end="")
            self.print_outcome(v)
            i += 1

    def is_ce(self, x):
        cond = self.__get_ce_conditions()
        return in_simplex(x, cond[0], cond[1], 0.0001)

    @staticmethod
    def get_clear_punish(T, S, A, Us):
        def get_cp(s):
            for a in A:
                if is_cp(s, a):
                    return a
            return None

        def is_cp(s, a):
            for t in T:
                for a2 in A:
                    if Us(t, s, a) > Us(t, s, a2):
                        return False
            return True

        Punishs = {}
        for s in S:
            p = get_cp(s)
            if p is None:
                return None
            Punishs[s] = p

        def P(s):
            return Punishs[s]

        return P

    @classmethod
    def generate_random(cls, size_T, size_S, size_A):
        T = list(range(1, size_T + 1))
        S = list(range(1, size_S + 1))
        A = list(range(1, size_A + 1))
        p = np.random.rand(size_T)
        p = p / p.sum()
        P = None
        i = 0
        while P is None:
            Us_vec = 10*np.random.rand(size_T * size_S * size_A)
            def Us(t, s, a, offset=i):
                return Us_vec[(t-1) * size_S * size_A + (s-1)*size_A + a-1]
            Ur_vec = 10*np.random.rand(size_T * size_S * size_A)
            def Ur(t, s, a, offset=i):
                return Ur_vec[(t-1) * size_S * size_A + (s-1)*size_A + a-1]
            P = cls.get_clear_punish(T, S, A, Us)
            i += 1
        return cls(p, T, S, A, Us, Ur, P)

    def __get_ce_conditions(self, get_parameters=False):
        return (self.__get_ce_ineqs_prob(get_parameters)
                + self.__get_ce_ineqs_sender(get_parameters)
                + self.__get_ce_ineqs_recevier(get_parameters), 
                self.__get_ce_eqs_prob(get_parameters))

    def __get_ce_eqs_prob(self, get_parameters=False):
        lT = len(self.T)
        lS = len(self.S)
        lA = len(self.A)
        eqs = []
        for t in range(lT):
            v = np.zeros(lT*lS*lA)
            v[t*lS*lA:(t+1)*lS*lA] = 1
            if get_parameters:
                eqs.append((v, 1, self.T[t]))
            else:
                eqs.append((v, 1))
        return eqs

    def __get_ce_ineqs_prob(self, get_parameters=False):
        lT = len(self.T)
        lS = len(self.S)
        lA = len(self.A)
        ineqs = []
        for i in range(lT*lS*lA):
            v = np.zeros(lT*lS*lA)
            v[i] = -1
            if get_parameters:
                ineqs.append((v, 0, self.int_to_TxSxA(i)))
            else:
                ineqs.append((v, 0))
        return ineqs

    def __get_ce_ineqs_sender(self, get_parameters=False):
        lT = len(self.T)
        lS = len(self.S)
        lA = len(self.A)
        SS_funcs = list(itertools.product(self.S, repeat=lS))
        ineqs = []
        for t, t2, f in itertools.product(self.T, self.T, SS_funcs):
            v = np.zeros(lT*lS*lA)
            for s, a in itertools.product(self.S, self.A):
                si = self.S.index(s)
                v[self.TxSxA_to_int(t, s, a)] += -self.Us(t, s, a)
                if f[si] == s:
                    v[self.TxSxA_to_int(t2, s, a)] += self.Us(t, s, a)
                else:
                    v[self.TxSxA_to_int(t2, s, a)] += self.Us(t, f[si], self.P(f[si])) 
            if get_parameters:
                ineqs.append((v, 0, (t, t2, f)))
            else:
                ineqs.append((v, 0))
        return ineqs

    def __get_ce_ineqs_recevier(self, get_parameters=False):
        lT = len(self.T)
        lS = len(self.S)
        lA = len(self.A)
        ineqs = []
        for s, a, a2 in itertools.product(self.S, self.A, self.A):
            v = np.zeros(lT*lS*lA)
            for t in self.T:
                ti = self.T.index(t)
                v[self.TxSxA_to_int(t, s, a)] += self.p[ti]*(self.Ur(t, s, a2)-self.Ur(t, s, a))
            if get_parameters:
                ineqs.append((v, 0, (s, a, a2)))
            else:
                ineqs.append((v, 0))
        return ineqs

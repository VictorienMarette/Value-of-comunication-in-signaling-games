import numpy as np
import itertools

from simplex import sumed_vertexes, in_simplex


# Note: plus tard faire un classe clear punish quierite de signaling game
class SignalingGame:
    def __init__(self, p, T, S, A, Us, Ur, P=None):
        self.p = p
        self.T = T
        self.S = S
        self.A = A
        self.Us = Us
        self.Ur = Ur
        self.P = P

    def chek_punish(self):
        if self.P is None:
            return False
        for t in self.T:
            for s in self.S:
                for a in self.A:
                    if self.Us(t, s, a) < self.Us(t, s, self.P(s)):
                        return False
        return True

    def get_clear_punish_conditions(self, get_parameters=False):
        if not self.chek_punish():
            raise ValueError("The punish isn't clean")
        return (self.get_cp_ineqs_prob(get_parameters)
                + self.get_cp_ineqs_sender(get_parameters)
                + self.get_cp_ineqs_recevier(get_parameters),
                self.get_cp_eqs_prob(get_parameters))

    def get_cp_eqs_prob(self, get_parameters=False):
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

    def get_cp_ineqs_prob(self, get_parameters=False):
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

    def get_cp_ineqs_sender(self, get_parameters=False):
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

    def get_cp_ineqs_recevier(self, get_parameters=False):
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

    def TxSxA_to_int(self, t, s, a):
        lS = len(self.S)
        lA = len(self.A)
        ti = self.T.index(t)
        si = self.S.index(s)
        ai = self.A.index(a)
        return ti*lS*lA + si*lA + ai

    def int_to_TxSxA(self, i):
        lS = len(self.S)
        lA = len(self.A)
        ti, r = divmod(i, lS*lA)
        si, ai = divmod(r, lA)
        return (self.T[ti], self.S[si], self.A[ai])

    def get_clear_punish_vertexes(self):
        lT = len(self.T)
        lS = len(self.S)
        lA = len(self.A)
        conditions = self.get_clear_punish_conditions()
        return sumed_vertexes(conditions[0], conditions[1], lT*lS*lA, 0.01)

    def print_clear_punish_vertexes(self):
        vertexes = self.get_clear_punish_vertexes()
        print("Vertex of outcome space:")
        i = 1
        for v in vertexes:
            text = "Vertexe " + str(i) + ": "+str(int(v[1]))+" iter, Us="
            text2 = ""
            Us = 0
            Ur = 0
            for t in self.T:
                for s in self.S:
                    for a in self.A:
                        Us += float(v[0][self.TxSxA_to_int(t, s, a)])*self.p[self.T.index(t)]*self.Us(t, s, a)
                        Ur += float(v[0][self.TxSxA_to_int(t, s, a)])*self.p[self.T.index(t)]*self.Ur(t, s, a)
                        text2 += " pi("+s+","+a+"|"+t+")=" + str(round(float(v[0][self.TxSxA_to_int(t, s, a)]),6))
            print(text+str(round(Us, 4))+", Ur="+str(round(Ur, 4))+","+text2)
            i += 1

    def is_cp_ce(self, x):
        cond = self.get_clear_punish_conditions()
        return in_simplex(x, cond[0], cond[1], 0.0001)

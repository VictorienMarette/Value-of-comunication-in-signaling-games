import numpy as np


class SignalingGame:
    def __init__(self, p, T, S, A, Us, Ur):
        self.p = p
        self.T = T
        self.S = S
        self.A = A
        self.Us = Us
        self.Ur = Ur

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

    def is_ce(self, x):
        pass

    def is_bn(self, x, eps=1e-12):
        pass

    def E_Us(self, x):
        tot = 0
        for t in self.T:
            ti = self.T.index(t)
            for a in self.A:
                for s in self.S:
                    index = self.TxSxA_to_int(t, s, a)
                    tot += self.p[ti]*x[index]*self.Us(t, s, a)
        return tot

    def E_Ur(self, x):
        tot = 0
        for t in self.T:
            ti = self.T.index(t)
            for a in self.A:
                for s in self.S:
                    index = self.TxSxA_to_int(t, s, a)
                    tot += self.p[ti]*x[index]*self.Ur(t, s, a)
        return tot

    def __str__(self):
        txt = "SignalingGame:\n"
        txt += f"  T = {self.T}\n"
        txt += f"  S = {self.S}\n"
        txt += f"  A = {self.A}\n"
        txt += f"  p = {self.p}\n\n"

        txt += "  Payoffs Us(t, s, a):\n"
        for t in self.T:
            txt += f"    Type t = {t}:\n"
            for s in self.S:
                # Convert np.float64 -> float
                row = [float(self.Us(t, s, a)) for a in self.A]
                txt += f"      Signal s = {s}: {row}\n"
            txt += "\n"

        txt += "  Payoffs Ur(t, s, a):\n"
        for t in self.T:
            txt += f"    Type t = {t}:\n"
            for s in self.S:
                row = [float(self.Ur(t, s, a)) for a in self.A]
                txt += f"      Signal s = {s}: {row}\n"
            txt += "\n"

        return txt

    @classmethod
    def generate_random(cls, size_T, size_S, size_A):
        T = list(range(1, size_T + 1))
        S = list(range(1, size_S + 1))
        A = list(range(1, size_A + 1))
        p = np.random.rand(size_T)
        p = p / p.sum()
        Us_vec = 10*np.random.rand(size_T * size_S * size_A)
        def Us(t, s, a):
            return Us_vec[(t-1) * size_S * size_A + (s-1)*size_A + a-1]
        Ur_vec = 10*np.random.rand(size_T * size_S * size_A)
        def Ur(t, s, a):
            return Ur_vec[(t-1) * size_S * size_A + (s-1)*size_A + a-1]
        return cls(p, T, S, A, Us, Ur)

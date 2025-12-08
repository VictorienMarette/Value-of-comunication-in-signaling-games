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

    def is_bn(self, x):
        pass

    @classmethod
    def generate_random(cls, size_T, size_S, size_A):
        return 1

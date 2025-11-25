class SignalingGame:
    def __init__(self, T, S, A, Us, Ur, P=None):
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

    def get_clear_punish_ineqs(self):
        if not self.chek_punish():
            raise ValueError("The punish isn't clean")
        return self.get_cp_ineqs_prob()+self.get_cp_ineqs_sender()+self.get_cp_ineqs_recevier()

    def get_cp_ineqs_prob(self):
        pass

    def get_cp_ineqs_sender(self):
        pass

    def get_cp_ineqs_recevier(self):
        pass

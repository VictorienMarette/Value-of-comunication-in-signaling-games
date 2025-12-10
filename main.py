from ClearPunishSignalingGame import ClearPunishSignalingGame

while True:
    G = ClearPunishSignalingGame.generate_random(2, 2, 2)
    V = G.get_ce_vertexes()
    BN = False
    bestBn = -15
    bestCE = 0
    for v in V:
        v0 = v[0][0].flatten()
        if G.is_bn(v0):
            Bn = True
            if G.E_us(v0) > bestBn:
                bestBn = G.E_us(v0)
        else:
            if G.E_us(v0) > bestCE:
                bestCE = G.E_us(v0)
    if not BN:
        print("BN pas vertex")
        print(G)
    elif bestBn < bestCE - 1e-12:
        print("BN not best")
        print(G)

from CheapTalkGame import *

T = ["L", "H"]
A = ["a1", "a2", "a3"]


def Us(t, a):
    if t == "L":
        if a == "a1":
            return 2
        elif a == "a2":
            return 3
        else:
            return 1
    if t == "H":
        if a == "a1":
            return 0
        elif a == "a2":
            return 2
        else:
            return 3


def Ur(t, a):
    if t == "L":
        if a == "a1":
            return 3
        elif a == "a2":
            return 2
        else:
            return 0
    if t == "H":
        if a == "a1":
            return 0
        elif a == "a2":
            return 2
        else:
            return 3


Game = CheapTalkGame(T, A, Us, Ur)


get_G(Game)
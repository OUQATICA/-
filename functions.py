import random as rd


def dictgen(keys):
    res = {}
    for i in range(len(keys)-rd.randint(1, len(keys)-1)):
        res[keys[rd.randint(0, len(keys)-1)]] = rd.randint(1, 3)
    return res

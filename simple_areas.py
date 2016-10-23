from math import sqrt, pi

def simple_areas(*args):
    x = len(args)
    if x == 1:
        return round(pi * (args[0] / 2.0) * (args[0] / 2.0), 2)
    if x == 2:
        return round(args[0] * args[1], 2)

    s = sum(args) / 2.0
    return round(sqrt(s * (s - args[0]) * (s - args[1]) * (s - args[2])), 2)

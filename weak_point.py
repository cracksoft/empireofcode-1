def golf(m):
    r = [sum(i) for i in m]
    x = [sum(i) for i in zip(*m)]
    return [r.index(min(r)),x.index(min(x))]

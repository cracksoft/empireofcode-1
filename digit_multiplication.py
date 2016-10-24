def golf(x):
    b = 1
    for a in ([int(i) for i in list(str(x)) if i > '1']):
        b *= a
    return b

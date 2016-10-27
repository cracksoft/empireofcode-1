def letter_queue(commands):
    x = []
    for c in commands:
        if c[1] == 'U':
            x.append(c[5:])
        elif x:
            x = x[1:]
    return ''.join(x)

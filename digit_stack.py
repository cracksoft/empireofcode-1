def golf(commands):
    k = []
    sum = 0
    for x in commands:
        y = x.split()
        if y[0] == "PUSH":
            k.append(int(y[1]))
        elif y[0] == "POP":
            sum += k.pop() if len(k) > 0 else 0
        else:
            sum += k[len(k)-1] if len(k) > 0 else 0
    return sum

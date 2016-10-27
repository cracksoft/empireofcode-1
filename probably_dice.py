MAX_VAL = 201

def increase(counter, sides):
    tmp = [0 for i in range(len(counter)+sides+1)]
    for i in range(1, sides+1):
        for c in range(len(counter)):
            if counter[c] != 0:
                tmp[c + i] += counter[c]
    return tmp


def probability(dice_number, sides, target):
    counter = [0] + [1 for _ in range(sides)] 
    for _ in range(dice_number-1):
        counter = increase(counter, sides)

    return round(counter[target] / sum(counter), 4) if target < len(counter) else 0

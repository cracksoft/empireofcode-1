from fractions import gcd

def divide_pie(groups):
    m = sum([abs(x) for x in groups])

    num = m
    den = m

    for i in range(len(groups)):
        if groups[i] < 0:
            num *= (m + groups[i])
            den *= m
        else:
            num -= (groups[i] * (den/m))

    x = gcd(num, den)
    return num//x, den//x

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert isinstance((2, -2), (tuple, list)), "Return tuple or list"
    assert tuple(divide_pie((2, -1, 3))) == (1, 18), "Example"
    assert tuple(divide_pie((1, 2, 3))) == (0, 1), "All know about the pie"
    assert tuple(divide_pie((-1, -1, -1))) == (8, 27), "One by one"
    assert tuple(divide_pie((10,))) == (0, 1), "All together"
    print("Code's finished? Earn rewards by clicking 'Check' to review your tests!")

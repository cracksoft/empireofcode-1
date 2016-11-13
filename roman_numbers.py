def roman(number):
    x = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}
    y = 1000
    r = ''

    while y > 0:
        t = number // y
        number %= y
        if t == 4 or t == 9:
            r += (x[y] + x[(t+1)*y])
        elif t < 4 and t > 0:
            r += (''.join([x[y] * t]))
        elif t > 4:
            r += (x[5*y] + ''.join([x[y] * (t-5)]))
        y //= 10
    return r


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert roman(6) == 'VI', '6'
    assert roman(76) == 'LXXVI', '76'
    assert roman(499) == 'CDXCIX', '499'
    assert roman(3888) == 'MMMDCCCLXXXVIII', '3888'
    print("Earn cool rewards by using the 'Check' button!")

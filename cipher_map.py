def solve(a, b):
    res = ''
    for i in range(0, len(a)):
        for j in range(0, len(a)):
            if a[i][j] == 'X':
                res += b[i][j]
    return res

def recall_password(cipher_grille, ciphered_password):
    c = [list(i) for i in list(cipher_grille)]
    d = [list(i) for i in list(ciphered_password)]

    res = solve(c, d)
    x = []
    for _ in range(0, 3):
        c = list(zip(*c[::-1]))
        x.append(solve(c, d))

    if d[0][0].isupper():
        return res + ''.join(x[::-1])
    return res + ''.join(x)

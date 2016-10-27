FONT = ("--X--XXX-XXX-X-X-XXX--XX-XXX-XXX--XX-XX--"
        "-XX----X---X-X-X-X---X-----X-X-X-X-X-X-X-"
        "--X---XX--X--XXX-XX--XXX--X--XXX-XXX-X-X-"
        "--X--X-----X---X---X-X-X-X---X-X---X-X-X-"
        "--X--XXX-XXX---X-XX---XX-X---XXX-XX---XX-")


f = [[] for _ in range(0, 10)]
c = 1
for i in range(1, 41, 4):
    for j in range(0, 5):
        k = (41*j)+i
        f[c%10] += FONT[k:k+3]
        f[c%10] = [1 if x == 'X' else 0 for x in f[c%10]]
        c += 1

def diff(s1, s2):
    return sum(1 if a!=b else 0 for a,b in zip(s1,s2))

def recognize(image):
    res = ''
    for i in range(1, len(image[0]), 4):
        x = []
        for j in range(0, 5):
            x += image[j][i:i+3]
        res += str(sorted([(diff(x, f[j]), j) for j in range(0, 10)])[0][1])
    return int(res)

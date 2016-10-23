from math import acos, degrees

get_angle = lambda a, b, c: round(degrees(acos((b*b+c*c-a*a)/(float(2*b*c)))))


def angles(a, b, c):
    return [0, 0, 0] if a + b <= c or b + c <= a or c + a <= b else \
        sorted([get_angle(a, b, c), get_angle(b, c, a), get_angle(c, a, b)])

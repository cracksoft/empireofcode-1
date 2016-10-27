import re

def pp(x):
    x = round(x, 2)
    return int(x) if int(x) == x else x

def circle_equation(note):
    [[x1, y1], [x2, y2], [x3, y3]] = [[int(a) for a in i.split(',')] for i in re.findall('([-]?\d,[-]?\d)',note)]

    a = x1*(y2-y3)-y1*(x2-x3)+x2*y3-x3*y2
    b = ((x1*x1+y1*y1)*(y3-y2)+(x2*x2+y2*y2)*(y1-y3)+(x3*x3+y3*y3)*(y2-y1))/a
    c = ((x1*x1+y1*y1)*(x2-x3)+(x2*x2+y2*y2)*(x3-x1)+(x3*x3+y3*y3)*(x1-x2))/a
    d = ((x1*x1+y1*y1)*(x3*y2-x2*y3)+(x2*x2+y2*y2)*(x1*y3-x3*y1)+(x3*x3+y3*y3)*(x2*y1-x1*y2))/a

    x = -b/2
    y = -c/2
    r = ((b*b+c*c-4*d)/4)**0.5

    return "(x-%s)^2+(y-%s)^2=%s^2" % (pp(x), pp(y), pp(r))

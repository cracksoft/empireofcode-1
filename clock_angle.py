def clock_angle(time):
    [h,m] = map(int, time.split(":"))
    if h > 12:
        h -= 12
    x = abs(0.5 * (60*h-11*m))
    return min(x, 360-x)

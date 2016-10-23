def count_units(number):
    return sum(int(x) for x in list(format(number, 'b')))

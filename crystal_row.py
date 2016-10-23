def check_line(line):
    z = ''
    for i in line:
        if i == z:
            return False
        z = i
    return True

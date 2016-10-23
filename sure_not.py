def sure_not(line):
    return ("not " if line.find('not ') < 0 else "") + line

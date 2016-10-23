def boolean(x, y, operation):
    if operation == "conjunction":
        return x and y
    if operation == "disjunction":
        return x or y
    if operation == "implication":
        return not x or y
    if operation == "exclusive":
        return x^y

    return (x == y)

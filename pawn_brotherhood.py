def safe_pawns(pawns):
    s = 0
    for x,y in pawns:
        x = ord(x)
        y = int(y)

        s = s + ((chr(x+1)+str(y-1)) in pawns or (chr(x-1)+str(y-1)) in pawns)
    return s


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1

    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")

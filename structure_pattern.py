def base(n, b):
    if n == 0: return '0'
    r = ""
    while n!= 0:
        r += str(n%b)
        n //= b
    return r[::-1]

def conv(a, pl):
    if a == ' ': return '3'
    return '2' if pl != 2 and a.isupper() else '1'

def check_structure(pattern, structure, pattern_level=2):
    return base(pattern, pattern_level).zfill(len(structure)) == \
        ''.join('0' if i.isdigit() else conv(i, pattern_level) for i in structure)

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    # Rank 1
    assert check_structure(42, "12a0b3e4"), "42 is the answer"
    assert not check_structure(101, "ab23b4zz"), "one hundred plus one"
    assert check_structure(0, "478103487120470129"), "Any number"
    assert check_structure(127, "Checkio"), "Uppercase"
    assert not check_structure(7, "Hello"), "Only full match"
    assert not check_structure(8, "a"), "Too short command"
    assert check_structure(5, "H2O"), "Water"
    assert not check_structure(42, "C2H5OH"), "Yep, this is not the Answer"
    
    # Rank 2
    assert check_structure(1823, 'CheckiO', 3), "up and down"
    assert not check_structure(1826, 'CheckiO', 3), "wrong up and down"
    assert check_structure(66431, '9z1b2c4d6a7Z', 3), "Various"
    
    # Rank 3
    assert not check_structure(39294315, 'Kill Them ALL', 4), "Don't kill"
    assert not check_structure(29, 'aXz', 4), "A Z"
    assert check_structure(39294442, 'Feed Them ALL', 4), "Feed them"
    assert check_structure(2385166685525, 'C3PO and 300 spartans', 4), "C3PO"
    
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")

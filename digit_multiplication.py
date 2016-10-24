def golf(x):
    t = 1
    for i in str(x):
        t *= max(int(i),1)
    return t

if __name__ == '__main__':
    assert golf(123405) == 120
    assert golf(999) == 729
    assert golf(1000) == 1
    assert golf(1111) == 1
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")

def good_radix(str_number):
    for k in range(2, 38):
        try:
            if int(str_number, k) % (k-1) == 0:
                return k
        except:
            pass
    return 0


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert good_radix("18") == 10, "Simple decimal"
    assert good_radix("1010101011") == 2, "Any number is divisible by 1"
    assert good_radix("222") == 3, "3rd test"
    assert good_radix("A23B") == 14, "It's not a hex"
    assert good_radix("IDDQD") == 0, "k is not exist"
    
    
    print("Now that you're finished, hit the 'Check' button to review your code and earn sweet rewards!")

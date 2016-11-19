from decimal import *

def convert(num, den):
    getcontext().prec = 1000
    x = str(Decimal(num)/Decimal(den)).split(".")
    try:
        y = x[1]
        length = len(y)
        for i in range(length):
            for j in range(i+1, length):
                substr = y[i:j]
                if y[j:].find(substr) == 0 and y[j:j+(len(substr)*3)].count(substr) == 3:
                    return "%s.%s(%s)" % (x[0],y[:i],substr)
    except:
        pass
    return x[0] + "." + (x[1] if len(x) > 1 else '')


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert convert(1, 3) == "0.(3)", "1/3 Classic"
    assert convert(5, 3) == "1.(6)", "5/3 The same, but bigger"
    assert convert(3, 8) == "0.375", "3/8 without repeating part"
    assert convert(7, 11) == "0.(63)", "7/11 prime/prime"
    assert convert(29, 12) == "2.41(6)", "29/12 not and repeating part"
    assert convert(11, 7) == "1.(571428)", "11/7 six digits"
    assert convert(0, 117) == "0.", "Zero"
    assert convert(1, 1000) == "0.001", "Zero"
    assert convert(1, 999) == "0.(001)", "Zero"
    
    print("Earn cool rewards by using the 'Check' button!")

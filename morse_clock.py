def morse_time(time_string):
    t = ''.join([i.zfill(2) for i in time_string.split(":")])
    y = [2, 4, 3, 4, 3, 4]
    x = [bin(int(t[i]))[2:].zfill(y[i]).replace('0','.').replace('1','-') for i in range(6)] 
    return "%s %s : %s %s : %s %s" % (x[0],x[1],x[2],x[3],x[4],x[5])


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert morse_time("10:37:49") == ".- .... : .-- .--- : -.. -..-", "First Test"
    assert morse_time("21:34:56") == "-. ...- : .-- .-.. : -.- .--.", "Second Test"
    assert morse_time("00:1:02") == ".. .... : ... ...- : ... ..-.", "Third Test"
    assert morse_time("23:59:59") == "-. ..-- : -.- -..- : -.- -..-", "Fourth Test"
    
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")

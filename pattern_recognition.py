def doit(a, b, y, x, yy, xx):
    for i in range(yy):
        if b[y+i][x:(x+xx)] != a[i]:
            return b

    for i in range(yy):
        for j in range(xx):
            b[y+i][x+j] += 2
    return b
    
def mark_patterns(pattern, image):
    py = len(pattern)
    px = len(pattern[0])
    iy = len(image)
    ix = len(image[0])
    dy = iy-py+1
    dx = ix-px+1

    for i in range(dy):
        for j in range(dx):
            image = doit(pattern, image, i, j, py, px)
    return image


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert mark_patterns([[1, 0], [1, 1]],
            [[0, 1, 0, 1, 0],
            [0, 1, 1, 0, 0],
            [1, 0, 1, 1, 0],
            [1, 1, 0, 1, 1],
            [0, 1, 1, 0, 0]]) == [[0, 3, 2, 1, 0],
                    [0, 3, 3, 0, 0],
                    [3, 2, 1, 3, 2],
                    [3, 3, 0, 3, 3],
                    [0, 1, 1, 0, 0]], "1st"
    assert mark_patterns([[1, 1], [1, 1]],
            [[1, 1, 1],
            [1, 1, 1],
            [1, 1, 1]]) == [[3, 3, 1],
                    [3, 3, 1],
                    [1, 1, 1]], "2nd"
    assert mark_patterns([[0, 1, 0], [1, 1, 1]],
            [[0, 0, 1, 0, 0, 0, 0, 0, 1, 0],
            [0, 1, 1, 1, 0, 0, 0, 1, 1, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
            [0, 1, 0, 0, 1, 1, 1, 0, 1, 0],
            [1, 1, 1, 0, 0, 0, 0, 0, 1, 1],
            [0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
            [0, 1, 1, 0, 0, 0, 1, 1, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]) == [[0, 2, 3, 2, 0, 0, 0, 2, 3, 2],
                    [0, 3, 3, 3, 0, 0, 0, 3, 3, 3],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 2, 3, 2, 0, 0, 0],
                    [2, 3, 2, 0, 3, 3, 3, 0, 1, 0],
                    [3, 3, 3, 0, 0, 0, 0, 0, 1, 1],
                    [0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
                    [0, 0, 1, 0, 0, 0, 2, 3, 2, 0],
                    [0, 1, 1, 0, 0, 0, 3, 3, 3, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]], "3rd"
    
    print("Now that you're finished, hit the 'Check' button to review your code and earn sweet rewards!")

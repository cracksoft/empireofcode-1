def danger(board, row, col):
    for (i,j) in board:
        if row == i or col ==j or abs(row-i) == abs(col-j):
            return True
    return False

def place(board, left):
    if not left:
        return (True, board)

    row = left[0]
    for col in range(1, 9):
        if not danger(board, row, col):
            board.append((row, col))
            (ok, board) = place(board, left[1:])
            if ok:
                return (ok, board)
            else:
                board.remove((row, col))
    
    return (False, board)

def place_queens(placed):
    row = []
    board = []
    left = []

    for p in placed:
        y = ord(p[0])-96
        x = int(p[1])
        row.append(y)
        if danger(board, y, x): return set()
        board.append((y, x))

    for i in range(1, 9):
        if i not in row:
            left.append(i)

    ok, board = place(board, left)

    if ok:
        return set([chr(i+96)+str(j) for i,j in board])
    return set()

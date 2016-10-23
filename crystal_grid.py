def check_grid(grid):
    if any(check_row(row) for row in grid):
        return False
    return not any(check_row(row) for row in zip(*grid))


def check_row(row):
    for i in range(1, len(row)):
        if row[i] == row[i-1]:
            return True
    return False

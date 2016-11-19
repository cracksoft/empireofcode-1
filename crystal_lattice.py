def check(row):
    for i in range(1, len(row)):
        if row[i] == row[i-1]:
            return True
    return False

def golf(cube):
    x = [check(row) for grid in cube for row in grid]
    x += [check(row) for grid in cube for row in zip(*grid)]
    x += [check(row) for grid in zip(*cube) for row in zip(*grid)]
    return not any(x)

if __name__ == "__main__":
    assert golf([[["a", "b"],
                  ["c", "d"]],
                 [["e", "f"],
                  ["g", "h"]]]) == True, "st example"
 
    assert golf([[["X", "Z"],
                  ["Z", "X"]],
                 [["Z", "X"],
                  ["X", "Z"]]]) == True, "1st example"
    assert golf([[["X", "Z"],
                  ["Z", "X"]],
                 [["X", "Z"],
                  ["Z", "X"]]]) == False, "2nd example"
    print("All done? Earn rewards by using the 'Check' button!")
